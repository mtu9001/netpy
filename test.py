import requests
from getpass import getpass

headers = {"content-type": "application/json"}

# Variables
pAuth = "/api/v1/auth/"
pUserRoles = "/api/v1/configuration/users/user-roles/"

host = input("Hostname : ")
uname = input("Username : ")
passwd = getpass("Password : ")

# Connect with username/password to retreive api_key
r = requests.get(
    "https://" + host + pAuth, verify=False, auth=(uname, passwd), headers=headers
)

# Show feedback
print("*" * 80)
auth_title = "Auth Information"
print(f"{auth_title:^80}")
print(f"Headers:          {headers}")
print(f"Path to Auth:     {pAuth}")
print(f"Host:             {host}")
print(f"Username:         {uname}")
print(f"Password:         {passwd}")
print()
print(f"Status Code:      {r.status_code}")
print(f"JSON Information: {r.json()}")
d = r.json()
print(f"JSON Key:         {d['api_key']}")
api_key = d["api_key"]
print("*" * 80)

# Connect with api_key and pull configuration information
try:
    config_request = requests.get(
        "https://10.100.100.251/api/v1/configuration", verify=False, auth=(api_key, "")
    )
except requests.exceptions.ConnectionError:
    r.status_code = "Connection Refused"

# Show feedback
print("*" * 80)
config_title = "Configuration Information"
print(f"{config_title:^80}")
print()
data = config_request.json()
print(data)
for key in data:
    print(f"{key} equal to {data[key]}")
    data1 = data[key]
    for element in data1:
        print(f"{element} equal to {data1[element]}")
print("*" * 80)
