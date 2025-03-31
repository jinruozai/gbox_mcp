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
    tools_info = gbox.call("get_tools")
    print("tools_info:", tools_info)
    
    # 遍历工具列表并添加到MCP
    for name, info in tools_info.items():
        # 为每个工具创建一个lambda函数，捕获工具名称
        tool_func = lambda tool_name=name: gbox.call(tool_name)
        # 添加工具到MCP
        mcp.add_tool(
            tool_func,
            name=name,
            description=info["description"]
        )
    print(f"成功初始化 {len(tools_info)} 个工具")

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
    