from getpass import getpass
from getInfo import getHostInfo, getLicense


# gather connection information
host = input('Hostname/IP: ')
user = input('Username: ')
passwd = getpass()

# connect to device and get RSI
# myRSI = getRSI(host, user, passwd)
myLicense = getLicense(host, user, passwd)
myInfo = getHostInfo(host, user, passwd)
