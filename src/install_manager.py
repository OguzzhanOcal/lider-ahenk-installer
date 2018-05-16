#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys
import time
from api.database.mariadb import MariaDbInstaller
from api.ejabberd.ejabberd import EjabberInstaller
from api.ldap.openldap import OpenLdapInstaller
from api.ssh.ssh import Ssh
from ruamel.yaml import scalarstring

class InstallManager(object):

    def __init__(self):
        self.ssh = Ssh()

    def install_mariadb(self, db_data):
        db_installer = MariaDbInstaller(self.ssh)
        db_installer.install(db_data)

    def install_ejabberd(self, ejabberd_data, ejabberd_register_data):
        ejabberd_installer = EjabberInstaller(self.ssh)
        ejabberd_installer.install(ejabberd_data, ejabberd_register_data)

    def install_ldap(self, ldap_data):
        ldap_installer = OpenLdapInstaller(self.ssh)
        ldap_installer.install(ldap_data)

    def ssh_connect(self, ssh_data):
        ssh_status = self.ssh.connect(ssh_data["ip"], ssh_data["username"], ssh_data["password"])
        if ssh_status == 1:
            return True
        else:
            return False
    def ssh_disconnect(self):
        self.ssh.disconnect()
        print("baglantı kapatıldı")

if __name__ == "__main__":
    S = scalarstring.DoubleQuotedScalarString

    ssh_data = {
        'ip': "192.168.56.103",
        'username': "pardus",
        'password': "1"
    }

    db_data = {
        'password': "1",
        'db_pwd': "secret",
        'db_name': "liderdb"
    }
    ejabberd_data = {
        'hosts': [S("localhost")],
        'ldap_servers': [S("ldap.server")],
        'ldap_rootdn': S("cn=admin,dc=mys,dc=pardus,dc=org"),
        'ldap_password': S("secret"),
        'ldap_base': S("dc=mys,dc=pardus,dc=org"),
        'host_config': {S("im.mys.pardus.org"): {'auth_method': ['internal', 'ldap', 'anonymous']}}
    }

    ejabberd_register_data = {
        'service_name': "im.mys.pardus.org",
        'username': "admin",
        'user_pwd': "1"
    }

    ldap_data = {
        'admin_pwd': "1",
        'base_dn': "liderahenk.org",
        'config_pwd': "1",
        'org_name': "ankara",
        'config_admin,dn': "cn=admin,cn=config",
        'admin_cn': "admin",
        'ladmin_user': "ladmin",
        'ladmin_pwd': "1",
        'ldap_status': "new"  # yeni ldap kur ya da varolan ldapı konfigüre et 'new' ya da 'conf' parametreleri alıyor

    }

    im = InstallManager()
    im.ssh_connect(ssh_data)
    # im.install_mariadb(db_data)
    # im.install_ejabberd(ejabberd_data, ejabberd_register_data)
    im.install_ldap(ldap_data)
    im.ssh_disconnect()
