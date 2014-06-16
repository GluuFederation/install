__author__ = 'yuriy'
import os, config

# Global Variables
d = config.getConfigDir()
errors = []
cwd = os.getcwd()

schemaDict = {'string':         {'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.15',
                                 'SUBSTR': 'caseIgnoreSubstringsMatch',
                                 'EQUALITY': 'caseIgnoreMatch'},
              'integer':        {'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.27',
                                 'ORDERING': 'integerOrderingMatch',
                                 'MATCH': 'integerMatch'},
              'dn':             {'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.12',
                                 'EQUALITY': 'distinguishedNameMatch'},
              'boolean':        {'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.7',
                                 'EQUALITY': 'booleanMatch'},
              'numericString':  {'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.36',
                                 'SUBSTR': 'numericStringSubstringsMatch',
                                 'EQUALITY': 'numericStringMatch'},
              'generalizedTime':{'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.24',
                                 'ORDERING': 'generalizedTimeOrderingMatch',
                                 'EQUALITY': 'generalizedTimeMatch'
                                 },
              'photo':         {'SYNTAX': '1.3.6.1.4.1.1466.115.121.1.15',
                                 'SUBSTR': 'caseIgnoreSubstringsMatch',
                                 'EQUALITY': 'caseIgnoreMatch'}
            }

# This is a list of the Gluu Custom Attributes. Note attribute descriptions
# and displayNames are only necessary for attributes that might be displayed to
# a user or admin
type = 'type'
desc = 'desc'
display = 'display'
customAttrDict = { 			'gluuCentreonEmail': {type:'string', desc:'Centreon Alert Email Address', display:'Centreon Alert Email'},
                            'gluuJiraEmail': {type:'string', desc:'Jira Alert Email Address', display:'Jira Alert Email'},
                            'gluuBillingEmail': {type:'string', desc:'Billing Alert Email Address', display:'Billing Alert Email'},
                            'gluuPrivacyEmail': {type:'string', desc:'Privacy Alert Email Address', display:'Privacy Alert Email'},
                            'gluuSvnEmail': {type:'string', desc:'SVN Alert Email Address', display:'SVN Alert Email'},
                            'gluuSmtpHost': {type:'string', desc:'SMTP Host', display:'SMTP Host'},
                            'gluuSmtpFromName': {type:'string', desc:'SMTP From Name', display:'SMTP From Name'},
                            'gluuSmtpFromEmailAddress': {type:'string', desc:'SMTP From Email Address', display:'SMTP From Email Address'},
                            'gluuSmtpRequiresAuthentication': {type:'string', desc:'SMTP Requires Authentication', display:'SMTP Requires Authentication'},
                            'gluuSmtpUserName': {type:'string', desc:'SMTP User Name', display:'SMTP User Name'},
                            'gluuSmtpPassword': {type:'string', desc:'SMTP User Password', display:'SMTP User Password'},
                            'gluuSmtpRequiresSsl': {type:'string', desc:'SMTP Requires SSL', display:'SMTP Requires SSL'},
                            'gluuSmtpPort': {type:'string', desc:'SMTP Port', display:'SMTP Port'},
                            'gluuApplianceDnsServer': {type:'string', desc:'Appliance DNS Server', display:'Appliance DNS Server'},
                            'gluuMaxLogSize': {type:'string', desc:'Maximum Log File Size', display:'Maximum Log File Size'},
                            'blowfishPassword': {type:'string', desc:'Blog Web URI', display:'Blog URI'},
                            'gluuAddPersonCapability': {type:'string', desc:'', display:''},
                            'gluuAppliancePollingInterval': {type:'string', desc:'', display:''},
                            'gluuAttributeEditType': {type:'string', desc:'', display:''},
                            'oxSCIMCustomAttribute': {type:'string', desc:'', display:''},
                            'oxMultivaluedAttribute': {type:'string', desc:'', display:''},
                            'gluuAttributeName': {type:'string' , desc:'', display:''},
                            'gluuAttributeOrigin': {type:'string' , desc:'', display:''},
                            'gluuAttributePrivacyLevel': {type:'string' , desc:'', display:''},
                            'gluuAttributeSystemEditType': {type:'string' , desc:'', display:''},
                            'gluuAttributeType': {type:'string' , desc:'', display:''},
                            'gluuAttributeViewType': {type:'string' , desc:'', display:''},
                            'gluuAttributeUsageType': {type:'string' , desc:'', display:''},
                            'gluuManageIdentityPermission': {type:'string' , desc:'', display:''},
                            'gluuCategory': {type:'string' , desc:'', display:''},
                            'gluuDSstatus': {type:'string' , desc:'', display:''},
                            'gluuFreeDiskSpace': {type:'string' , desc:'', display:''},
                            'gluuFreeSwap': {type:'string' , desc:'', display:''},
                            'gluuGroupCount': {type:'string' , desc:'', display:''},
                            'gluuGroupType': {type:'string' , desc:'', display:''},
                            'gluuGroupVisibility': {type:'string' , desc:'', display:''},
                            'gluuHostname': {type:'string' , desc:'', display:''},
                            'gluuHTTPstatus': {type:'string' , desc:'', display:''},
                            'gluuIpAddress': {type:'string' , desc:'', display:''},
                            'gluuLogoImage': {type:'string' , desc:'', display:''},
                            'gluuFaviconImage': {type:'string' , desc:'', display:''},
                            'gluuTempFaviconImage': {type:'string' , desc:'', display:''},
                            'gluuLastUpdate': {type:'string' , desc:'', display:''},
                            'gluuManagerGroup': {type:'string' , desc:'', display:'Organization Identity Managers'},
                            'gluuFreeMemory': {type:'string' , desc:'', display:''},
                            'gluuBandwidthTX': {type:'string' , desc:'', display:''},
                            'gluuBandwidthRX': {type:'string' , desc:'', display:''},
                            'gluuTrustContact': {type:'string' , desc:'', display:''},
                            'gluuTrustDeconstruction': {type:'string' , desc:'', display:''},
                            'gluuOwnerGroup': {type:'string' , desc:'', display:'Organization Identity Owners'},
                            'gluuOrgShortName': {type:'string' , desc:'', display:'Organization Short Name'},
                            'gluuOrgProfileMgt': {type:'string' , desc:'', display:''},
                            'gluuPersonCount': {type:'string' , desc:'', display:''},
                            'gluuPublishIdpMetadata': {type:'string' , desc:'', display:''},
                            'gluuReleasedAttribute': {type:'string' , desc:'', display:''},
                            'gluuShibAssertionsIssued': {type:'string' , desc:'', display:''},
                            'gluuShibFailedAuth': {type:'string' , desc:'', display:''},
                            'gluuShibSecurityEvents': {type:'string' , desc:'', display:''},
                            'gluuShibSuccessfulAuths': {type:'string' , desc:'', display:''},
                            'gluuStatus': {type:'string' , desc:'', display:''},
							'gluuValidationStatus': {type:'string' , desc:'', display:''},
                            'gluuSystemUptime': {type:'string' , desc:'', display:''},
                            'gluuVDSstatus': {type:'string' , desc:'', display:''},
                            'gluuVDSenabled': {type:'string' , desc:'', display:''},
                            'gluuThemeColor': {type:'string' , desc:'', display:''},
                            'gluuCustomMessage': {type:'string' , desc:'', display:''},
                            'gluuWhitePagesEnabled': {type:'string' , desc:'', display:''},
                            'gluuFederationHostingEnabled': {type:'string' , desc:'', display:''},
                            'gluuContainerFederation': {type:'dn' , desc:'', display:''},
                            'gluuIsFederation': {type:'string' , desc:'', display:''},
                            'gluuVdsCacheRefreshEnabled': {type:'string' , desc:'', display:''},
                            'gluuVdsCacheRefreshPollingInterval': {type:'string' , desc:'', display:''},
                            'gluuVdsCacheRefreshLastUpdate': {type:'string' , desc:'', display:''},
                            'gluuVdsCacheRefreshLastUpdateCount': {type:'string' , desc:'', display:''},
                            'gluuVdsCacheRefreshProblemCount': {type:'string' , desc:'', display:''},
                            'oxAuthenticationMode': {type:'string' , desc:'', display:''},
                            'oxAuthenticationLevel': {type:'string' , desc:'', display:''},
                            'gluuScimEnabled': {type:'string' , desc:'', display:''},
                            'gluuValidationLog':{type:'string', desc:'', display:''},
                            'gluuApplianceUpdateReuestList':{type:'string', desc:'', display:''},
                            'gluuResizeInitiated':{type:'string', desc:'', display:''},
                            'iname': {type:'string' , desc:'', display:''},
                            'inum': {type:'string' , desc:'XRI i-number', display:'i-number'},
                            'inumFN': {type:'string' , desc:'XRI i-number sans punctuation', display:'i-number'},
                            'memberOf': {type:'string' , desc:'', display:''},
                            'photo1': {type:'photo', desc:'Photo', display:'Photo'},
                            'primaryKeyAttrName': {type:'string', desc:'Primary Key Attribute Name', display:'Primary Key Attribute Name'},
                            'primaryKeyValue': {type:'string', desc:'Primary Key Value', display:'Primary Key Value'},
                            'secondaryKeyAttrName': {type:'string', desc:'Secondary Key Attribute Name', display:'Secondary Key Attribute Name'},
                            'secondaryKeyValue': {type:'string', desc:'Secondary Key Value', display:'Secondary Key Value'},
                            'tertiaryKeyAttrName': {type:'string', desc:'Tertiary Key Attribute Name', display:'Tertiary Key Attribute Name'},
                            'tertiaryKeyValue': {type:'string', desc:'Tertiary Key Value', display:'Tertiary Key Value'},
                            'role': {type:'string', desc:'Role', display:'Role'},
                            'secretAnswer': {type:'string' , desc:'Secret Answer', display:'Secret Answer'},
                            'secretQuestion': {type:'string' , desc:'Secret Question', display:'Secret Question'},
                            'gluuSAMLspMetaDataFN': {type:'string' , desc:'', display:''},
                            'gluuSAMLspMetaDataSourceType': {type:'string' , desc:'', display:''},
                            'gluuSAMLspMetaDataURL': {type:'string' , desc:'', display:''},
                            'gluuSAMLMetaDataFilter': {type:'string' , desc:'', display:''},
                            'gluuProfileConfiguration': {type:'string' , desc:'', display:''},
                            'gluuEntityId': {type:'string' , desc:'', display:''},
                            'gluuSAMLTrustEngine': {type:'string' , desc:'', display:''},
                            'gluuSAMLmaxRefreshDelay': {type:'string' , desc:'', display:''},
                            'timezone': {type:'string' , desc:'Timezone', display:'Timezone'},
                            'transientId': {type:'string' , desc:'TransientId', display:'TransientId'},
                            'persistentId': {type:'string' , desc:'PersistentId', display:'PersistentId'},
                            'urn': {type:'string' , desc:'', display:''},
                            'gluuSAML1URI': {type:'string' , desc:'', display:''},
                            'gluuSAML2URI': {type:'string' , desc:'', display:''},
                            'gluuWhitePagesListed':{type:'string', desc:'Allow Publication', display:'Allow Publication'},
                            'gluuSLAManager':{type:'string', desc:'', display:''},
                            'oxExternalUid':{type:'string', desc:'', display:'External identifier for custom strong auth systems.'},
                            'oxTrustEmail':{type:'string', desc:'', display:''},
                            'oxTrustMiddleName':{type:'string', desc:'', display:''},
                            'oxTrustNameFormatted':{type:'string', desc:'', display:''},
                            'oxTrusthonorificPrefix':{type:'string', desc:'', display:''},
                            'oxTrusthonorificSuffix':{type:'string', desc:'', display:''},
                            'oxTrustPhoneValue':{type:'string', desc:'', display:''},
                            'oxTrustImsValue':{type:'string', desc:'', display:''},
                            'oxTrustPhotos':{type:'string', desc:'', display:''},
                            'oxTrustExternalId':{type:'string', desc:'', display:''},
                            'oxTrustUserType':{type:'string', desc:'', display:''},
                            'oxTrustTitle':{type:'string', desc:'', display:''},
                            'oxTrustActive':{type:'string', desc:'', display:''},
                            'oxTrustx509Certificate':{type:'string', desc:'', display:''},
                            'oxTrustMetaCreated':{type:'string', desc:'', display:''},
                            'oxTrustMetaLastModified':{type:'string', desc:'', display:''},
                            'oxTrustMetaVersion':{type:'string', desc:'', display:''},
                            'oxTrustMetaLocation':{type:'string', desc:'', display:''},
                            'oxTrustNickName':{type:'string', desc:'', display:''},
                            'oxTrustProfileURL':{type:'string', desc:'', display:''},
                            'oxTrustLocale':{type:'string', desc:'', display:''},
                            'oxTrustRole':{type:'string', desc:'', display:''},
                            'oxTrustEntitlements':{type:'string', desc:'', display:''},
                            'oxTrustAddresses':{type:'string', desc:'', display:''},
                            'associatedClient':{type:'string', desc:'', display:''},
                            'gluuOptOuts':{type:'string', desc:'Attributes restricted by person', display:'White Pages removed'},
                            'gluuSpecificRelyingPartyConfig':{type:'string' , desc:'', display:''},
                            'gluuRulesAccepted':{type:'string' , desc:'', display:''},
                            'federationRules':{type:'string' , desc:'', display:''},
                            'deployedAppliances':{type:'string' , desc:'', display:''},
                            'gluuUrl':{type:'string' , desc:'', display:''},
                            'softwareVersion':{type:'string' , desc:'', display:''},
                            'gluuSPTR':{type:'string', desc:'', display:''},
                            'url':{type:'string', desc:'', display:''},
                            'proStoresToken':{type:'string', desc:'', display:''},
                            'gluuManager':{type:'string', desc:'', display:''},
                            'gluuPaidUntil':{type:'string', desc:'', display:''},
                            'gluuInvoiceNo':{type:'string', desc:'', display:''},
                            'gluuProStoresUser':{type:'string', desc:'', display:''},
                            'gluuSslExpiry':{type:'string', desc:'', display:''},
                            'gluuInvoiceNumber':{type:'string', desc:'', display:''},
                            'gluuInvoiceDate':{type:'generalizedTime', desc:'', display:''},
                            'gluuInvoiceAmount':{type:'string', desc:'', display:''},
                            'gluuInvoiceStatus':{type:'string', desc:'', display:''},
                            'gluuInvoiceLineItemName':{type:'string', desc:'', display:''},
                            'gluuInvoiceProductNumber':{type:'string', desc:'', display:''},
                            'gluuInvoiceQuantity':{type:'string', desc:'', display:''},
							'gluuAdditionalMemory':{type:'string', desc:'', display:''},
							'gluuAdditionalUsers':{type:'string', desc:'', display:''},
							'gluuAdditionalBandwidth':{type:'string', desc:'', display:''},
                            'nonProfit':{type:'boolean', desc:'', display:''},
                            'gluuTargetRAM':{type:'string', desc:'', display:''},
                            'gluuManagedOrganizations':{type:'string', desc:'', display:''},
                            'county': {type:'string' , desc:'', display:''},
                            'prostoresTimestamp': {type:'string' , desc:'', display:''},
                            'gluuPaymentProcessorTimestamp': {type:'string' , desc:'', display:''},
                            'gluuLoadAvg': {type:'string' , desc:'', display:''},
                            'gluuLifeRay': {type:'string' , desc:'', display:''},
                            'gluuPrivate': {type:'string' , desc:'', display:''},
                            'x':{type:'string', desc:'OX XRI Component', display:''},
							'xri':{type:'string', desc:'OX XRI address', display:''},
							'sourceRelationalXdiStatement':{type:'string', desc:'OX SourceRelationalXdiStatement', display:''},
							'targetRelationalXdiStatement':{type:'string', desc:'OX TargetRelationalXdiStatement', display:''},
							'myCustomAttr1':{type:'string', desc:'MyCustomAttribute1', display:''},
							'myCustomAttr2':{type:'string', desc:'MyCustomAttribute2', display:''},
							'oxAuthTrustedClient':{type:'string', desc:'oxAuth Trusted Client', display:''},
							'literalValue':{type:'string', desc:'OX literalValue', display:''},
							'literalBinaryValue':{type:'string', desc:'OX literalValue', display:''},
							'xdiStatement':{type:'string', desc:'OX xdiStatement', display:''},
							'organizationalOwner':{type:'string', desc:'OX organizationalOwner', display:''},
                            'oxAuthClientId':{type:'string', desc:'oxAuth Client id', display:''},
                            'oxAuthClientSecret':{type:'string', desc:'oxAuth Client Secret', display:''},
                            'associatedPerson':{type:'string', desc:'associatedPerson', display:''},
                            'oxAuthClientUserGroup':{type:'string', desc:'oxAuth Client User group', display:''},
                            'oxAuthContact':{type:'string', desc:'oxAuth Contact', display:''},
                            'oxAuthAppType':{type:'string', desc:'oxAuth App Type', display:''},
                            'oxAuthRegistrationAccessToken':{type:'string', desc:'oxAuth Registration Access Token', display:''},
                            'oxAuthLogoURI':{type:'string', desc:'oxAuth Logo URI', display:''},
                            'oxAuthClientURI':{type:'string', desc:'oxAuth Client URI', display:''},
                            'oxAuthRedirectURI':{type:'string', desc:'oxAuth Redirect URI', display:''},
                            'oxAuthTokenEndpointAuthMethod':{type:'string', desc:'oxAuth Token Endpoint Auth Method', display:''},
                            'oxAuthPolicyURI':{type:'string', desc:'oxAuth Policy URI', display:''},
                            'oxAuthTosURI':{type:'string', desc:'oxAuth TOS URI', display:''},
                            'oxAuthJwksURI':{type:'string', desc:'oxAuth JWKs URI', display:''},
                            'oxAuthX509URL':{type:'string', desc:'oxAuth x509 URL', display:''},
                            'oxAuthX509PEM':{type:'string', desc:'oxAuth x509 in PEM format', display:''},
                            'oxAuthSectorIdentifierURI':{type:'string', desc:'oxAuth Sector Identifier URI', display:''},
                            'oxAuthSubjectType':{type:'string', desc:'oxAuth Subject Type', display:''},
                            'oxAuthRequestObjectSigningAlg':{type:'string', desc:'oxAuth Request Object Signing Alg', display:''},
                            'oxAuthSignedResponseAlg':{type:'string', desc:'oxAuth Signed Response Alg', display:''},
                            'oxAuthUserInfoEncryptedResponseAlg':{type:'string', desc:'oxAuth User Info Encrypted Response Alg', display:''},
                            'oxAuthUserInfoEncryptedResponseEnc':{type:'string', desc:'oxAuth User Info Encrypted Response Enc', display:''},
                            'oxAuthIdTokenSignedResponseAlg':{type:'string', desc:'oxAuth ID Token Signed Response Alg', display:''},
                            'oxAuthIdTokenEncryptedResponseAlg':{type:'string', desc:'oxAuth ID Token Encrypted Response Alg', display:''},
                            'oxAuthIdTokenEncryptedResponseEnc':{type:'string', desc:'oxAuth ID Token Encrypted Response Enc', display:''},
                            'oxAuthClientIdIssuedAt':{type:'string', desc:'oxAuth Client Issued At', display:''},
                            'oxAuthClientSecretExpiresAt':{type:'string', desc:'Date client expires', display:''},
                            'oxAuthDefaultMaxAge':{type:'string', desc:'oxAuth Default Max Age', display:''},
                            'oxAuthRequireAuthTime':{type:'string', desc:'oxAuth Require Authentication Time', display:''},
                            'oxAuthDefaultAcrValues':{type:'string', desc:'oxAuth Default Acr Values', display:''},
                            'oxAuthInitiateLoginURI':{type:'string', desc:'oxAuth Initiate Login URI', display:''},
                            'oxAuthPostLogoutRedirectURI':{type:'string', desc:'oxAuth Post Logout Redirect URI', display:''},
                            'oxAuthRequestURI':{type:'string', desc:'oxAuth Request URI', display:''},
                            'oxAuthScope':{type:'string', desc:'oxAuth Attribute Scope', display:''},
                            'oxAuthFederationRequestType':{type:'string', desc:'oxAuth Federation request type attribute', display:''},
                            'oxAuthFederationOpId':{type:'string', desc:'oxAuth Federation OP ID attribute', display:''},
                            'oxAuthFederationOpDomain':{type:'string', desc:'oxAuth Federation OP domain attribute', display:''},
                            'oxAuthFederationMetadataIntervalCheck':{type:'string', desc:'oxAuth Federation metadata interval check attribute', display:''},
                            'oxAuthFederationOP':{type:'string', desc:'oxAuth Federation OP attribute', display:''},
                            'oxAuthFederationRP':{type:'string', desc:'oxAuth Federation RP attribute', display:''},
                            'oxAuthFederationMetadata':{type:'string', desc:'oxAuth Federation metadata attribute', display:''},
                            'oxAuthFederationMetadataURI':{type:'string', desc:'oxAuth Federation metadata URI attribute', display:''},
                            'oxAuthFederationId':{type:'string', desc:'oxAuth Federation ID attribute', display:''},
                            'oxAuthFederationTrustStatus':{type:'string', desc:'oxAuth Federation Trust Status attribute', display:''},
                            'oxAuthSkipAuthorization':{type:'string', desc:'oxAuth skip authorization attribute', display:''},
                            'oxAuthReleasedScope':{type:'string', desc:'oxAuth released scope attribute', display:''},
                            'oxAuthClaim':{type:'string', desc:'oxAuth Attribute Claim', display:''},
                            'oxAuthUserDN':{type:'string', desc:'oxAuth User DN', display:''},
                            'oxAuthConfErrors':{type:'string', desc:'oxAuth Errors Configuration', display:''},
                            'oxAuthConfStatic':{type:'string', desc:'oxAuth Static Configuration', display:''},
                            'oxAuthConfDynamic':{type:'string', desc:'oxAuth Dynamic Configuration', display:''},
                            'oxAuthConfWebKeys':{type:'string', desc:'oxAuth Web Keys Configuration', display:''},
                            'oxAuthConfLdapAuth':{type:'string', desc:'LDAP authentication configuration', display:''},
                            'oxAuthConfCustomAuthMethod':{type:'string', desc:'Custom authentication method', display:''},
                            'oxAuthConfIdPythonScript':{type:'string', desc:'Custom id generation', display:''},
                            'oxAuthResponseType':{type:'string', desc:'oxAuth Response Type', display:''},
                            'oxAuthGrantType':{type:'string', desc:'oxAuth Grant Type', display:''},
                            'oxAuthAuthenticationTime':{type:'string', desc:'oxAuth Authentication Time', display:''},
                            'oxAuthPermissionGranted':{type:'string', desc:'oxAuth Permission Granted', display:''},
                            'oxAuthPermissionGrantedMap':{type:'string', desc:'oxAuth Permission Granted Map', display:''},
                            'oxAuthTokenType':{type:'string', desc:'oxAuth Token Type', display:''},
                            'oxAuthTokenCode':{type:'string', desc:'oxAuth Token Code', display:''},
                            'oxAuthExpiration':{type:'string', desc:'oxAuth Expiration', display:''},
                            'oxAuthCreation':{type:'string', desc:'oxAuth Creation', display:''},
                            'oxAuthGrantId':{type:'string', desc:'oxAuth grant id', display:''},
                            'oxAuthUserId':{type:'string', desc:'oxAuth user id', display:''},
                            'oxAuthAuthorizationCode':{type:'string', desc:'oxAuth authorization code', display:''},
                            'oxAuthNonce':{type:'string', desc:'oxAuth nonce', display:''},
                            'oxAuthJwtRequest':{type:'string', desc:'oxAuth JWT Request', display:''},
                            'defaultScope':{type:'string', desc:'oxAuth default scope', display:''},
                            'oxAuthPersistentJWT':{type:'string', desc:'oxAuth Persistent JWT', display:''},
                            'scimAuthMode':{type:'string', desc:'SCIM Authorization mode', display:''},
                            'scimGroup':{type:'string', desc:'scim Group', display:''},
                            'scimStatus':{type:'string', desc:'scim status', display:''},
                            'oxTrustCustAttrB':{type:'string', desc:'scim status', display:''},
                            'oxFaviconImage':{type:'string', desc:'URI for a graphic icon', display:''},
                            'oxAuthUmaScope':{type:'string', desc:'URI reference of scope descriptor', display:''},
                            'oxGroup':{type:'string', desc:'User group', display:''},
                            'oxResource':{type:'string', desc:'Host path', display:''},
                            'oxId':{type:'string', desc:'Identifier', display:''},
                            'oxName':{type:'string', desc:'Name', display:''},
                            'oxRevision':{type:'string', desc:'Revision', display:''},
                            'oxPolicyRule':{type:'string', desc:'Revision', display:''},
                            'registrationDate':{type:'generalizedTime', desc:'Registration date', display:''},
                            'oxIDPAuthentication':{type:'string', desc:'Custom IDP authentication configuration', display:''},
                            'oxAmHost':{type:'string', desc:'am host', display:''},
                            'oxHost':{type:'string', desc:'ox host', display:''},
                            'oxTicket':{type:'string', desc:'ox ticket', display:''},
                            'oxConfigurationCode':{type:'string', desc:'ox configuration code', display:''},
                            'oxResourceSetId':{type:'string', desc:'ox resource set id', display:''},
                            'oxUmaPermission':{type:'string', desc:'ox uma permission', display:''},
                            'oxPolicyScript':{type:'string', desc:'ox policy script', display:''},
                            'oxType':{type:'string', desc:'ox type', display:''},
                            'programmingLanguage':{type:'string', desc:'programming language', display:''},
                            'oxAssociatedClient':{type:'string', desc:'ox associated client', display:''},
                            'oxUrl':{type:'string', desc:'ox url', display:''},
                            'oxIconUrl':{type:'string', desc:'ox icon url', display:''},
                            'oxTrustConfApplication':{type:'string', desc:'oxTrust Application Configuration', display:''},
                            'oxClusteredServers': {type:'string' , desc:'List of the clustering partners of this server', display:'CLustered Servers'},
                            'oxClusterType': {type:'string' , desc:'Type of the underlying clustering mechanism', display:'Cluster Type'},
                            'oxMemcachedServerAddress': {type:'string' , desc:'Initialization string for memcached client', display:'Memcached Server Address'},
                            'oxLogViewerConfig': {type:'string' , desc:'Log viewer configuration', display:''},
                            'oxGuid': {type:'string' , desc:'A random string to mark temporary tokens', display:'OX GUID'},
                            'personInum': {type:'string' , desc:'Inum of a person', display:'Inum of a person'},
                            'creationDate': {type:'string' , desc:'Creation Date', display:'Creation Date'},
                            'passwordResetAllowed': {type:'string' , desc:'Is password reset mechanics allowed', display:'Is password reset mechanics allowed'},
                            'oxProxConf':{type:'string', desc:'oxProx Configuration', display:''},
                            'oxProxyToOpClientMapping':{type:'string', desc:'oxProx client mapping to op client', display:''},
                            'oxProxyScope':{type:'string', desc:'oxProx scope', display:''},
                            'oxProxyClaimMapping':{type:'string', desc:'oxProx claim mapping', display:''},
                            'oxProxyAccessToken':{type:'string', desc:'oxProx access token', display:''},
                            'oxProxyClientId':{type:'string', desc:'oxProx client id', display:''},
                            'oxPushApplication':{type:'dn', desc:'oxPush application DN', display:''},
                            'oxPushApplicationConf':{type:'string', desc:'oxPush application configuration', display:''},
                            'oxPushDeviceConf':{type:'string', desc:'oxPush device configuration', display:''},
                            'oxDomain':{type:'string', desc:'domain', display:''},
                            'oxX509URL':{type:'string', desc:'x509 URL', display:''},
                            'oxX509PEM':{type:'string', desc:'x509 in PEM format', display:''},
                            'oxScriptDn':{type:'string', desc:'Script object DN', display:''},
                            'oxScript':{type:'string', desc:'Attribute that contains script (python, java script)', display:''},
                            'oxScriptType':{type:'string', desc:'Attribute that contains script type (e.g. python, java script)', display:''},
                            'oxTrustStoreConf':{type:'string', desc:'oxPush application configuration', display:''},
                            'oxTrustStoreCert':{type:'string', desc:'oxPush device configuration', display:''},
                            'oxLinkExpirationDate': {type:'string' , desc:'Link Expiration Date', display:'oxLinkExpirationDate'},
                            'oxLinkModerated': {type:'string' , desc:'Is Link Moderated?', display:'oxLinkModerated'},
                            'oxLinkModerators': {type:'string' , desc:'Link Moderators', display:'oxLinkModerators'},
                            'oxLinkCreator': {type:'string' , desc:'Link Creator', display:'oxLinkCreator'},
                            'oxLinkPending': {type:'string' , desc:'Pending Registrations', display:'oxLinkPending'},
							'oxLinkLinktrack': {type:'string' , desc:'Linktrack link', display:'oxLinkLinktrack'},
							'oxLinktrackEnabled': {type:'string' , desc:'Is Linktrack API configured', display:'oxLinktrackEnabled'},
							'oxLinktrackLogin': {type:'string' , desc:'Linktrack API login', display:'oxLinktrackUsername'},
							'oxLinktrackPassword': {type:'string' , desc:'Linktrack API password', display:'oxLinktrackPassword'},
                            'oxLastAccessTime': {type:'generalizedTime' , desc:'Last access time', display:'Last access time'},
                            'oxLastLogonTime': {type:'generalizedTime' , desc:'Last logon time', display:'Last logon time'},
                            'oxRegistrationConfiguration': {type:'string' , desc:'Registration Configuration', display:'Registration Configuration'},
                            'oxCreationTimestamp': {type:'generalizedTime' , desc:'Registration time', display:'Registration time'},
                            'oxInviteCode': {type:'string' , desc:'Invite Code', display:'Invite Code'},
                            'oxSmtpConfiguration': {type:'string', desc:'SMTP configuration', display:'SMTP configuration'},
                       }
unusedAttrs = customAttrDict

# This list is used for descriptions and display names
stdAttrDict =         {'c': {type:'string' , desc:'Country', display:'Country'},
                       'carLicense': {type:'string' , desc:'Vehicle Licence Plate Number', display:'Licencse Plate'},
                       'cn': {type:'string' , desc:'Name search keywords', display:'Name search keywords'},
                       'departmentNumber': {type:'string' , desc:'Organizational Department', display:'Department'},
                       'description': {type:'string' , desc:'Description', display:'Description'},
                       'displayName': {type:'string' , desc:'Display Name', display:'Display Name'},
                       'employeeNumber': {type:'string' , desc:'Employee Number', display:'Employee Number'},
                       'employeeType': {type:'string' , desc:'Employee Type', display:'Employee Type'},
                       'facsimileTelephoneNumber': {type:'string' , desc:'Fax Telephone Number', display:'Fax Number'},
                       'givenName': {type:'string' , desc:'First Name', display:'First Name'},
                       'homePhone': {type:'string' , desc:'Home Telephone Number', display:'Home Telephone Number'},
                       'homePostalAddress': {type:'string' , desc:'Home Address', display:'Home Address'},
                       'l': {type:'string' , desc:'City', display:'City'},
                       'mail': {type:'string' , desc:'Primary Email Address', display:'Email'},
                       'manager': {type:'string' , desc:'Manager', display:'Manager'},
                       'mobile': {type:'string' , desc:'Mobile Telephone Number', display:'Mobile Telephone Number'},
                       'o': {type:'string' , desc:'Organization i-number', display:'Organization i-number'},
                       'postalCode': {type:'string' , desc:'Postal or Zip Code', display:'Postal Code'},
                       'postOfficeBox': {type:'string' , desc:'Postal Box', display:'PO Box'},
                       'preferredDeliveryMethod': {type:'string' , desc:'Preferred Delivery Method', display:'Preferred Delivery Method'},
                       'preferredLanguage': {type:'string' , desc:'Preferred Language', display:'Preferred Language'},
                       'roomNumber': {type:'string' , desc:'Room Number', display:'Room Number'},
                       'secretary': {type:'string' , desc:'Secretary', display:'Secretary'},
                       'sn': {type:'string' , desc:'Last Name', display:'Last Name'},
                       'st': {type:'string' , desc:'State or Province', display:'State or Province'},
                       'street': {type:'string' , desc:'Street', display:'Street'},
                       'telephoneNumber': {type:'string' , desc:'Work Telephone Number', display:'Work Telephone Number'},
                       'title': {type:'string' , desc:'Organizational Title', display:'Title'},
                       'uid': {type:'string' , desc:'Organizational Username', display:'Username'},
                       'uniqueIdentifier': {type:'string' , desc:'Unique Identifier', display:'Unique Identifier'},
                       'lastModifiedTime': {type:'string' , desc:'Last modified time', display:'Last modified time'},
                       'userPassword': {type:'string' , desc:'Password', display:'Password'},
                      }

level1 = {'editType': ['user', 'admin'],'viewType': ['user', 'admin'], 'level': 1}
level2 = {'editType': [],'viewType': ['user', 'admin'], 'level': 2}
level3 = {'editType': ['admin'],'viewType': ['user', 'admin'], 'level': 3}
level4 = {'editType': ['admin'], 'viewType': ['admin'], 'level': 4}
level5 = {'editType': [],'viewType': ['admin'], 'level': 5}
level6 = {'editType': [],'viewType': [], 'level': 6}

# Specify in objects if they are (editable | readonly) or (hidden | visible)
oxEntry    = {  'inum': level1,
				'iname': level1,
				'displayName': level1
			 }

oxNode     = {  'x': level1,
				'xri': level1,
				'xdiStatement': level1,
				'organizationalOwner': level1,
				'owner': level1,
                'sourceRelationalXdiStatement': level1,
                'targetRelationalXdiStatement': level1
			}

oxLiteralNode = { 'x': level1,
                  'xri': level1,
                  'xdiStatement': level1,
                  'organizationalOwner': level1,
                  'owner': level1,
                  'literalBinaryValue': level1,
                  'literalValue': level1,
                  'targetRelationalXdiStatement': level1
                }

oxAuthClient = { 'inum': level1,
                'displayName': level1,
                'oxAuthClientSecret': level1,
                'oxAuthClientUserGroup': level1,
                'oxAuthContact': level1,
                'oxAuthAppType': level1,
                'oxAuthRegistrationAccessToken': level1,
                'oxAuthLogoURI': level1,
                'oxAuthClientURI': level1,
                'oxAuthRedirectURI': level1,
                'oxAuthResponseType': level1,
                'oxAuthGrantType': level1,
                'oxAuthTokenEndpointAuthMethod': level1,
                'oxAuthPolicyURI': level1,
                'oxAuthTosURI': level1,
                'oxAuthJwksURI': level1,
                'oxAuthSectorIdentifierURI': level1,
                'oxAuthSubjectType': level1,
                'oxAuthRequestObjectSigningAlg': level1,
                'oxAuthSignedResponseAlg': level1,
                'oxAuthUserInfoEncryptedResponseAlg': level1,
                'oxAuthUserInfoEncryptedResponseEnc': level1,
                'oxAuthIdTokenSignedResponseAlg': level1,
                'oxAuthIdTokenEncryptedResponseAlg': level1,
                'oxAuthIdTokenEncryptedResponseEnc': level1,
                'oxAuthClientIdIssuedAt': level1,
                'oxAuthClientSecretExpiresAt': level1,
                'oxAuthDefaultMaxAge': level1,
                'oxAuthRequireAuthTime': level1,
                'oxAuthDefaultAcrValues': level1,
                'oxAuthInitiateLoginURI': level1,
                'oxAuthPostLogoutRedirectURI': level1,
                'oxAuthRequestURI': level1,
                'oxAuthScope': level1,
                'associatedPerson': level1,
                'oxAuthFederationMetadataURI': level1,
                'oxAuthFederationId': level1,
                'oxAuthTrustedClient': level1,
                'oxLastAccessTime': level1,
                'oxLastLogonTime': level1,
               }

oxCustomAttributes = { 'oxTrustCustAttrB': level1 }

oxAuthCustomScope = { 'inum': level1,
                'displayName': level1,
                'description': level1,
                'oxAuthClaim': level1,
                'defaultScope': level1
               }

oxAuthFederationRP = {
                'inum': level1,
                'displayName': level1,
                'oxAuthRedirectURI': level1,
                'oxAuthX509PEM': level1,
                'oxAuthX509URL': level1
}

oxAuthFederationOP = {
                'inum': level1,
                'displayName': level1,
                'oxAuthFederationOpId': level1,
                'oxAuthFederationOpDomain': level1,
                'oxAuthX509PEM': level1,
                'oxAuthX509URL': level1
}

oxAuthFederationMetadata = {
                'inum': level1,
                'displayName': level1,
                'oxAuthRedirectURI': level1,
                'oxAuthFederationOP': level1,
                'oxAuthFederationRP': level1,
                'oxAuthFederationMetadataIntervalCheck': level1
}

oxAuthFederationRequest = {
                'inum': level1,
                'displayName': level1,
                'oxAuthRedirectURI': level1,
                'oxAuthFederationOpId': level1,
                'oxAuthFederationRequestType': level1,
                'oxAuthFederationOpDomain': level1
}

oxAuthFederationTrust = {
                'inum': level1,
                'displayName': level1,
                'oxAuthRedirectURI': level1,
                'oxAuthFederationId': level1,
                'oxAuthFederationMetadataURI': level1,
                'oxAuthFederationTrustStatus': level1,
                'oxAuthSkipAuthorization': level1,
                'oxAuthReleasedScope': level1
}

oxAuthSessionId = {
                'uniqueIdentifier': level1,
                'lastModifiedTime': level1,
                'oxAuthUserDN': level1,
                'oxAuthAuthenticationTime': level1,
                'oxAuthPermissionGranted': level1,
                'oxAuthPermissionGrantedMap': level1
}

oxAuthConfiguration = {
                'oxAuthConfDynamic': level1,
                'oxAuthConfStatic': level1,
                'oxAuthConfErrors': level1,
                'oxAuthConfWebKeys': level1,
                'oxAuthConfLdapAuth': level1,
                'oxAuthConfIdPythonScript': level1,
                'oxAuthConfCustomAuthMethod': level1,
                'ou': level1
}

oxProxConfiguration = {
               'oxProxConf': level1,
               'oxScriptDn': level1,
               'ou': level1
}
oxProxOp = {
                'inum': level1,
                'displayName': level1,
                'oxId': level1,
                'oxDomain': level1,
                'c': level1,
                'l': level1,
                'oxX509PEM': level1,
                'oxX509URL': level1
}
oxProxClient = {
                'inum': level1,
                'displayName': level1,
                'oxProxyToOpClientMapping': level1,
                'oxProxyClaimMapping': level1,
                'oxProxyScope': level1
}

oxProxAccessToken = {
                'oxProxyAccessToken': level1,
                'oxProxyClientId': level1,
                'oxAuthCreation': level1,
                'oxAuthExpiration': level1
}

oxScript = {
                'inum': level1,
                'oxScript': level1,
                'oxScriptType': level1
}

oxTrustConfiguration = {
                'oxTrustConfApplication': level1,
                'ou': level1
}

oxAuthToken = {
                'uniqueIdentifier': level1,
                'oxAuthGrantType': level1,
                'oxAuthAuthenticationTime': level1,
                'oxAuthScope': level1,
                'createTimestamp': level1,
                'oxAuthCreation': level1,
                'oxAuthExpiration': level1,
                'oxAuthJwtRequest': level1,
                'oxAuthGrantId': level1,
                'oxAuthUserId': level1,
                'oxAuthAuthorizationCode': level1,
                'oxAuthNonce': level1,
                'oxAuthTokenCode': level1,
                'oxAuthTokenType': level1,
                'oxAuthenticationMode': level1,
                'oxAuthenticationLevel': level1
}


oxAuthUmaResourceSet = {
                'inum': level1,
                'oxId': level1,
                'displayName': level1,
                'oxFaviconImage': level1,
                'oxAuthUmaScope': level1,
                'oxRevision': level1,
                'oxGroup': level1,
                'oxResource': level1,
                'oxAssociatedClient': level1,
                'oxType': level1,
                'owner': level1
               }

oxAuthUmaScopeDescription = {
                'inum': level1,
                'oxId': level1,
                'displayName': level1,
                'oxFaviconImage': level1,
                'oxRevision': level1,
                'oxPolicyRule': level1,
                'oxAssociatedClient': level1,
                'oxUrl': level1,
                'oxIconUrl': level1,
                'oxType': level1,
                'owner': level1
               }

oxAuthUmaResourceSetPermission = {
                'oxAmHost': level1,
                'oxHost': level1,
                'oxAuthExpiration': level1,
                'oxTicket': level1,
                'oxConfigurationCode': level1,
                'oxResourceSetId': level1,
                'oxAuthUmaScope': level1
}

oxAuthUmaRPT = {
                'uniqueIdentifier': level1,
                'oxAuthUserId': level1,
                'oxAuthClientId': level1,
                'oxAuthAuthenticationTime': level1,
                'oxAuthTokenCode': level1,
                'oxAuthCreation': level1,
                'oxAuthExpiration': level1,
                'oxAmHost': level1,
                'oxUmaPermission': level1
}

oxAuthUmaPolicy = {
                'inum': level1,
                'displayName': level1,
                'description': level1,
                'oxPolicyScript': level1,
                'programmingLanguage': level1,
                'oxAuthUmaScope': level1
}

oxPushApplication = {
                'oxId': None,
                'oxName': None,
                'displayName': None,
                'oxPushApplicationConf': None
}

oxPushDevice = {
                'oxId': None,
                'oxType': None,
                'oxPushApplication': None,
                'oxAuthUserId': None,
                'oxPushDeviceConf': None
}

gluuPerson = {  'c': level1,
                'displayName': level1,
                'givenName': level1,
                'iname': level2,
                'inum': level2,
                'mail': level1,
                'memberOf': level5,
                'o': level5,
                'preferredLanguage': level1,
                'secretQuestion': level1,
                'secretAnswer': level1,
                'gluuStatus': level6,
                'seeAlso': level6,
                'sn': level1,
                'timezone': level1,
                'transientId': level1,
                'persistentId': level1,
                'role': level3,
                'uid': level2,
                'userPassword': level6,
                'photo1': level1,
                'gluuWhitePagesListed': level1,
				'gluuSLAManager': level5,
                'gluuOptOuts': level1,
                'gluuManagedOrganizations': level6,
                'oxTrustEmail': level1,
                'oxTrustMiddleName': level1,
                'oxTrustNameFormatted': level1,
                'oxTrusthonorificPrefix': level1,
                'oxTrusthonorificSuffix': level1,
                'oxTrustPhoneValue': level1,
                'oxTrustImsValue': level1,
                'oxTrustPhotos': level1,
                'oxTrustExternalId': level1,
                'oxTrustUserType': level1,
                'oxTrustTitle': level1,
                'oxTrustActive': level1,
                'oxTrustx509Certificate': level1,
                'oxTrustMetaCreated': level1,
                'oxTrustMetaLastModified': level1,
                'oxTrustMetaVersion': level1,
                'oxTrustMetaLocation': level1,
                'oxTrustNickName': level1,
                'oxTrustProfileURL': level1,
                'oxTrustLocale': level1,
                'oxTrustRole': level1,
                'oxTrustEntitlements': level1,
                'oxExternalUid': level4,
                'oxTrustAddresses': level1,
                'associatedClient': level1,
                'oxAuthPersistentJWT': level1,
                'oxCreationTimestamp': level1,
                'oxInviteCode': level1,
                'oxLastLogonTime': level1,
}

eduPerson = {   'eduPersonNickname': level4,
                'eduPersonOrgDN': level4,
                'eduPersonOrgUnitDN': level4,
                'eduPersonPrincipalName': level4,
                'eduPersonEntitlement': level4,
                'eduPersonAffiliation': level4,
                'eduPersonPrimaryAffiliation': level4,
                'eduPersonPrimaryOrgUnitDN': level4,
                'eduPersonScopedAffiliation': level4,
                'eduPersonTargetedID': level4,
                'eduPersonAssurance': level4}

inetOrgPerson = {   'sn': level1,
                    'cn': level1,
                    'userPassword': level6,
                    'telephoneNumber': level1,
                    'seeAlso': level6,
                    'description': level1,
                    'title': level3,
                    'x121Address': level6,
                    'registeredAddress': level6,
                    'destinationIndicator': level6,
                    'preferredDeliveryMethod': level4,
                    'telexNumber': level6,
                    'teletexTerminalIdentifier': level6,
                    'telephoneNumber': level1,
                    'internationaliSDNNumber': level6,
                    'facsimileTelephoneNumber': level1,
                    'street': level1,
                    'postOfficeBox': level1,
                    'postalCode': level1,
                    'postalAddress': level6,
                    'physicalDeliveryOfficeName': level6,
                    'ou': level6,
                    'st': level1,
                    'l': level1,
                    'businessCategory': level6,
                    'carLicense': level1,
                    'departmentNumber': level3,
                    'displayName': level1,
                    'employeeNumber': level4,
                    'employeeType': level4,
                    'givenName': level1,
                    'homePhone': level1,
                    'homePostalAddress': level1,
                    'initials': level6,
                    'jpegPhoto': level6,
                    'labeledURI': level6,
                    'mail': level1,
                    'manager': level4,
                    'mobile': level1,
                    'o': level4,
                    'pager': level6,
                    'photo': level6,
                    'roomNumber': level1,
                    'secretary': level4,
                    'uid': level2,
                    'userCertificate': level6,
                    'x500UniqueIdentifier': level6,
                    'preferredLanguage': level1,
                    'userSMIMECertificate': level6,
                    'userPKCS12': level6}

gluuGroup=  {  'c': None,
                'description': None,
                'displayName': None,
                'gluuGroupVisibility': None,
                'gluuStatus': None,
                'gluuGroupType': None,
                'iname': None,
                'inum': None,
                'member': None,
                'o': None,
                'owner': None,
                'seeAlso': None}

gluuOrganization= {  'c': None,
                     'l':None,
                     'st':None,
                     'gluuOrgShortName': None,
                     'description': None,
                     'displayName': None,
                     'gluuLogoImage': None,
                     'gluuFaviconImage': None,
                     'gluuTempFaviconImage': None,
                     'gluuThemeColor': None,
                     'gluuCustomMessage': None,
                     'iname': None,
                     'inum': None,
                     'mail': None,
                     'memberOf': None,
                     'o': None,
                     'uid': None,
                     'userPassword': None,
                     'objectClass': None,
                     'gluuStatus': None,
                     'gluuManagerGroup': None,
                     'gluuOwnerGroup': None,
                     'gluuAddPersonCapability': None,
                     'gluuOrgProfileMgt': None,
                     'gluuManageIdentityPermission': None,
                     'gluuWhitePagesEnabled': None,
                     'gluuFederationHostingEnabled': None,
                     'deployedAppliances':None,
                     'gluuManager': None,
                     'gluuInvoiceNo': None,
                     'gluuPaidUntil': None,
					 'gluuProStoresUser': None,
					 'gluuAdditionalUsers': None,
                     'nonProfit': None,
                     'proStoresToken':None,
                     'street':None,
                     'postalCode':None,
                     'county':None,
                     'title':None,
                     'telephoneNumber':None,
                     'prostoresTimestamp':None,
                     'gluuPaymentProcessorTimestamp':None,
					 'scimAuthMode': None,
					 'scimGroup': None,
					 'scimStatus': None,
                     'gluuApplianceUpdateReuestList':None,
					 'oxLinkLinktrack':None,
					 'oxLinktrackEnabled':None,
					 'oxLinktrackLogin':None,
                     'oxRegistrationConfiguration':None,
                     'oxCreationTimestamp':None,
					 'oxLinktrackPassword':None
                   }

gluuAppliance= {  'iname': None,
                  'inum': None,
                  'inumFN': None,
                  'c': None,
                  'o': None,
                  'description': None,
                  'displayName': None,
                  'gluuAppliancePollingInterval': None,
                  'gluuFreeMemory': None,
                  'gluuFreeDiskSpace': None,
                  'gluuFreeSwap': None,
                  'gluuPersonCount': None,
                  'gluuGroupCount': None,
                  'gluuHostname': None,
                  'gluuIpAddress': None,
                  'gluuLastUpdate': None,
                  'gluuPublishIdpMetadata': None,
                  'gluuShibAssertionsIssued': None,
                  'gluuShibFailedAuth': None,
                  'gluuShibSecurityEvents': None,
                  'gluuShibSuccessfulAuths': None,
                  'gluuStatus': None,
                  'gluuDSstatus': None,
                  'gluuVDSstatus': None,
                  'gluuVDSenabled': None,
                  'gluuCentreonEmail': None,
                  'gluuJiraEmail': None,
                  'gluuBillingEmail': None,
                  'gluuPrivacyEmail': None,
                  'gluuSvnEmail': None,
                  'gluuSmtpHost': None,
                  'gluuSmtpFromName': None,
                  'gluuSmtpFromEmailAddress': None,
                  'gluuSmtpRequiresAuthentication': None,
                  'gluuSmtpUserName': None,
                  'gluuSmtpPassword': None,
                  'gluuSmtpRequiresSsl': None,
                  'gluuSmtpPort': None,
                  'gluuApplianceDnsServer': None,
                  'gluuMaxLogSize': None,
                  'gluuBandwidthTX': None,
                  'gluuBandwidthRX': None,
                  'gluuHTTPstatus': None,
                  'gluuSystemUptime': None,
                  'blowfishPassword': None,
                  'userPassword': None,
                  'gluuSPTR': None,
                  'gluuUrl':None,
                  'gluuOrgProfileMgt': None,
                  'gluuManageIdentityPermission': None,
                  'gluuWhitePagesEnabled': None,
                  'gluuFederationHostingEnabled': None,
                  'gluuVdsCacheRefreshEnabled':None,
                  'oxAuthenticationMode':None,
                  'oxAuthenticationLevel':None,
                  'gluuVdsCacheRefreshPollingInterval':None,
                  'gluuVdsCacheRefreshLastUpdate':None,
                  'gluuVdsCacheRefreshLastUpdateCount':None,
                  'gluuVdsCacheRefreshProblemCount':None,
                  'gluuScimEnabled':None,
                  'softwareVersion':None,
                  'gluuManager': None,
                  'gluuInvoiceNo': None,
                  'gluuPaidUntil': None,
                  'gluuAdditionalMemory': None,
                  'gluuAdditionalBandwidth': None,
                  'gluuSslExpiry':None,
                  'gluuTargetRAM':None,
                  'gluuPaymentProcessorTimestamp':None,
                  'gluuLoadAvg':None,
                  'gluuLifeRay':None,
                  'gluuPrivate':None,
                  'gluuResizeInitiated':None,
                  'oxIDPAuthentication':None,
                  'oxClusteredServers':None,
                  'oxClusterType':None,
                  'oxMemcachedServerAddress':None,
                  'oxLogViewerConfig':None,
                  'passwordResetAllowed':None,
                  'oxTrustStoreConf':None,
                  'oxTrustStoreCert':None,
                  'oxSmtpConfiguration':None,
                }

gluuAttribute= { 'description': None,
                 'displayName': None,
                 'gluuAttributeOrigin': None,
                 'gluuAttributeEditType': None,
                 'gluuAttributeName': None,
                 'oxSCIMCustomAttribute': None,
                 'oxMultivaluedAttribute': None,
                 'gluuAttributePrivacyLevel': None,
                 'gluuAttributeSystemEditType': None,
                 'gluuAttributeType': None,
                 'gluuAttributeViewType': None,
                 'gluuAttributeUsageType': None,
                 'gluuCategory': None,
                 'gluuStatus': None,
                 'iname': None,
                 'inum': None,
                 'objectClass': None,
                 'seeAlso': None,
                 'gluuSAML1URI': None,
                 'gluuSAML2URI': None,
                 'urn': None,
                }

gluuSAMLconfig= { 'description': None,
                  'displayName': None,
                  'iname': None,
                  'inum': None,
                  'objectClass': None,
                  'gluuStatus': None,
                  'gluuValidationStatus': None,
                  'gluuReleasedAttribute': None,
                  'gluuSAMLspMetaDataSourceType': None,
                  'gluuSAMLspMetaDataFN': None,
                  'gluuSAMLspMetaDataURL': None,
                  'gluuSpecificRelyingPartyConfig': None,
                  'o': None,
                  'gluuTrustContact': None,
                  'gluuTrustDeconstruction': None,
                  'gluuSAMLMetaDataFilter': None,
                  'gluuProfileConfiguration':None,
                  'gluuSAMLTrustEngine': None,
                  'gluuSAMLmaxRefreshDelay': None,
                  'gluuContainerFederation': None,
                  'gluuIsFederation': None,
                  'gluuEntityId': None,
                  'federationRules': None,
                  'url': None,
                  'gluuRulesAccepted': None,
                  'gluuValidationLog':None,
                  'oxAuthPostLogoutRedirectURI':None
                }

gluuInumMap=    { 'inum': None,
                  'primaryKeyAttrName': None,
                  'primaryKeyValue': None,
                  'secondaryKeyAttrName': None,
                  'secondaryKeyValue': None,
                  'tertiaryKeyAttrName': None,
                  'tertiaryKeyValue': None,
                  'gluuStatus': None
                }

gluuInvoice=    { 'gluuInvoiceNumber': None,
                  'gluuInvoiceDate': None,
                  'gluuInvoiceAmount': None,
                  'gluuInvoiceStatus': None,
                  'gluuInvoiceProductNumber':None,
                  'inum': None,
                  'gluuInvoiceQuantity': None,
                  'gluuInvoiceLineItemName': None
                }

gluuPasswordResetRequest=    { 'oxGuid': None,
                  'personInum': None,
                  'creationDate': None
                }
oxLink=    {      'oxGuid': None,
                  'oxLinkExpirationDate': None,
                  'oxLinkModerated': None,
                  'oxLinkModerators': None,
                  'oxLinkCreator': None,
                  'oxLinkPending': None,
				  'description': None,
				  'oxLinkLinktrack': None
                }

# These are needed by Radiant Logic
vdapcontainer   =  {'ou': None}
vdDirectoryView =  {'o': None}
vdlabel         =  {'o': None}


# These will be used to print schema
customObjectclasses = [('gluuPerson', gluuPerson),
                 ('gluuGroup', gluuGroup),
                 ('gluuOrganization', gluuOrganization),
                 ('gluuAppliance', gluuAppliance),
                 ('gluuAttribute', gluuAttribute),
                 ('gluuSAMLconfig', gluuSAMLconfig),
                 ('gluuInumMap', gluuInumMap),
                 ('gluuInvoice', gluuInvoice),
                 ('gluuPasswordResetRequest', gluuPasswordResetRequest),
                 ('oxLink', oxLink),
                 ('vdapcontainer', vdapcontainer),
                 ('vdDirectoryView', vdDirectoryView),
                 ('vdlabel', vdlabel),
                 ('oxEntry', oxEntry),
                 ('oxNode', oxNode),
				 ('oxAuthClient', oxAuthClient),
				 ('oxAuthCustomScope', oxAuthCustomScope),
				 ('oxAuthFederationRP', oxAuthFederationRP),
				 ('oxAuthFederationOP', oxAuthFederationOP),
				 ('oxAuthFederationMetadata', oxAuthFederationMetadata),
				 ('oxAuthFederationRequest', oxAuthFederationRequest),
				 ('oxAuthFederationTrust', oxAuthFederationTrust),
				 ('oxAuthSessionId', oxAuthSessionId),
				 ('oxAuthConfiguration', oxAuthConfiguration),
				 ('oxTrustConfiguration', oxTrustConfiguration),
				 ('oxAuthUmaResourceSet', oxAuthUmaResourceSet),
				 ('oxAuthUmaScopeDescription', oxAuthUmaScopeDescription),
				 ('oxAuthUmaResourceSetPermission', oxAuthUmaResourceSetPermission),
				 ('oxAuthToken', oxAuthToken),
				 ('oxAuthUmaRPT', oxAuthUmaRPT),
				 ('oxAuthUmaPolicy', oxAuthUmaPolicy),
				 ('oxLiteralNode', oxLiteralNode),
				 ('oxProxConfiguration', oxProxConfiguration),
				 ('oxProxOp', oxProxOp),
				 ('oxProxClient', oxProxClient),
				 ('oxProxAccessToken', oxProxAccessToken),
				 ('oxScript', oxScript),
				 ('oxPushApplication', oxPushApplication),
				 ('oxPushDevice', oxPushDevice)
                 ]

def generateSchema():
    r = ["""dn: cn=schema
objectClass: top
objectClass: ldapSubentry
objectClass: subschema
cn: schema"""]
    attrs = customAttrDict.keys()
    attrs.sort()
    for attrName in attrs:
        attrType = customAttrDict[attrName]['type']
        attrDesc = customAttrDict[attrName]['desc']
        attrTypeDict = schemaDict[attrType]
        s = "attributeTypes: ( %s-oid NAME '%s'" % (attrName, attrName)
        if attrDesc != '': s = s + " DESC '%s'" % attrDesc
        r.append(s)
        schemaKeys = attrTypeDict.keys()
        for schemaKey in schemaKeys:
            r.append("  %s %s" % (schemaKey, attrTypeDict[schemaKey]))
        r.append("  X-ORIGIN 'Gluu created attribute' )")

    for objectclass in customObjectclasses:
        ocName = objectclass[0]
        attrs = objectclass[1].keys()
        attrs.sort()
        firstAttr = attrs[0]
        s = "\n ( %s" % firstAttr
        if unusedAttrs.has_key(firstAttr): del unusedAttrs[firstAttr]
        counter = len(firstAttr)
        for attr in attrs[1:]:
            if unusedAttrs.has_key(attr): del unusedAttrs[attr]
            counter = counter + len(attr)
            s = s + " $ %s" % attr
            if counter > 60:
                    counter = 0
                    s = s + "\n "
        s = s + " ) \n  X-ORIGIN 'Gluu created objectclass' )"
        r.append("objectclasses: ( %s-oid NAME '%s' SUP top STRUCTURAL MUST objectclass MAY %s" % (ocName, ocName, s))
    if len(unusedAttrs):
        for attr in unusedAttrs.keys():
            errors.append("Unused custom attribute: %s" % attr)
    return '\n'.join(r)

def createUserSchema():
    f = open(d['userSchemaTemplateFN'])
    userTemplate = f.read()
    f.close()
    f = open(d['userSchemaFN'], 'w')
    f.write(userTemplate % d)
    f.close()
    return

# Create Schema File
def createSchemaFile() :
    f = open(d['schemaFN'], 'w')
    f.write(generateSchema())
    f.close()

