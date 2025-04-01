import json
import struct
import socket

class GBoxUDP:
    def __init__(self, ip='127.0.0.1', port=30080):
        """初始化GBoxUDP实例
        
        Args:
            ip (str): GBox服务器IP地址
            port (int): GBox服务器端口
        """
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', 0))
        self.sock.settimeout(5)
        print(f"GBoxUDP初始化成功: {ip}:{port}")
        
    def call(self, obj, function_name, params=None):
        """调用GBox函数并返回结果
        
        Args:
            obj: 对象引用
            function_name: 函数名
            params: 可选的参数字典
        """
        if params is None:
            params = {}
            
        message = {
            "obj": obj,
            "name": function_name,
            "arguments": params
        }
        
        try:
            # 发送请求并接收响应
            self._send_str(json.dumps(message))
            response = self._receive()
            print("response:", response)
            # 尝试解析为JSON
            try:
                response = json.loads(response)
                if isinstance(response, dict) and 'result' in response:
                    return response['result']
                return response
            except json.JSONDecodeError:
                return {"raw_response": response}
                
        except TimeoutError:
            return {"error": "timeout", "message": "GBox响应超时"}
        except Exception as e:
            return {"error": "exception", "message": str(e)}
    
    def _send_str(self, message):
        """发送字符串到GBox设备"""
        try:
            msg_bytes = message.encode('gbk')
        except UnicodeEncodeError:
            msg_bytes = message.encode('utf-8')
        
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
        
        # 组装并发送完整消息
        full_msg = header + length + cmd_type + cmd_id + var_len + var_data + end_mark
        self.sock.sendto(full_msg, (self.ip, self.port))
        
    def _receive(self, timeout=5):
        """接收GBox的响应"""
        self.sock.settimeout(timeout)
        
        try:
            # 接收数据并解析
            data, addr = self.sock.recvfrom(5*1024)
            content = self._parse_string(data)
            if content is None:
                raise ValueError("无法解析GBox字符串格式")
            
            return content
            
        except socket.timeout:
            raise TimeoutError("等待响应超时")
        except Exception as e:
            raise
            
    def _parse_string(self, data):
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
            
            # 2. 解析 AutoVar 数据
            if len(data) < 20:  # 至少要包含变量长度
                return None
                
            var_len = struct.unpack('<I', data[16:20])[0]
            
            if var_len == 0:
                return ""
                
            # 3. 解析字符串数据
            var_data = data[20:20+var_len]  # 只取变量数据部分
            
            if len(var_data) < 1:
                return None
                
            var_type = var_data[0]  # 第一个字节是类型
            
            # 4. 根据类型处理字符串
            content = None
            if var_type == 0xB0:  # EXTSAVE_STR_NULL
                return ""
            elif var_type == 0xB1:  # EXTSAVE_STR_BYTE
                if len(var_data) < 2:
                    return None
                str_len = var_data[1]
                content = var_data[2:]
            elif var_type == 0xB2:  # EXTSAVE_STR_WORD
                if len(var_data) < 3:
                    return None
                str_len = struct.unpack('<H', var_data[1:3])[0]
                content = var_data[3:]
            elif var_type == 0xB3:  # EXTSAVE_STR_LONG
                if len(var_data) < 5:
                    return None
                str_len = struct.unpack('<I', var_data[1:5])[0]
                content = var_data[5:]
            else:
                return None
            
            if content is None:
                return None
                
            # 解析GBox特殊编码
            result = ""
            i = 0
            
            while i < len(content):
                if content[i] < 0x80:  # ASCII字符
                    result += chr(content[i])
                    i += 1
                    continue
                
                # 处理标记字节(0x80+N)
                if content[i] >= 0x80:
                    unicode_count = content[i] - 0x80  # 获取后续Unicode字符数量
                    i += 1
                    
                    # 确保有足够的字节可读
                    if i + unicode_count * 2 > len(content):
                        print(f"Warning: 标记字节指示{unicode_count}个Unicode字符,但剩余字节不足")
                        break
                    
                    # 读取指定数量的Unicode字符
                    for _ in range(unicode_count):
                        if i + 1 >= len(content):
                            break
                        unicode_char = struct.unpack('<H', content[i:i+2])[0]
                        result += chr(unicode_char)
                        i += 2
                    continue
                
                # 如果到这里,说明遇到了未知的字节
                print(f"Warning: 遇到未知字节: 0x{content[i]:02x}")
                i += 1
            
            return result
                
        except Exception:
            return None 