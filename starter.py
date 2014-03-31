__author__ = 'yuriy'

import os, util, config

def start(d):
    tomcatBin = os.path.join(d['tomcatHome'], "bin")

    tomcatHome = os.path.normpath(d['tomcatHome'])
    tomcatBin = os.path.normpath(tomcatBin)

    print "Set CATALINA_HOME=%s" % tomcatHome
    os.environ["CATALINA_HOME"] = tomcatHome

    tomcatJavaOpts = d['tomcatJavaOpts']
    print "Set JAVA_OPTS=%s" % tomcatJavaOpts
    os.environ["JAVA_OPTS"] = tomcatJavaOpts

    if d['platform'] == "windows":
        actions = [
            '%s\\startup.bat -Xmx1024m -XX:PermSize=256m -XX:MaxPermSize=512' % (tomcatBin) # starts tomcat
        ]
    else:
        actions = [
            '%s/startup.sh -Xmx1024m -XX:PermSize=256m -XX:MaxPermSize=512' % (tomcatBin) # starts tomcat
        ]

    util.call(actions)

#start(config.getConfigDir())