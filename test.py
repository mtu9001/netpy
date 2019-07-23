import requests
from getpass import getpass


headers = {"content-type": "application/json"}

# Variables
pAuth = "/api/v1/auth/"
pUserRoles = "/api/v1/configuration/users/user-roles/"

# Tests
# input("Hostname : ")
url = "10.100.100.251"
# input("Username : ")
uname = "admin"
# getpass("Password : ")
passwd = "Juniper12345!!"

try:
    r = requests.get(
        "https://" + url + pAuth, verify=False, auth=(uname, passwd), headers=headers
    )
except requests.exceptions.ConnectionError:
    r.status_code = "Connection Refused"


print("*" * 80)
print(f"Auth Information")
print()
print("--- Status Code ---")
print(r.status_code)
print("--- text ---")
print(r.text)
print("--- Headers ---")
print(r.headers)
print("--- JSON response ---")
print(r.json())
d = r.json()
print("--- d ---")
api_key = d["api_key"]
print(api_key)
print(r.content)
print("*" * 80)

"""
try:
    config_request = requests.get('https://10.100.100.251/api/v1/configuration', verify=False, auth=(api_key, ''))
except requests.exceptions.ConnectionError:
    r.status_code = "Connection Refused"

print("*" * 80)
print("Config Information")
print()
print(config_request.content)
print()
data = config_request.json()
print(data)
for key in data:
    print(key)
    data1 = data[key]
    for element in data1:
        print(element)
print("*" * 80)
"""

