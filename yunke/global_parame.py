# 管理端配置
admin_host = "192.168.3.11"
admin_port = "7798"
admin_ip = f"http://{admin_host}:{admin_port}"
login_url = f"http://{admin_host}:{admin_port}/seraph-admin/admin-api/login"
login_data = {
    "username": "test",
    "password": "$2a$12$ad9950826af929239fef1uQR4AP0ch9mpW/3AASoEra3o2z7SCEwq"
}
token = ""
open_api_token = "63cfd17e-2e02-4785-a617-09ba2ed82a89"
login_header = {"Content-Type": "application/json"}
app_id = 1
# 代理端IP地址
proxy_host = "192.168.2.11"
proxy_port = "8000"
proxy_ip = f"http://{proxy_host}:{proxy_port}"
