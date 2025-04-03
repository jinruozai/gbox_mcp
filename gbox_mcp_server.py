import os
import sys
import asyncio
import threading
import argparse
from mcp.server.fastmcp import FastMCP
from gboxtcp import GBoxTCP
import time
# 定义全局变量
gbox = None

# 初始化MCP
from mcp.server.lowlevel.server import NotificationOptions
mcp = FastMCP("GBox")
# 启用工具变更通知
mcp._mcp_server.notification_options.tools_changed = True

def fetch_tools(tagmcp,funname,params=None)->bool:
    """初始化所有工具"""
    # 获取工具列表
    tools_info = gbox.call(None, funname,params)  # obj 为 None，因为是全局函数
    
    # 检查tools_info是否为列表类型
    if not isinstance(tools_info, list):
        print(f"获取到的工具信息格式不正确: {tools_info}")
        return False
        
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
            tagmcp.add_tool(
                tool_func,
                name=tool['name'],
                description=tool['description']
            )
        print(f"成功初始化 {len(tools_info)} 个工具")
        
        # 尝试通知工具变更
        try:
            if hasattr(tagmcp._mcp_server, 'send_notification'):
                tagmcp._mcp_server.send_notification('$/tools/changed', None)
        except Exception as e:
            print(f"发送工具变更通知时出错: {str(e)}")
        
        return True
    except Exception as e:
        print(f"初始化工具时发生错误: {str(e)}")
    return False


def init_tools():
    fetch_tools(mcp,"get_tools")

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
    gbox = GBoxTCP(**params)

    testdata = gbox.call("基本工具", "get_role_test_data")
    print(testdata)
    # 初始化工具
    init_tools()
    mcp.run(transport='stdio')
    
    