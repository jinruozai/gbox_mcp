import time
from gboxtcp import GBoxTCP

class TestGBoxTCP(GBoxTCP):
    def _on_message_received(self, message: str):
        """重写消息处理方法，只输出收到的消息"""
        print(f"[RECV] {repr(message)}")

def main():
    client = TestGBoxTCP('10.211.55.4', 30080)
    
    try:
        if not client.connect():
            return

        client.call("","get_tools")

        # 等待接收消息
        time.sleep(20)

    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    main()