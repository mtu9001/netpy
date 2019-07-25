from getpass import getpass
from getInfo import getHostInfo, getLicense, setRescueConfig


# gather connection information
host = input("Hostname/IP: ")
user = input("Username: ")
passwd = getpass()

# connect to device and get RSI
# get License information
# getLicense(host, user, passwd)

# get RSI information
# getRSI(host, user, passwd)

# get Host information
getHostInfo(host, user, passwd)
setRescueConfig(host, user, passwd)
