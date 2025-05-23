#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用WebSocket接口执行ComfyUI工作流并实时获取图像
基于官方websockets_api_example_ws_images.py示例修改
"""

import websocket  # 需要安装: pip install websocket-client
import uuid
import json
import urllib.request
import urllib.parse
import os
import argparse
import io
from PIL import Image

# ComfyUI服务器地址
server_address = "127.0.0.1:8188"

class ComfyUI:
    def __init__(self, server_addr=None):
        self.server_address = server_addr or server_address
        self.client_id = str(uuid.uuid4())
    
    def queue_prompt(self, prompt):
        """将工作流发送到ComfyUI服务器并排队执行"""
        p = {"prompt": prompt, "client_id": self.client_id}
        data = json.dumps(p).encode('utf-8')
        req = urllib.request.Request(f"http://{self.server_address}/prompt", data=data)
        try:
            return json.loads(urllib.request.urlopen(req).read())
        except urllib.error.HTTPError as e:
            print(f"HTTP错误: {e.code} - {e.reason}")
            print("请求数据:", json.dumps(p, indent=2))
            raise

    def get_images(self, ws, prompt):
        """通过WebSocket连接获取图像"""
        print("正在提交工作流...")
        prompt_id = self.queue_prompt(prompt)['prompt_id']
        print(f"等待图像生成，任务ID: {prompt_id}")
        
        output_images = {}
        current_node = ""
        
        while True:
            out = ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message['type'] == 'executing':
                    data = message['data']
                    if data['prompt_id'] == prompt_id:
                        if data['node'] is None:
                            print("工作流执行完成!")
                            break  # 执行完成
                        else:
                            current_node = data['node']
                            print(f"正在执行节点: {current_node}")
            else:
                # 这是图像数据
                print(f"收到来自节点 '{current_node}' 的图像数据")
                images_output = output_images.get(current_node, [])
                images_output.append(out[8:])  # 去掉WebSocket图像前缀
                output_images[current_node] = images_output
        
        return output_images

    def add_websocket_node(self, workflow_data):
        """添加SaveImageWebsocket节点到工作流"""
        # 检查工作流中是否已经有SaveImageWebsocket节点
        for node_id, node in workflow_data.items():
            if node.get("class_type") == "SaveImageWebsocket":
                print("工作流已包含SaveImageWebsocket节点")
                return workflow_data
        
        # 查找VAEDecode节点和SaveImage节点
        vae_node_id = None
        save_node_id = None
        save_node_input = None
        
        for node_id, node in workflow_data.items():
            if node.get("class_type") == "VAEDecode":
                vae_node_id = node_id
            elif node.get("class_type") == "SaveImage":
                save_node_id = node_id
                if "inputs" in node and "images" in node["inputs"]:
                    save_node_input = node["inputs"]["images"]
        
        # 如果找到SaveImage节点的输入，使用它
        if save_node_input:
            input_source = save_node_input
            print(f"使用SaveImage节点的输入源: {input_source}")
        # 否则尝试使用VAEDecode节点的输出
        elif vae_node_id:
            input_source = [vae_node_id, 0]
            print(f"使用VAEDecode节点输出作为输入源: {input_source}")
        else:
            print("警告: 无法找到合适的图像输入源，工作流可能无法正常工作")
            return workflow_data
        
        # 添加SaveImageWebsocket节点
        workflow_data["save_image_websocket_node"] = {
            "class_type": "SaveImageWebsocket",
            "inputs": {
                "images": input_source
            }
        }
        
        print("已添加SaveImageWebsocket节点到工作流")
        return workflow_data
    
    def generate_images(self, prompt_text=None, workflow_path=None, output_dir="output"):
        """
        生成图像并返回保存的文件路径列表
        
        Args:
            prompt_text: 提示词文本
            workflow_path: 工作流文件路径
            output_dir: 输出目录
        
        Returns:
            保存的图像路径列表
        """
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 加载工作流JSON文件
        if workflow_path and os.path.exists(workflow_path):
            workflow_file = workflow_path
            print(f"使用指定的工作流文件: {workflow_file}")
        else:
            # 使用默认路径
            workflow_file = os.path.join(os.path.dirname(__file__), "sd_base.json")
            if not os.path.exists(workflow_file):
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                workflow_file = os.path.join(base_dir, "comfyui", "sd_base.json")
            print(f"使用默认工作流文件: {workflow_file}")
        
        try:
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
        except Exception as e:
            print(f"加载工作流文件失败: {e}")
            raise
        
        # 如果提供了提示词，修改工作流
        if prompt_text:
            if "6" in workflow_data and "inputs" in workflow_data["6"] and "text" in workflow_data["6"]["inputs"]:
                old_prompt = workflow_data["6"]["inputs"]["text"]
                workflow_data["6"]["inputs"]["text"] = prompt_text
                print(f"已修改提示词:")
                print(f"原始: {old_prompt}")
                print(f"新的: {prompt_text}")
            else:
                print("警告: 未找到提示词节点，将使用原始提示词")
        else:
            print("未提供提示词，使用原始提示词")
        
        # 添加SaveImageWebsocket节点到工作流
        workflow_data = self.add_websocket_node(workflow_data)
        
        # 连接WebSocket
        print(f"连接WebSocket服务器: ws://{self.server_address}/ws?clientId={self.client_id}")
        ws = websocket.WebSocket()
        
        saved_paths = []
        
        try:
            ws.connect(f"ws://{self.server_address}/ws?clientId={self.client_id}")
            
            # 获取图像
            images = self.get_images(ws, workflow_data)
            
            # 保存图像
            image_count = 0
            for node_id, image_list in images.items():
                for i, image_data in enumerate(image_list):
                    try:
                        image = Image.open(io.BytesIO(image_data))
                        output_name = f"ws_image_{image_count}.png"
                        output_path = os.path.join(output_dir, output_name)
                        image.save(output_path)
                        saved_paths.append(output_path)
                        print(f"图像已保存: {output_path}")
                        image_count += 1
                    except Exception as e:
                        print(f"保存图像失败: {e}")
            
            print(f"\n成功生成并保存 {image_count} 张图像")
            
        except Exception as e:
            print(f"执行工作流时出错: {e}")
            raise
        finally:
            ws.close()
        
        return saved_paths

def run_comfyui(prompt=None, output_dir="output", workflow_file=None, server_addr=None):
    """运行ComfyUI生成图像的便捷函数"""
    comfy = ComfyUI(server_addr)
    return comfy.generate_images(prompt, workflow_file, output_dir)

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='执行ComfyUI工作流并实时获取图像')
    parser.add_argument('prompt', nargs='?', help='可选的提示词，如不提供则使用原始提示词')
    parser.add_argument('--output', '-o', default="output", help='图像输出目录')
    parser.add_argument('--workflow', '-w', help='工作流JSON文件路径，如不提供则使用默认路径')
    parser.add_argument('--server', '-s', help='ComfyUI服务器地址')
    args = parser.parse_args()
    
    # 运行ComfyUI
    try:
        run_comfyui(
            prompt=args.prompt,
            output_dir=args.output,
            workflow_file=args.workflow,
            server_addr=args.server
        )
    except Exception as e:
        print(f"执行失败: {e}")
        import sys
        sys.exit(1) 