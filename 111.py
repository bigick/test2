import msal
import requests

# 配置：从 Azure 注册应用中获取
CLIENT_ID = "your-client-id"
TENANT_ID = "your-tenant-id"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["User.Read"]
USERNAME = "your-username@example.com"
PASSWORD = "your-password"  # 不推荐硬编码，仅用于测试或展示用例

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# 获取 token
result = app.acquire_token_by_username_password(USERNAME, PASSWORD, scopes=SCOPE)

if "access_token" in result:
    headers = {"Authorization": f"Bearer {result['access_token']}"}
    response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
    print(response.json())
else:
    print("获取 Token 失败："， result.get("error_description"))
