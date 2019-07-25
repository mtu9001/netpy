# Set Pulse Secure best practices on PSA devices
#
# User Session Security
# 1. Disable roaming session or limit to subnet for non-roaming user roles:
# 2. Disable persistent sessions
# 3. Remove Browser Session Cookie
# 4. Disable split tunneling
# 5. Session limits
# 6. Launch Pulse as stand alone
# 7. Use the IP lockout option to block brute force password attacks
# 8. ESP encryption strength should be set to 256bit
# 9. Ensure all web bookmarks are using https:// (when applicable)
# 10. Web ACL
# 11. Selective Rewriting
# 12. VPN Tunneling Access Control
# 13. Disable "Allowing saving logon information" and "Dynamic certificate trust" for Connections Setting under Pulse Secure Client
# 14. Enable Server certificate trust enforcement
# 15. Enable Traffic Enforcement for IPV4 and IPV6 (for L3 tunnel customers)
# 16. Enable HTTP Only Device Cookie under User Role
#
# Server Side Security
# 1. Logging
# 2. Configure NTP
# 3. Disable legacy SSL support
# 4. Disable clients with weak ciphers
# 5. Disable 3DES
# 6. Disable all TLS_RSA ciphers
# 7. Configure inbout SSL for "Accept 1.2 and later"
# 8. Enable PFS or configure ECDHE
#
# Device Management
# 1. Lock down administrative access to internal or management interfaces only
# 2. Disable roaming session or limit to a subnet for admin users
# 3. Add realm level restrictions for admin realms and roles to provide additional protection
# 4. Lock down serial console access with a password
# 5. Encrypt backed up configuration exports and store them securely.
# 6. Do not use "admin", "administrator" or other popular administrator login names or passwords.
# 7. Rename the default admin sign in URL from /admin to something non-standard
# 8. Use two-arm configuration whenever possible. (External and Internal port).
# 9. If the device is using a one-arm configuration (Internal port only) and SNMP is enabled, ensure UDP port 161 is blocked from external access.
#
# Authentication Security
# 1. Two factor authentication (2FA)
# 2. If possible use client certificate authentication with OCSP or a CRL on the server-side with secondary authentication for sign-in realms. (AD/LDAP authentication servers).
# 3. LDAP: LDAPS or Start TLS
# 4. AD: standard mode strongly recommended
# 5. If local authentication is utilized, use the following settings:
"""
    Minimum password length: 10
    Maximum password length: 128
    Password must have at least 1 digits
    Password must have at least 2 letters
    Password must have mix of UPPERCASE and lowercase letters
"""
#
# Endpoint Security
# 1. Host Checker
# 2. Software Updates
