__author__ = 'yuriy'

import os, util, config

def cleanUp(d):
    cleanUpPreviousRun(d)
    cleanUpTomcat(d)


def cleanUpTomcat(d):
    tomcatConf = os.path.join(d['tomcatHome'], "conf")
    tomcatBin = os.path.join(d['tomcatHome'], "bin")
    tomcatWebapps = os.path.join(d['tomcatHome'], "webapps")

    tomcatConf = os.path.normpath(tomcatConf)
    tomcatBin = os.path.normpath(tomcatBin)
    tomcatWebapps = os.path.normpath(tomcatWebapps)

    if d['platform'] == "windows":
        actions = [
            '%s\\shutdown.bat' % (tomcatBin), # shutdown tomcat
            'del /f /q %s\\ox*' % (tomcatConf), # remove OX configs
            'del /f /q %s\\ox*' % (tomcatWebapps), # remove wars
            'rmdir /s /q %s\\oxauth' % (tomcatWebapps), # remove dirs
            'rmdir /s /q %s\\oxTrust' % (tomcatWebapps) # remove dirs
        ]
    else:
        actions = [
            '%s/shutdown.sh' % (tomcatBin), # shutdown tomcat
            'rm -f %s/ox*' % (tomcatConf), # remove OX configs
            'rm -f %s/ox*' % (tomcatWebapps) # remove OX configs
        ]
    util.call(actions)


def cleanUpPreviousRun(d):
    if d['platform'] == "windows":
        actions = [
            'del /f /q %s' % d['dataGeneratedFile'], # remove dataGeneratedFile.ldif
            'del /f /q %s' % d['schemaFN'], # remove schemaFN.ldif

        ]
    else:
        actions = [
            'rm -f %s' % d['dataGeneratedFile'], # remove dataGeneratedFile.ldif
            'rm -f %s' % d['schemaFN'], # remove schemaFN.ldif
        ]
    util.call(actions)

cleanUp(config.getConfigDir())
