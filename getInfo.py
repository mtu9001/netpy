import os.path
from jnpr.junos import Device
from netmiko import Netmiko


def getRSI(host, user, passwd):
    # create dev object with connection information
    dev = Device(user=user, host=host, password=passwd)
    # open device connection
    dev.open()
    # set timeout for long commands
    dev.timeout = 60 * 60
    # need to abstract command
    output = dev.rpc.get_support_information()
    # close dev session because we're good people
    dev.close()
    # print output information
    print(output.text)
    # if statment, if file exists overwrite or create new?
    if os.path.exists("RSI.txt"):
        ans = input("Overwrite existing RSI.txt file? (y/n): ")
        if "y" in ans:
            os.remove("RSI.txt")
        else:
            output_filepath = "RSI.txt"
            output_information = open(output_filepath, "w")
            output_information.write(output.text)


def getLicense(host, user, passwd):
    net_connect = Netmiko(
        host, username=user, password=passwd, device_type="juniper_junos"
    )

    command = "show system license"

    print("Logging in as " + user)
    print("*" * 80)
    print(net_connect.find_prompt())
    print()

    print("*" * 80)
    print("Sending command: " + command)
    output = net_connect.send_command(command)
    print(output)
    print("*" * 80)
    print("Logging out and closing session . . .")
    net_connect.disconnect()
    print()


def getHostInfo(host, user, passwd):
    net_connect = Netmiko(
        host, username=user, password=passwd, device_type="juniper_junos"
    )

    commands = [
        "show version | no-more",
        "show system alarms | no-more",
        "show chassis alarms | no-more",
        "show interfaces terse | match inet | match up",
        "show route 0.0.0.0",
        "request system storage cleanup dry-run | no-more",
        "show system storage detail | no-more",
        "show system config rescue | no-more",
    ]

    print("Logging in as " + user)
    print("*" * 80)
    print(net_connect.find_prompt())
    print()

    for command in commands:
        print("*" * 80)
        print("Sending command: " + command)
        print(net_connect.send_command(command))

    print("*" * 80)
    print("Logging out and closing session . . .")
    net_connect.disconnect()
