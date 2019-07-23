from getpass import getpass
from netmiko import ConnectHandler

host = input("Hostname/IP: ")
user = input("Username: ")
passwd = getpass()

devices = []

ips = ["10.0.100.249"]
for ip in ips:
    fortinet = {
        "device_type": "fortinet",
        "ip": host,
        "username": user,
        "password": passwd,
    }

    devices.append(fortinet)

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.send_command("show system global"))
    print()
    print(net_connect.send_command("show system admin"))
