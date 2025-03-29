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
		# 尝试使用GBK编码，失败则使用UTF-8
		try:
			msg_bytes = message.encode('gbk')
			encoding = 'gbk'
		except UnicodeEncodeError:
			msg_bytes = message.encode('utf-8')
			encoding = 'utf-8'
		
		# 打包字符串数据
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
		
		# 打印调试信息
		print(f"发送消息 (编码: {encoding}):")
		print(f"  总长度: {len(full_msg)}")
		print(f"  字符串长度: {msg_len}")
		print(f"  类型标记: 0x{var_data[0]:02X}")
		print(f"  内容: {message}")
		
		# 发送UDP数据包
		self.sock.sendto(full_msg, (self.ip, self.port))
		
	def get_tools(self):
		"""从GBox获取可用的工具列表"""
		message = {
			"function": "get_tools",
			"params": {}
		}
		self.send_gbox_str(json.dumps(message))
		try:
			response = self.receive_response()
			
			# 如果收到的是字符串，说明解析成功但非JSON格式
			if isinstance(response, str):
				print(f"收到非JSON格式的工具列表，内容长度: {len(response)}")
				return GBOX_TOOLS  # 使用默认工具列表
			
			# 如果收到的是字典类型，检查是否是有效的工具列表
			if isinstance(response, dict):
				# 如果收到的是消息响应，而不是工具列表
				if "function" in response or "message" in response:
					print(f"获取工具列表失败，返回的不是工具列表格式: {response}")
					return GBOX_TOOLS
				
				# 检查每个工具的格式是否正确
				valid_tools = {}
				for tool_name, tool_info in response.items():
					if not isinstance(tool_info, dict):
						print(f"警告：工具 {tool_name} 不是字典格式")
						continue
					if "name" not in tool_info or "description" not in tool_info:
						print(f"警告：工具 {tool_name} 缺少必要字段")
						continue
					valid_tools[tool_name] = tool_info
				
				if not valid_tools:
					print("没有找到有效的工具定义")
					return GBOX_TOOLS
				
				return valid_tools
			
			print(f"警告：GBox返回的不是有效的工具列表格式: {type(response)}")
			return GBOX_TOOLS
		except Exception as e:
			print(f"获取工具列表失败: {e}")
			return GBOX_TOOLS
	
	def parse_gbox_string(self, data):
		"""解析 GBox 的 AutoVar 字符串格式"""
		try:
			# 1. 检查魔数
			if len(data) < 16:  # 基本头部长度
				return None
				
			magic = struct.unpack('<I', data[0:4])[0]
			if magic != 0xBE33EE38:
				return None
				
			# 解析头部
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
			var_data = data[20:20+var_len]  # 只取变量数据部分
			if len(var_data) < 1:
				return None
				
			var_type = var_data[0]  # 第一个字节是类型
			print(f"变量类型: 0x{var_type:02X}")
			
			# 4. 根据类型处理字符串
			content = None
			if var_type == 0xB0:  # EXTSAVE_STR_NULL
				return ""
			elif var_type == 0xB1:  # EXTSAVE_STR_BYTE
				if len(var_data) < 2:
					print("字符串数据不完整：缺少长度字节")
					return None
				str_len = var_data[1]
				# 检查是否有足够的数据
				if 2 + str_len > len(var_data):
					print(f"警告: 字符串长度与实际数据不匹配，报告长度{str_len}字节，实际只有{len(var_data)-2}字节")
					# 这里仍然尝试读取所有可用数据，避免截断
					content = var_data[2:]
				else:
					content = var_data[2:2+str_len]
			elif var_type == 0xB2:  # EXTSAVE_STR_WORD
				if len(var_data) < 3:
					print("字符串数据不完整：缺少长度字节")
					return None
				str_len = struct.unpack('<H', var_data[1:3])[0]
				# 检查是否有足够的数据
				if 3 + str_len > len(var_data):
					print(f"警告: 字符串长度与实际数据不匹配，报告长度{str_len}字节，实际只有{len(var_data)-3}字节")
					# 尝试读取所有可用数据
					content = var_data[3:]
				else:
					content = var_data[3:3+str_len]
			elif var_type == 0xB3:  # EXTSAVE_STR_LONG
				if len(var_data) < 5:
					print("字符串数据不完整：缺少长度字节")
					return None
				str_len = struct.unpack('<I', var_data[1:5])[0]
				# 检查是否有足够的数据
				if 5 + str_len > len(var_data):
					print(f"警告: 字符串长度与实际数据不匹配，报告长度{str_len}字节，实际只有{len(var_data)-5}字节")
					# 尝试读取所有可用数据
					content = var_data[5:]
				else:
					content = var_data[5:5+str_len]
			else:
				print(f"未知的变量类型: 0x{var_type:02X}")
				return None
				
			print(f"字符串长度: {str_len}，实际读取: {len(content)} 字节")
			
			if content is None:
				return None
				
			# 特殊处理: 打印字节序列以便调试
			print("字节内容前20字节:")
			hex_str = ' '.join([f'{b:02X}' for b in content[:min(20, len(content))]])
			print(hex_str)
			
			# GBox的编码方式很特殊，需要特殊处理：
			# - ASCII字符(小于0x80)直接一个字节表示
			# - 非ASCII字符(中文等)使用: 标记字节(0x80-0x96) + 连续的两字节Unicode字符
			result = ""
			i = 0
			while i < len(content):
				if content[i] < 0x80:  # ASCII字符
					result += chr(content[i])
					i += 1
				elif 0x80 <= content[i] <= 0x96:  # 非ASCII字符的标记字节
					char_count = content[i] - 0x80  # 标记字节后面的Unicode字符数量
					print(f"发现标记字节: 0x{content[i]:02X}, 表示{char_count}个Unicode字符")
					i += 1
					
					if i + char_count*2 > len(content):
						print(f"警告: Unicode字符数量超出数据范围，需要{char_count*2}字节，只剩{len(content)-i}字节")
						# 只读取可用的完整字符
						char_count = min(char_count, (len(content) - i) // 2)
						print(f"调整为读取{char_count}个Unicode字符")
					
					for j in range(char_count):
						if i + 1 < len(content):
							unicode_char = struct.unpack('<H', content[i:i+2])[0]
							result += chr(unicode_char)
							print(f"Unicode字符: 0x{unicode_char:04X} -> {chr(unicode_char)}")
							i += 2
						else:
							break
				else:  # 尝试作为GBK编码处理
					if i + 1 < len(content):
						try:
							char_bytes = bytes([content[i], content[i+1]])
							char = char_bytes.decode('gbk')
							result += char
							i += 2
						except:
							result += chr(content[i])
							i += 1
					else:
						result += chr(content[i])
						i += 1
			
			print(f"解析后字符串: {result}")
			return result
				
		except Exception as e:
			print(f"解析 GBox 字符串时出错: {e}")
			import traceback
			traceback.print_exc()
			return None

	def _process_content(self, content):
		"""处理内容的通用方法"""
		# 首先尝试直接解码
		try:
			result = content.decode('utf-8')
			if self._is_valid_json(result):
				print(f"UTF-8解码成功: {result}")
				return result
		except UnicodeDecodeError:
			pass
		
		# 尝试处理GBox特殊编码
		try:
			# 创建一个新的字节数组来存储处理后的数据
			processed = bytearray()
			i = 0
			while i < len(content):
				# 检查是否是GBox特殊字符标记（0x80-0x96）
				if i + 2 < len(content) and 0x80 <= content[i] <= 0x96:
					# 提取后两个字节
					char_bytes = bytes([content[i+1], content[i+2]])
					try:
						# 尝试用GB2312解码（因为这是GBox最可能使用的编码）
						char = char_bytes.decode('gb2312')
						processed.extend(char.encode('utf-8'))
						print(f"解码特殊字符: 标记=0x{content[i]:02X}, 字节={char_bytes.hex()}, 结果={char}")
					except:
						try:
							# 如果GB2312失败，尝试GBK
							char = char_bytes.decode('gbk')
							processed.extend(char.encode('utf-8'))
							print(f"GBK解码特殊字符: 标记=0x{content[i]:02X}, 字节={char_bytes.hex()}, 结果={char}")
						except:
							# 如果解码失败，记录错误并保留原始字节
							print(f"无法解码特殊字符: 标记=0x{content[i]:02X}, 字节={char_bytes.hex()}")
							processed.extend(content[i:i+3])
					i += 3
				else:
					# 普通ASCII字符
					if 32 <= content[i] <= 126:
						processed.append(content[i])
					i += 1
			
			# 尝试解码处理后的数据
			result = processed.decode('utf-8')
			print(f"GBox编码处理结果: {result}")
			
			# 验证JSON格式
			if self._is_valid_json(result):
				return result
				
			# 如果JSON不完整，尝试修复
			if result.count('{') > 0:
				# 找到第一个 { 和最后一个 }
				start = result.find('{')
				end = result.rfind('}')
				if start >= 0 and end > start:
					result = result[start:end+1]
					print(f"提取JSON部分: {result}")
					if self._is_valid_json(result):
						return result
					
		except Exception as e:
			print(f"GBox编码处理失败: {e}")
			# 打印详细的字节信息以便调试
			print("原始字节序列:")
			for i in range(0, len(content), 16):
				chunk = content[i:i+16]
				hex_str = ' '.join([f'0x{b:02X}' for b in chunk])
				ascii_str = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in chunk])
				print(f"{i:04X}: {hex_str:<48} {ascii_str}")
		
		return None

	def _is_valid_json(self, s):
		"""检查字符串是否是有效的JSON"""
		try:
			# 检查字符串是否以 { 开始
			s = s.strip()
			if not s.startswith('{'):
				return False
			# 尝试解析JSON
			parsed = json.loads(s)
			# 确保解析出的是一个字典
			if not isinstance(parsed, dict):
				return False
			return True
		except:
			return False
	
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
			# 增加接收缓冲区大小到5KB，与GBox原始代码保持一致
			data, addr = self.sock.recvfrom(5*1024)
			print(f"收到来自 {addr} 的响应，长度: {len(data)} 字节")
			
			# 解析 GBox 字符串格式
			content = self.parse_gbox_string(data)
			if content is None:
				raise ValueError("无法解析 GBox 字符串格式")
				
			print(f"解析出的内容: {content}")
			
			# 尝试解析为 JSON，如果不是 JSON 则直接返回原始内容
			try:
				response = json.loads(content)
				print(f"JSON解析结果: {response}")
				return response
			except json.JSONDecodeError:
				# 直接返回原始内容，不尝试修复
				print("不是标准JSON格式，直接返回原始内容")
				return content
			
		except socket.timeout:
			print("等待响应超时")
			raise TimeoutError("等待响应超时")
		except Exception as e:
			print(f"接收响应时发生错误: {e}")
			raise

	def fix_gbox_json(self, json_str):
		"""修复GBox返回的非标准JSON格式
		Args:
			json_str: GBox返回的JSON字符串
		Returns:
			str: 修复后的标准JSON字符串
		"""
		# GBox返回的JSON格式特点：
		# 1. 键名不用引号包裹，如 {key : value} 而不是 {"key" : value}
		# 2. 值之间使用空格分隔，而不是逗号，如 {key1 : value1 key2 : value2}
		
		# 第一步：将所有没有引号的键添加引号
		result = ""
		in_string = False
		i = 0
		
		while i < len(json_str):
			if json_str[i] == '"':
				# 切换字符串状态
				in_string = not in_string
				result += json_str[i]
			elif json_str[i] == ':' and not in_string:
				# 找到前面的键名
				j = i - 1
				while j >= 0 and json_str[j].isspace():
					j -= 1
				
				if j >= 0 and json_str[j] != '"':
					# 键名不是以引号结束的，寻找键名开始位置
					key_end = j + 1
					while j >= 0 and (json_str[j].isalnum() or json_str[j] == '_'):
						j -= 1
					key_start = j + 1
					
					# 替换键名为带引号的格式
					key = json_str[key_start:key_end]
					result = result[:-(key_end-key_start)] + '"' + key + '"'
				
				result += json_str[i]
			else:
				result += json_str[i]
			
			i += 1
		
		# 第二步：将空格分隔符替换为逗号
		json_str = result
		result = ""
		in_string = False
		i = 0
		
		while i < len(json_str):
			if json_str[i] == '"':
				# 切换字符串状态
				in_string = not in_string
				result += json_str[i]
			elif json_str[i] == '}' and not in_string:
				# 检查是否需要在}前添加逗号
				result = result.rstrip()
				if result.endswith(','):
					result = result[:-1]
				result += json_str[i]
			elif not in_string and i + 1 < len(json_str):
				current_char = json_str[i]
				next_char = json_str[i+1]
				
				# 找到键值对之间的间隔
				if (current_char in ['"', '}', ']', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', 'E', 'l', 'L', 'f', 'F', 't', 'T', 'r', 'R', 'u', 'U', 'n', 'N', 'a', 'A', 's', 'S']) and \
				   next_char.isspace() and i + 2 < len(json_str):
					   
					# 跳过空白
					j = i + 1
					while j < len(json_str) and json_str[j].isspace():
						j += 1
					
					# 如果下一个非空白字符是键名（字母、数字或引号），则添加逗号
					if j < len(json_str) and (json_str[j].isalnum() or json_str[j] == '"'):
						result += current_char + ','
					else:
						result += current_char
					
					i += 1
				else:
					result += current_char
			else:
				result += json_str[i]
			
			i += 1
		
		return result

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
		gbox.send_gbox_str(json.dumps(message))
		result = gbox.receive_response()
		print(f"结果: {result}")
	else:
		# MCP 服务器模式
		mcp.run(transport='stdio')

if __name__ == "__main__":
	main() 