# **network python**

The following are example python scripts used by myself to collect, digest, and present network device data in a meaningful manner. Currently, I have examples for Juniper, FortiOS, and Pulse Secure devices and will add others as needed.

## Installation

No real installation process yet. Clone the repo, load the requirements, and you are set.

## Usage

Currently these are command line scripts and typically run from a terminal of some sort. I would like consolidate them and use an interface to streamline the usage, but that's for a different time.

## Juniper

---
Sample scripts to get information from Juniper devices and retrieve RSI for JTAC.

JTAC typically asks for RSI (request support information) in a zipped file either when on the phone, or when creating a support ticket.

The following scripts use a user provided username and password for basic ssh authentication. The device will require netconf running over ssh.

Please view the official [Juniper REST API guide](https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.html) for more information.

### [get_jnpr_info.py](https://www.github.com/)

This script collects host, username, password information and calls functions from getInfo.py.

```zsh

user$ python get_jnpr_info.py

Hostname/IP: 192.168.100.1
Username: netconfuser
Password:

Logging in as netconfuser
******************************
netconfuser@LAB-SRX-0>

******************************
Sending command: show system license

License usage:
                                 Licenses     Licenses    Licenses    Expiry
  Feature name                       used    installed      needed
  Virtual Appliance                     1            1           0    permanent
  remote-access-ipsec-vpn-client        0            2           0    permanent

Licenses installed:
  License identifier:
  License version: 4
  Software Serial Number:
  Customer ID:
  Features:
    Virtual Appliance - Virtual Appliance
      count-down, Original validity: 60 days

******************************
Logging out and closing session . . .

user$
```

### [getInfo.py](https://www.github.com/)

This includes the getRSI, getLicense, and getHostInfo functions called by get_jnpr_info.py.

getRSI uses py-junos-eznc to establish a connection to the device, calls the RPC get_support_information, and asks the user to save the file as RSI.txt locally.

getLicense uses netmiko to connect to the device, pass "show system license", and return the output.

getHostInfo uses netmiko to connect to the device and run a handful of commands to gather useful information about the device.

## Fortinet

---
Sample scripts to get information from FortiOS devices.

Please view the official [Fortinet REST API guide](https://www.github.com/) for more information.

### [get_fgt_info.py](https://www.github.com/)

```zsh
python get_fgt_info.py
```

## Pulse Secure

---
Sample scripts to get information from Pulse Secure PSA devices and setup recommended best practices.

Please view the official [Pulse Secure PCS/PPS REST API Solutions Guide](https://www-prev.pulsesecure.net/download/techpubs/current/1470/pulse-connect-secure/pcs/9.0rx/ps-pcs-pps-9.0r3-rest-api-solutions-guide.pdf) for more information.

### [get_psa_info.py](https://www.github.com/)

```zsh
python get_psa_info.py
```

### [psa_bp.py](https://www.github.com/)

```zsh
python psa_bp.py
```
