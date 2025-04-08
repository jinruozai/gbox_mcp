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

DOC_DIR = "gbox_doc"
SYNTAX_DOC_PATH = os.path.join(DOC_DIR, "gbox_syntax.md")
API_DOC_PATH = os.path.join(DOC_DIR, "gbox_api.md")

@mcp.resource("gbox://doc/syntax")
def get_syntax_doc() -> str:
    """Provides the content of the GBox syntax documentation (gbox_syntax.md) as a resource."""
    try:
        with open(SYNTAX_DOC_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Syntax documentation file not found at {SYNTAX_DOC_PATH}")
        return f"Error: Syntax documentation file not found at {SYNTAX_DOC_PATH}" # Return error message to client
    except Exception as e:
        print(f"Error loading syntax documentation file {SYNTAX_DOC_PATH}: {e}")
        return f"Error loading syntax documentation file {SYNTAX_DOC_PATH}: {e}" # Return error message to client

@mcp.resource("gbox://doc/api")
def get_api_doc() -> str:
    """Provides the content of the GBox API documentation (gbox_api.md) as a resource."""
    try:
        with open(API_DOC_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: API documentation file not found at {API_DOC_PATH}")
        return f"Error: API documentation file not found at {API_DOC_PATH}" # Return error message to client
    except Exception as e:
        print(f"Error loading API documentation file {API_DOC_PATH}: {e}")
        return f"Error loading API documentation file {API_DOC_PATH}: {e}" # Return error message to client

@mcp.tool()
def gbox_version() -> str:
    """Returns the current GBox engine version by attempting to call 'get_gbox_version' via the GBox connection."""
    global gbox
    if gbox:
        try:
            version_info = gbox.call(None, "get_gbox_version") 
            return f"GBox Version: {str(version_info)}" 
        except Exception as e:
            return f"Error attempting to call get_gbox_version via GBox connection: {e}"
    else:
        return "GBox connection has not been initialized. Cannot retrieve version."

if __name__ == "__main__":
    # 解析命令行参数并获取有效参数
    params = parse_args()
    print(f"使用服务器配置:", ", ".join(f"{k}={v}" for k, v in params.items()) or "使用默认配置")
    
    # 初始化GBoxTCP实例
    gbox = GBoxTCP(**params)

    # 初始化工具
    init_tools()

    # 初始化工具 (Dynamically fetched from GBox)
    init_tools() 

    # --- Remove explicit tool registration ---
    # The gbox_version tool is now registered via the @mcp.tool() decorator above.
    # The documentation resources (gbox://doc/syntax, gbox://doc/api) are registered via the @mcp.resource decorator above.
    
    # Attempt to notify about tool changes (from init_tools). 
    # Statically registered tools/resources are available immediately.
    try:
        if hasattr(mcp._mcp_server, 'send_notification'):
            mcp._mcp_server.send_notification('$/tools/changed', None)
            print("Sent notification about dynamically fetched tool changes.")
    except Exception as e:
        print(f"发送工具变更通知时出错: {str(e)}")

    mcp.run(transport='stdio')
    
    