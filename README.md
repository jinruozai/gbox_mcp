# GBox MCP Server

GBox MCP (Machine Control Protocol) Server 是一个基于 FastMCP 的服务器实现，用于与 GBox 系统进行通信和控制。

## 功能特点

- 基于 FastMCP 协议实现
- 支持工具动态加载和管理
- 支持 TCP 通信
- 自动工具变更通知

## 系统要求

- Python 3.6+
- FastMCP
- GBoxTCP

## 安装

1. 克隆仓库：
```bash
# 从 Gitee 克隆
git clone https://gitee.com/lazygoo/gbox_mcp.git
# 或从 GitHub 克隆
git clone https://github.com/jinruozai/gbox_mcp.git
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

启动服务器：
```bash
python gbox_mcp_server.py [--ip IP地址] [--port 端口号]
```

### 参数说明

- `--ip`: 服务器IP地址（可选）
- `--port`: 服务器端口号（可选）

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。 