__author__ = 'yuriy'

import schema, config, random

d = config.getConfigDir()

# These will be used to print sample attr metadata
sampleMetaDataObjectclasses = {'gluuPerson': schema.gluuPerson,
                               'inetOrgPerson': schema.inetOrgPerson,
                               'eduPerson': schema.eduPerson}

# read this "key" extends "value"
ocExtensions = {'inetOrgPerson': 'gluuPerson'}

maceNamespace = ['eduCourseMember', 'eduPersonEntitlement', 'eduPersonAffiliation', 'eduPersonNickname',
                 'eduPersonOrgDN', 'eduPersonOrgUnitDN', 'eduPersonPrimaryAffiliation', 'eduPersonPrimaryOrgUnitDN',
                 'eduPersonPrincipalName', 'eduPersonScopedAffiliation', 'eduPersonTargetedID', 'labeledURI',
                 'carLicense', 'departmentNumber', 'displayName', 'employeeNumber', 'employeeType', 'preferredLanguage',
                 'cn', 'sn', 'telephoneNumber', 'seeAlso', 'description', 'title', 'registeredAddress',
                 'facsimileTelephoneNumber', 'street', 'postOfficeBox', 'postalCode', 'postalAddress',
                 'physicalDeliveryOfficeName', 'ou', 'o', 'st', 'l', 'givenName', 'businessCategory', 'initials',
                 'homePostalAddress', 'roomNumber', 'mail', 'manager', 'uid', 'homePhone', 'mobile', 'pager']

# yuriyz : be careful if you want to change scopes inum, this inum is used by oxTrust Demo client
# it seems that it's possible to generate also client LDIF but unfortunately client id and secret is
# "hardcoded" in oxTrust properties, we don't want to generate oxTrust properties right now (maybe it will be changed in future)
scopes = {
    'openid': {
        'inum': '@!1111!0009!E4B4',
        'description': 'Obtain an ID Token associated with the authentication session.',
        'claims': ['uid']
    },
    'address': {
        'inum': '@!1111!0009!F2D2',
        'description': 'View your address',
        'claims': ['homePostalAddress', 'postalAddress', 'street', 'st', 'postOfficeBox', 'postalCode', 'mail']
    },
    'profile': {
        'inum': '@!1111!0009!D2D2',
        'description': 'View basic information about your account',
        'claims': ['displayName', 'givenName', 'sn', 'preferredLanguage', 'timezone', 'photo1']
    },
    'email': {
        'inum': '@!1111!0009!A4C4',
        'description': 'View your email address',
        'claims': ['mail']
    },
    'http://docs.kantarainitiative.org/uma/scopes/prot.json': {
        'inum': '@!1111!0009!6D96',
        'description': 'UMA Protection scope',
        'claims': []
    },
    'http://docs.kantarainitiative.org/uma/scopes/authz.json': {
        'inum': '@!1111!0009!6D97',
        'description': 'UMA Authorization scope',
        'claims': ['mail']
    },
}

# yuriyz : store attribute inums in map, we need them for scope generation
attributeIdMap =  {}

def getInumberQuad():
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
    return "%s%s%s%s" % (
    l[random.randint(0, 15)], l[random.randint(0, 15)], l[random.randint(0, 15)], l[random.randint(0, 15)])


def getAttributeLDIF():
    r = []
    template = """
dn: inum=%s,ou=attributes,o=%s,%s
objectClass: gluuAttribute
objectClass: top
description: %s
displayName: %s
inum: %s
gluuAttributeOrigin: %s
gluuAttributeName: %s
gluuAttributePrivacyLevel: level3
gluuAttributeType: %s
gluuStatus: active
urn: %s"""
#    attrRejectList = []
    objectclasses = sampleMetaDataObjectclasses.keys()
    objectclasses.sort()
    usedInum = []
    for ocName in objectclasses:
        ocDict = sampleMetaDataObjectclasses[ocName]
        attrs = ocDict.keys()
        attrs.sort()
        for attr in attrs:
            # We don't want to duplicate attrs where the parent already has defined it.
            # If this entry has a parent, don't print the attribute
            if ocExtensions.has_key(ocName):
                parent = sampleMetaDataObjectclasses[ocExtensions[ocName]]
                if parent.has_key(attr): continue

            # If the attr is not visiable or editable by anyone, don't print it
            if ocDict[attr]['level'] == 6: continue

            # Prepare Attr for printing
            editTypeList = ocDict[attr]['editType']
            viewTypeList = ocDict[attr]['viewType']
            inumQuad = None
            while ((inumQuad == None) | (inumQuad in usedInum)):
                inumQuad = getInumberQuad()
            usedInum.append(inumQuad)
            inum = "%s!%s" % (d['attributeInum'], inumQuad)
            attrType = "string"
            attrDisplay = attr
            attrDesc = attr
            customAttrDict = schema.customAttrDict
            stdAttrDict = schema.stdAttrDict
            if customAttrDict.has_key(attr):
                attrType = customAttrDict[attr]['type']
                if customAttrDict[attr]['display'] != '': attrDisplay = customAttrDict[attr]['display']
                if customAttrDict[attr]['desc'] != '': attrDesc = customAttrDict[attr]['desc']
            elif stdAttrDict.has_key(attr):
                attrType = stdAttrDict[attr]['type']
                if stdAttrDict[attr]['display'] != '': attrDisplay = stdAttrDict[attr]['display']
                if stdAttrDict[attr]['desc'] != '': attrDesc = stdAttrDict[attr]['desc']
                # Figure out the URN
            urn = "urn:gluu:dir:attribute-def:%s" % attr
            if attr in maceNamespace:
                urn = "urn:mace:dir:attribute-def:%s" % attr

            attributeIdMap[attr] = inum
            r.append(
                template % (inum, d['orgInum'], d['suffix'], attrDesc, attrDisplay, inum, ocName, attr, attrType, urn))

            for user in editTypeList:
                r.append("gluuAttributeEditType: %s" % user)
            for user in viewTypeList:
                r.append("gluuAttributeViewType: %s" % user)

    result = '\n'.join(r)
    print "===== getAttributeLDIF() generates: " + result
    return result

def getScopeLDIF():
    r = []
    template = """

dn: inum=%(inum)s,ou=scopes,o=%(orgInum)s,%(suffix)s
defaultScope: true
description: %(description)s
displayName: %(displayName)s
inum: %(inum)s
objectClass: oxAuthCustomScope
objectClass: top"""

    claimsTemplate = """oxAuthClaim: inum=%(inum)s,ou=attributes,o=%(orgInum)s,%(suffix)s"""
    for pair in scopes.iteritems():
        scopeName = pair[0]
        scopeDic = pair[1]
        formatDic = scopeDic.copy()
        formatDic['displayName'] = scopeName
        formatDic['orgInum'] = d['orgInum']
        formatDic['suffix'] = d['suffix']

        r.append(template % formatDic)

        claimList = scopeDic['claims']
        for claimName in claimList:
            attrInum = attributeIdMap.get(claimName)
            if not attrInum == None:
                formatDic['inum'] = attrInum
                r.append(claimsTemplate % formatDic)

    result = '\n'.join(r)
    print "===== getScopeLDIF() generates: " + result
    return result

def getGroupsLDIF():
    template = """

dn: inum=%(managerGroupInum)s,ou=groups,o=%(orgInum)s,%(suffix)s
displayName: Gluu Manager Group
gluuGroupType: gluuManagerGroup
gluuStatus: active
iname: @mustardseed*group*managerGroup
inum: %(managerGroupInum)s
o: o=%(orgInum)s,%(suffix)s
objectClass: gluuGroup
objectClass: top
member: inum=%(personInum)s!%(personQuad)s,ou=people,o=%(orgInum)s,%(suffix)s
owner: inum=%(personInum)s!%(personQuad)s,ou=people,o=%(orgInum)s,%(suffix)s"""
    r = []
    r.append(template % d)
    result = '\n'.join(r)
    print "===== getGroupsLDIF() generates: " + result
    return result

def printTemplate():
    f = open(d['dataTemplateFile'])
    template = f.read()
    f.close()
#    d['personQuad'] = getInumberQuad()
#    d['groupQuad'] = getInumberQuad()
#    d['applianceQuad'] = getInumberQuad()
    return template % d


def generateDataLdif():
    s = printTemplate()
    f = open(d['dataGeneratedFile'], 'w')
    f.write(s + getAttributeLDIF() + getScopeLDIF() + getGroupsLDIF())
    f.close()

#generateDataLdif()

