# GBox MCP Server

这是一个简单的 Model Context Protocol (MCP) 服务器实现，用于与 GBox 进行通信。

## 安装

1. 确保已安装 Python 3.7+
2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 运行

启动 MCP 服务器：
```bash
python gbox_mcp_server.py
```

## 功能

目前实现的工具：
- `get_game_name`: 获取当前游戏名称

## 配置

默认配置：
- GBox IP: 10.211.55.4
- GBox Port: 20000

如需修改配置，请在 `GBoxCommunicator` 类初始化时传入新的参数。 