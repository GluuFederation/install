__author__ = 'yuriy'

import sys
from getpass import getpass

IS_CONFIG_OK = "isConfigOk"

def getConfigDir(configFile="setup.properties"):

    argv = sys.argv
    if len(argv) == 2 and argv[1] == "-test":
        configFile = "setup-dev.properties"

#    print "Use configuration file:",
#    print configFile

    f = open(configFile, "r")
    try:
        answer = {}
        for line in f:
            strippedLine = line.strip()
            if not strippedLine.startswith("#") and not strippedLine == "":
                k, v = strippedLine.split('=', 1)
                answer[k.strip()] = v.strip()
        return answer
    finally:
        f.close()

#print getConfigDir("setup-dev.properties")

def getConfigInteractively():
    d = {}
    d['platform'] = raw_input("OS platform [windows|unix]: ").lower()
    d['dsHome'] = raw_input("Full path to Directory Server: ")
    d['ldapHost'] = raw_input("LDAP hostname: ")
    d['ldapPort'] = raw_input("LDAP port: ")
    d['ldapDN'] = raw_input("LDAP BIND DN: ")
    d['ldapPW'] = getpass("Password for cn=Directory Manager: ")
    d['dataTemplateFile'] = raw_input("Filename for init data: ")
    d['orgInum'] = raw_input("Organizational inumber: ")
    d['orgPass'] = getpass("Organizational password: ")
    d['orgInumNoDelimiters'] = d['orgInum'][2:]
    d['suffix'] = raw_input("LDAP root naming context (suffix): ")
    d['orgName'] = raw_input("Organization name: "),
    d['orgShortName'] = raw_input("Organization Short Name: ")
    d['l'] = raw_input("Organization city: ")
    d['givenName'] = raw_input("Admin given name: ")
    d['sn'] = raw_input("Admin last name: ")
    d['uid'] = raw_input("Admin username: ")
    d['mail'] = raw_input("Admin email: ")
    d['password'] = getpass("Admin password: ")
    d['personInum'] = "%s!0000" % d['orgInum']
    d['applianceInum'] = "%s!0002" % d['orgInum']
    d['groupInum'] = "%s!0003" % d['orgInum']
    d['attributeInum'] = "%s!0005" % d['orgInum']
    return d
