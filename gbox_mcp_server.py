import os
import sys
import asyncio
import threading
import argparse
from mcp.server.fastmcp import FastMCP
from gboxudp import GBoxUDP

# 定义全局变量
gbox = None

def hello_mcp():
    try:
        des = get_mcp_description()
        print("start mcp server:", des)
    except Exception as e:
        print("获取MCP描述失败:", e)

# 初始化MCP
mcp = FastMCP("GBox")

@mcp.tool()
def get_mcp_description():
    """获取MCP描述
    Returns:
        str: MCP的简短描述
    """
    return gbox.call("get_mcp_description")

@mcp.tool()
def get_scene_range():
    """获取场景地图的尺寸范围
    Returns:
        dict: 包含地图边界坐标(xmin,ymin,xmax,ymax)的字典
    """
    return gbox.call("get_scene_range")

@mcp.tool()
def create_rand_object():
    """在场景中的随机位置创建一个随机物体
    Returns:
        dict: 包含创建结果的字典
    """
    return gbox.call("create_rand_object")

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
    
    # 在新线程中获取并打印MCP描述
    hello_mcp()
    
    # 启动MCP服务器
    mcp.run(transport='stdio')
    