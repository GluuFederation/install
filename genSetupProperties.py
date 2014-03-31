#!/usr/bin/python

fn = "template-setup.properties"

d  = {}

ldap_stuff = {
'dsHome':'/opt/opendj',
'ldapHost':'localhost',
'ldapPort':'1389',
'ldapDN':'cn=directory manager',
'ldapPW':'spam9876',
'suffix':'o=gluu',
'desc':'LDAP Info'
}

org_stuff = {
'orgName':'My Oranization Inc.',
'orgShortName':'myOrg',
'l':'Austin',
'desc':'Organization Info'
}

admin_stuff={
'givenName':'Admin',
'sn':'User',
'uid':'admin',
'mail':'admin@myOrg.com',
'password':'spam1234',
'desc':'Admin Info'
}

src_stuff={
'oxAuthHome':'/usr/local/src/oxAuth',
'oxTrustHome':'/usr/local/src/ox/oxTrust',
'tomcatHome':'/opt/tomcat',
'desc':'Source Info'
}


l = [ldap_stuff, org_stuff, admin_stuff, src_stuff]

print "\n"

for dict in l:
    print dict['desc']
    print "-----------------"
    del dict['desc']
    for item in dict:
        d[item] = raw_input("Enter %s [%s] : " % (item, dict[item]))
        if d[item].strip() == '': d[item] = dict[item]
    print 

f = open(fn)
s = f.read()
print s % d

