#!/usr/bin/env python

import generateData, configureDS, schema, config, build, deploy, starter, interactive, sys

# Configuration dictionary
d = config.getConfigDir()

# MAIN PROGRAM
d = interactive.collectConfigs(d)

if not d[config.IS_CONFIG_OK]:
    print 'Configuration is invalid, exit OX Platform setup!'
    sys.exit()

# generate ldap schema
if d['generateSchema'] == 'true':
    print 'Start to generate schema...'
    schema.createSchemaFile()
    schema.createUserSchema()
    print 'Finished to generate schema.'

# generate Ldap Data
if d['generateLdapDataLdif'] == 'true':
    print 'Start to generate ldap data...'
    generateData.generateDataLdif()
    print 'Finished to generate ldap data.'

# configure DS with schema and data
if d['configureDS'] == 'true':
    print 'Start to configure Directory Server...'
    configureDS.configureDirectoryServer(d)
    print 'Finished to configure Directory Server.'

if d['buildOX'] == 'true':
    print 'Start to build OX...'
    build.buildOx(d)
    print 'Finished to build OX.'

if d['deployOX'] == 'true':
    print 'Start to deploy OX...'
    deploy.deployOx(d)
    print 'Finished to deploy OX.'

if d['startContainer'] == 'true':
    print 'Start Application Container...'
    starter.start(d)
    print 'Finished to start Application Container.'


