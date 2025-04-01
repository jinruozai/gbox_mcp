import os
import sys
import asyncio
import threading
import argparse
from mcp.server.fastmcp import FastMCP
from gboxudp import GBoxUDP

# 定义全局变量
gbox = None

# 初始化MCP
mcp = FastMCP("GBox")

def init_tools():
    """初始化所有工具"""
    # 获取工具列表
    tools_info = gbox.call(None, "get_tools")  # obj 为 None，因为是全局函数
    print("tools_info:", tools_info)
    print("tools_info type:", type(tools_info))
    
    # 检查tools_info是否为列表类型
    if not isinstance(tools_info, list):
        print(f"获取到的工具信息格式不正确: {tools_info}")
        return
        
    # 遍历工具列表并添加到MCP
    try:
        for tool in tools_info:
            # 检查工具信息是否包含必要的字段
            if not isinstance(tool, dict) or 'name' not in tool or 'description' not in tool:
                print(f"工具信息格式不正确，跳过: {tool}")
                continue
                
            # 为每个工具创建一个lambda函数，捕获工具名称、对象引用和参数定义
            tool_func = lambda tool_name=tool['name'], tool_obj=tool['obj'], tool_params=tool.get('parameters'): \
                gbox.call(tool_obj, tool_name, tool_params)
                
            # 添加工具到MCP
            mcp.add_tool(
                tool_func,
                name=tool['name'],
                description=tool['description']
            )
        print(f"成功初始化 {len(tools_info)} 个工具")
    except Exception as e:
        print(f"初始化工具时发生错误: {str(e)}")

# 解析命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description='GBox MCP服务器')
    parser.add_argument('--ip', type=str, help='服务器IP地址')
    parser.add_argument('--port', type=int, help='服务器端口')
    args = parser.parse_args()
    return {k: v for k, v in vars(args).items() if v is not None}

if __name__ == "__main__":
    # 解析命令行参数并获取有效参数
    params = parse_args()
    print(f"使用服务器配置:", ", ".join(f"{k}={v}" for k, v in params.items()) or "使用默认配置")
    
    # 初始化GBoxUDP实例
    gbox = GBoxUDP(**params)
    
    # 初始化工具
    init_tools()
    
    # 启动MCP服务器
    mcp.run(transport='stdio')
    