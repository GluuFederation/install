import getpass, config, logging


# 0.
# 0.1 check whether java is installed (on 'java -version' we should get version output)
# 0.2 check whether maven is installed (on 'maven -version' we should get version output)

# 1. specify opendj server home path
# 2. validate whether it's ok -> if not redirect to 1.
# 3. specify not blank host, port, binddn and password
# 4. test ldap connection via opendj/bin batch files, if valid go on, otherwise -> 3.
# 5. specify path for oxAuth downloaded source files
# 6. validate whether inside we have pom.xml, if not then -> 5.
# 7. specify path oxTrust downloaded source files
# 8. validate whether inside we have pom.xml, if not then -> 7.

# 9. run actual setup.py

# 10. after setup run ldap import validate oxAuth and oxTrust configurations in ldap via opendj commands
# (this step is one of the most important since most of the problems people are facing is configuration absence or bad configuration location)

def collectConfigs(d):
    if (True): # todo - temp to not break existing automatic installation
        d[config.IS_CONFIG_OK] = True
        return d

    print "Welcome to OX Platform setup."
    d[config.IS_CONFIG_OK] = False

    opendjHome = notBlankInput("LDAP Server home directory: ")
    # todo validate whether path is valid opendj home path

    host = notBlankInput("LDAP Server host (IP or DNS name): ")
    port = notBlankInput("LDAP Server port: ")
    bindDn = notBlankInput("LDAP Server Bind DN (e.g. cn=Directory Manager): ")
    password = getpass.getpass('LDAP Server Bind DN password: ')

    print "Test ldap connection ...!"
    # todo
    return d

def notBlankInput(message):
    logging.info(message)
    while(True):
        value = raw_input(message)
        if not value and value != '':
            return value
        else:
            print "Blank value is not allowed"


