import requests
from getpass import getpass

headers = {"content-type": "application/json"}

# API paths
auth_path = "/api/v1/auth/"
config_path = "/api/v1/configuration"
admin_path = "/api/v1/configuration/administrators"
admin_auth_path = "/api/v1/configuration/authentication"
sys_config_path = "/api/v1/configuration/system"
user_config_path = "/api/v1/configuration/users"
local_user_path = "/api/v1/configuration/authentication/auth-servers/auth-server/Sys-Local/local/users/user/user0001"
active_user_path = "/api/v1/system/active-users"

host = input("Host IP: ")
uname = input("Username: ")
passwd = getpass("Password: ")

# get API key
auth_response = requests.get(
    "https://" + host + auth_path, verify=False, auth=(uname, passwd), headers=headers
)
auth_data = auth_response.json()
api_key = auth_data["api_key"]
# print(auth_data)
print(api_key)

"""
# get config information
config_response = requests.get(
    "https://" + host + config_path, verify=False, auth=(api_key, "")
)
config_data = config_response.json()
print(config_data)

# get admin information
admin_response = requests.get(
    "https://" + host + admin_path, verify=False, auth=(api_key, "")
)
admin_data = admin_response.json()
print(admin_data)

# get admin auth information
admin_auth_response = requests.get(
    "https://" + host + admin_auth_path, verify=False, auth=(api_key, "")
)
admin_auth_data = admin_auth_response.json()
print(admin_auth_data)

# get system configuration information
sys_config_response = requests.get(
    "https://" + host + sys_config_path, verify=False, auth=(api_key, "")
)
sys_config_data = sys_config_response.json()
print(sys_config_data)

# get user configuration information
user_config_response = requests.get(
    "https://" + host + user_config_path, verify=False, auth=(api_key, "")
)
user_config_data = user_config_response.json()
print(user_config_data)

# get local user information
local_user_response = requests.get(
    "https://" + host + local_user_path,
    verify=False,
    auth=(api_key, ""),
    headers=headers,
)
local_user_data = local_user_response.json()
print(local_user_data)
"""

# get active users
active_user_response = requests.get(
    "https://" + host + active_user_path,
    verify=False,
    auth=(api_key, ""),
    headers=headers,
)
active_user_data = active_user_response.json()
print(active_user_data)

