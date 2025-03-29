import os
import json
import struct
import socket
import time
import sys
from mcp.server.fastmcp import FastMCP

# GBox 工具列表定义
GBOX_TOOLS = {
    "get_weather": {
        "name": "get_weather",
        "description": "获取指定城市的天气信息",
        "function": "get_weather",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名称",
                    "default": "Beijing"
                }
            }
        }
    }
    # 在这里添加更多工具...
}

class GBoxCommunicator:
	def __init__(self, ip='127.0.0.1', port=20000):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 允许端口重用
		self.sock.bind(('0.0.0.0', 0))  # 让系统自动分配端口
		self.listen_port = self.sock.getsockname()[1]  # 获取系统分配的端口号
		self.sock.settimeout(5)
		print(f"UDP socket 已绑定到端口 {self.listen_port}")
		
	def send_gbox_str(self, message: str) -> None:
		"""发送字符串到GBox设备"""
		# 打包字符串数据
		msg_bytes = message.encode('utf-8')
		msg_len = len(msg_bytes)
		if msg_len == 0:
			var = struct.pack('B', 0xB0)
		elif msg_len <= 0xFF:
			var = struct.pack('BB', 0xB1, msg_len)
		elif msg_len <= 0xFFFF:
			var = struct.pack('<BH', 0xB2, msg_len)
		else:
			var = struct.pack('<BI', 0xB3, msg_len)
		var_data = var + msg_bytes
		
		# 构造完整消息
		header = struct.pack('<I', 0xBE33EE38)  # 魔数
		length = struct.pack('<I', len(var_data) + 20)  # 总长度
		cmd_type = struct.pack('<I', 2)  # 命令类型
		cmd_id = struct.pack('<I', 1)  # 命令ID
		var_len = struct.pack('<I', len(var_data))  # 变量数据长度
		end_mark = struct.pack('<I', 0xFD11EDED)  # 结束标记
		
		# 组装完整消息
		full_msg = header + length + cmd_type + cmd_id + var_len + var_data + end_mark
		
		# 发送UDP数据包
		self.sock.sendto(full_msg, (self.ip, self.port))
		print(f"已发送消息到 GBox ({self.ip}:{self.port}): {message}")
	
	def get_tools(self):
		"""从GBox获取可用的工具列表"""
		message = {
			"function": "get_tools",
			"params": {}
		}
		json_str = json.dumps(message)
		self.send_gbox_str(json_str)
		try:
			response = self.receive_response()
			# 检查返回的是否是有效的工具列表格式（直接返回工具字典）
			if isinstance(response, dict):
				# 检查每个工具的格式是否正确
				for tool_name, tool_info in response.items():
					if not isinstance(tool_info, dict) or "name" not in tool_info or "description" not in tool_info:
						print(f"警告：工具 {tool_name} 的定义格式不正确")
						return {}
				return response
			print(f"警告：GBox返回的不是有效的工具列表: {response}")
			return {}
		except Exception as e:
			print(f"获取工具列表失败: {e}")
			return {}
	
	def parse_gbox_string(self, data):
		"""解析 GBox 的 AutoVar 字符串格式"""
		try:
			# 1. 检查魔数
			if len(data) < 16:  # 基本头部长度
				return None
				
			magic = struct.unpack('<I', data[0:4])[0]
			if magic != 0xBE33EE38:
				return None
				
			total_len = struct.unpack('<I', data[4:8])[0]
			cmd_type = struct.unpack('<I', data[8:12])[0]
			cmd_id = struct.unpack('<I', data[12:16])[0]
			
			print(f"解析头部: magic=0x{magic:08X}, total_len={total_len}, cmd_type={cmd_type}, cmd_id={cmd_id}")
			
			# 2. 解析 AutoVar 数据
			if len(data) < 20:  # 至少要包含变量长度
				return None
				
			var_len = struct.unpack('<I', data[16:20])[0]
			print(f"变量数据长度: {var_len}")
			
			if var_len == 0:
				return ""
				
			# 3. 解析字符串数据
			var_data = data[20:20+var_len]  # 只取变量数据部分，不包括结束标记
			if len(var_data) < 1:
				return None
				
			var_type = var_data[0]  # 第一个字节是类型
			print(f"变量类型: 0x{var_type:02X}")
			print(f"原始字节: {' '.join([f'0x{b:02X}' for b in var_data])}")
			
			if var_type == 0xB0:  # EXTSAVE_STR_NULL
				return ""
			elif var_type == 0xB1:  # EXTSAVE_STR_BYTE
				str_len = var_data[1]
				print(f"字符串长度: {str_len}")
				content = var_data[2:2+str_len]
				print(f"字符串内容字节: {' '.join([f'0x{b:02X}' for b in content])}")
				try:
					# 尝试直接解码ASCII字符
					result = ''.join(chr(b) for b in content if 32 <= b <= 126)
					print(f"ASCII解码结果: {result}")
					return result
				except Exception as e:
					print(f"ASCII解码失败: {e}")
					return None
			elif var_type == 0xB2:  # EXTSAVE_STR_WORD
				str_len = struct.unpack('<H', var_data[1:3])[0]
				content = var_data[3:3+str_len]
				try:
					result = ''.join(chr(b) for b in content if 32 <= b <= 126)
					return result
				except:
					return None
			elif var_type == 0xB3:  # EXTSAVE_STR_LONG
				str_len = struct.unpack('<I', var_data[1:5])[0]
				content = var_data[5:5+str_len]
				try:
					result = ''.join(chr(b) for b in content if 32 <= b <= 126)
					return result
				except:
					return None
				
			return None
		except Exception as e:
			print(f"解析 GBox 字符串时出错: {e}")
			return None
			
	def receive_response(self, timeout=5) -> dict:
		"""接收GBox的响应
		Args:
			timeout: 超时时间（秒）
		Returns:
			dict: 解析后的响应数据
		"""
		print(f"等待 GBox 响应，超时时间 {timeout} 秒...")
		self.sock.settimeout(timeout)
		
		try:
			print("等待接收数据...")
			data, addr = self.sock.recvfrom(4096)
			print(f"收到来自 {addr} 的响应，长度: {len(data)} 字节")
			
			# 解析 GBox 字符串格式
			content = self.parse_gbox_string(data)
			if content is None:
				raise ValueError("无法解析 GBox 字符串格式")
				
			print(f"解析出的内容: {content}")
			
			# 尝试解析为 JSON，如果不是 JSON 则直接返回文本
			try:
				response = json.loads(content)
				print(f"JSON解析结果: {response}")
				return response
			except json.JSONDecodeError:
				print("不是JSON格式，直接返回文本内容")
				return {"message": content}
			
		except socket.timeout:
			print("等待响应超时")
			raise TimeoutError("等待响应超时")
		except Exception as e:
			print(f"接收响应时发生错误: {e}")
			raise

def register_gbox_tools(mcp_server, gbox_comm):
	"""注册 GBox 提供的所有工具到 MCP 服务器
	
	Args:
		mcp_server: FastMCP 服务器实例
		gbox_comm: GBox 通信器实例
	"""
	# 从GBox获取工具列表
	tools = gbox_comm.get_tools()
	if not tools or not isinstance(tools, dict):
		print("警告：无法从GBox获取有效的工具列表，将使用默认工具列表")
		tools = GBOX_TOOLS
	
	def create_tool_wrapper(tool_name, tool_info):
		"""创建工具包装函数"""
		def wrapper(**kwargs):
			# 构造发送给 GBox 的消息
			message = {
				"function": tool_name,
				"params": kwargs
			}
			
			try:
				print(f"\n开始调用工具 {tool_name}...")
				# 发送消息到 GBox
				json_str = json.dumps(message)
				gbox_comm.send_gbox_str(json_str)
				
				# 接收 GBox 的响应
				response = gbox_comm.receive_response()
				return response
					
			except TimeoutError:
				return {"error": "请求超时", "message": "GBox 响应超时"}
			except Exception as e:
				return {"error": "请求出错", "message": str(e)}
		
		return wrapper

	# 注册所有工具
	for tool_name, tool_info in tools.items():
		if not isinstance(tool_info, dict) or "name" not in tool_info or "description" not in tool_info:
			print(f"警告：工具 {tool_name} 的定义格式不正确，跳过注册")
			continue
			
		wrapper = create_tool_wrapper(tool_name, tool_info)
		mcp_server.tool(name=tool_info["name"], description=tool_info["description"])(wrapper)

	print(f"已注册 {len(tools)} 个 GBox 工具")

def main():
	"""主函数，处理命令行参数并运行服务器"""
	mcp = FastMCP("GBox MCP")
	gbox = GBoxCommunicator()
	
	# 注册工具
	register_gbox_tools(mcp, gbox)
	
	if len(sys.argv) > 1 and sys.argv[1] == "test":
		# 测试模式
		city = "Beijing"
		if len(sys.argv) > 2:
			city = sys.argv[2]
		print(f"测试获取天气信息: {city}")
		message = {
			"function": "get_weather",
			"params": {"city": city}
		}
		json_str = json.dumps(message)
		gbox.send_gbox_str(json_str)
		result = gbox.receive_response()
		print(f"结果: {result}")
	else:
		# MCP 服务器模式
		mcp.run(transport='stdio')

if __name__ == "__main__":
	main() 