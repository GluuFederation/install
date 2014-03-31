__author__ = 'yuriy'

import subprocess, os, config

def buildOx(config):
    buildMvn(config['oxAuthHome'])
    buildMvn(config['oxTrustHome'])

def buildMvn(projectHome):
    """
    Build project that is under Maven build system:
    Command: mvn -s settings.xml -Dmaven.test.skip=true clean install
    """
    currentWorkingDir = os.getcwd()

    try:
        os.chdir(projectHome)

        #actions = ['mvn -s settings.xml clean install -Dmaven.test.skip=true -Dcfg=setup']
        actions = ['mvn clean install -Dmaven.test.skip=true -Dcfg=setup']

        for action in actions:
            print "\n%s\n" % action
            subprocess.call(action, shell=True)
    finally: #yuriy : its important to change working directory back
        os.chdir(currentWorkingDir)

#buildMvn('u:\\own\\project\\oxAuth')
#buildOx(config.getConfigDir())

