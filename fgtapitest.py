from fortiosapi import FortiOSAPI
from getpass import getpass
from pprint import pprint

fgt = FortiOSAPI()

# get information from user
host = input("Host IP: ")
username = input("Username: ")
passwd = getpass("Password: ")

device = {"host": host, "username": username, "password": passwd}

# verify=False due to self signed cert on internal interface
fgt.login(**device, verify=False)

out = fgt.monitor("system", "status")
pprint(out)
out = fgt.get("system", "global")
pprint(out)

fgt.logout()
