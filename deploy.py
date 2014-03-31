__author__ = 'yuriy'

import os, util, config

def deployOx(d):
    deployOxAuth(d)
    deployOxTrust(d)


def deployOxAuth(d):
    oxAuthTarget = os.path.join(d['oxAuthHome'], "Server", "target")
    oxAuthConf = os.path.join(oxAuthTarget, "conf")
    tomcatConf = os.path.join(d['tomcatHome'], "conf")
    tomcatWebapps = os.path.join(d['tomcatHome'], "webapps")

    oxAuthTarget = os.path.normpath(oxAuthTarget)
    oxAuthConf = os.path.normpath(oxAuthConf)
    tomcatConf = os.path.normpath(tomcatConf)

    if d['platform'] == "windows":
        actions = [
            'copy %s\\*.* %s' % (oxAuthConf, tomcatConf), # copy configs
            'copy %s\\oxauth.war %s' % (oxAuthTarget, tomcatWebapps), # copy war
        ]
    else:
        actions = [
            'cp %s/*.* %s' % (oxAuthConf, tomcatConf), # copy configs
            'cp %s/oxauth.war %s' % (oxAuthTarget, tomcatWebapps), # copy war
        ]

    util.call(actions)


def deployOxTrust(d):
    oxTrustTarget = os.path.join(d['oxTrustHome'], "target")
    oxTrustConf = os.path.join(oxTrustTarget, "conf")
    tomcatConf = os.path.join(d['tomcatHome'], "conf")
    tomcatWebapps = os.path.join(d['tomcatHome'], "webapps")

    oxTrustTarget = os.path.normpath(oxTrustTarget)
    oxTrustConf = os.path.normpath(oxTrustConf)
    tomcatConf = os.path.normpath(tomcatConf)

    if d['platform'] == "windows":
        actions = [
            'copy %s\\*.* %s' % (oxTrustConf, tomcatConf), # copy configs
            'copy %s\\oxtrust.war %s' % (oxTrustTarget, tomcatWebapps), # copy war
        ]
    else:
        actions = [
            'cp %s/oxTrust*.* %s' % (oxTrustConf, tomcatConf), # copy configs
            'cp %s/oxTrust.war %s' % (oxTrustTarget, tomcatWebapps), # copy war
        ]

    util.call(actions)

#deployOx(config.getConfigDir())
