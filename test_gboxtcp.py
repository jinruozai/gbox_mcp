import time
from gboxtcp import GBoxTCP


def main():
    client = GBoxTCP('10.211.55.4', 30080)
    
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