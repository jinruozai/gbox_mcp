@echo off
echo GBox通信测试工具
echo ================
echo.

if "%1"=="" (
    echo 正在运行默认测试 (北京天气)...
    python gbox_mcp_server.py test
) else (
    echo 正在查询 %1 的天气...
    python gbox_mcp_server.py test %1
)

echo.
echo 测试完成!
pause 