import socket
from netmiko import Netmiko
from getpass import getpass


def requestRSI(host, username, password, dev_type, local_ip):
    net_connect = Netmiko(
        host, username=username, password=password, device_type=dev_type
    )

    command = "show version"

    print("Logging in as " + username)
    print(net_connect.find_prompt())
    print()
    print("Sending command: " + command)
    print("*" * 80)
    print(net_connect.send_command(command))
    net_connect.disconnect()


if __name__ == "__main__":
    # gather connection information
    hostname = input("Hostname/IP: ")
    dev_type = input("Device Type (e.g. cisco_ios, juniper_junos, etc.: ")
    username = input("Username: ")
    password = getpass()
    local_ip = socket.gethostbyname(socket.gethostname())

    # start paramiko sftp server

    # request RSI
    requestRSI(hostname, username, password, dev_type, local_ip)
