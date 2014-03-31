__author__ = 'yuriy'

import util, os

def configureDirectoryServer(config):
    dsType = config['dsType']
    if dsType == 'opendj' or dsType == 'opends':
        configureOpenDJ(config)
    else:
        print 'Currently only opendj and opends is supported. Exit from DS configuration.'



def configureOpenDJ(d):
    cwd = os.getcwd()
    print 'Configure openDJ (openDS), working directory: %s' % cwd
    tup = (d['dsHome'], d['ldapHost'], d['ldapDN'], d['ldapPW'], d['ldapPort'], cwd, d['dataGeneratedFile'])

    if d['platform'] == "windows":
        actions = ['%s\\bat\\stop-ds.bat' % d['dsHome'],
			   'copy %s\\%s %s\\config\\schema' % (cwd, d['schemaFN'], d['dsHome']),
                           'copy %s\\%s %s\\config\\schema' % (cwd, d['userSchemaFN'], d['dsHome']),
			   '%s\\bat\\start-ds.bat' % d['dsHome'],
		       '%s\\bat\\dsconfig.bat set-global-configuration-prop -h %s -p 4444 --trustAll --no-prompt -D "%s" -w %s --set single-structural-objectclass-behavior:accept' % tup[:-3],
			   '%s\\bat\\dsconfig.bat -h %s -p 4444 --trustAll --no-prompt -D "%s" -w %s set-password-policy-prop --policy-name "Default Password Policy" --set allow-pre-encoded-passwords:true' % tup[:-3],
               '%s\\bat\\dsconfig.bat set-backend-prop --backend-name userRoot --add base-dn:%s -h %s -p 4444 -D "%s" -w %s --trustAll --noPropertiesFile --no-prompt' %
                           (d['dsHome'], d['suffix'], d['ldapHost'], d['ldapDN'], d['ldapPW']),
			   '%s\\bat\\ldapmodify.bat -h %s -D "%s" -w %s -a -p %s -f %s\\%s' % tup]

    else:
        actions = ['%s/bin/stop-ds' % d['dsHome'],
			   'cp %s/%s %s/config/schema' % (cwd, d['schemaFN'], d['dsHome']),
			   'cp %s/%s %s/config/schema' % (cwd, d['userSchemaFN'], d['dsHome']),
			   '%s/bin/start-ds' % d['dsHome'],
			   '%s/bin/dsconfig set-global-configuration-prop -h %s -p 4444 --trustAll --no-prompt -D "%s" -w %s --set single-structural-objectclass-behavior:accept' % tup[:-3],
			   '%s/bin/dsconfig -h %s -p 4444 --trustAll --no-prompt -D "%s" -w %s set-password-policy-prop --policy-name "Default Password Policy" --set allow-pre-encoded-passwords:true' % tup[:-3],
               '%s/bin/dsconfig set-backend-prop --backend-name userRoot --add base-dn:%s -h %s -p 4444 -D "%s" -w %s --trustAll --noPropertiesFile --no-prompt' %
                                          (d['dsHome'], d['suffix'], d['ldapHost'], d['ldapDN'], d['ldapPW']),
			   '%s/bin/ldapmodify -h %s -D "%s" -w %s -a -p %s -f %s/%s' % tup]
    util.call(actions)

