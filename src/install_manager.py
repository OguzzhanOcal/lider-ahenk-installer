#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.database.mariadb import MariaDbInstaller
from api.ejabberd.ejabberd import EjabberInstaller
from api.ldap.openldap import OpenLdapInstaller
from api.lider.lider import LiderInstaller
from api.ssh.ssh import Ssh

class InstallManager(object):

    def __init__(self):
        self.ssh = Ssh()

    def install_mariadb(self, data):
        db_installer = MariaDbInstaller(self.ssh)
        db_installer.install(data)

    def install_ejabberd(self, data):
        ejabberd_installer = EjabberInstaller(self.ssh)
        ejabberd_installer.install(data)

    def install_ldap(self, data):
        ldap_installer = OpenLdapInstaller(self.ssh)
        ldap_installer.install(data)

    def install_lider(self, data):
        lider_installer = LiderInstaller(self.ssh)
        lider_installer.install(data)

    def ssh_connect(self, data):
        ssh_status = self.ssh.connect(data["ip"], data["username"], data["password"])
        if ssh_status == 1:
            return True
        else:
            return False

    def ssh_disconnect(self):
        self.ssh.disconnect()
        print("baglantı kapatıldı")

if __name__ == "__main__":

    data = {
        # ssh connection information
        'ip': "server_ip",
        'username': "pardus",
        'password': "1",

        # Database Configuration
        'db_pwd': "secret",
        'db_name': "liderdb",

        # Ejabberd Configuration
        'e_service_name': "im.mys.pardus.org",
        'e_username': "admin",
        'e_user_pwd': "1",
        'e_hosts': "127.0.0.1",
        'ldap_servers': "127.0.0.1",

        # OpenLDAP Configuration
        'l_admin_pwd': "1",
        'l_base_dn': "liderahenk.org",
        'l_config_pwd': "1",
        'l_org_name': "ankara",
        'l_config_admin_dn': "cn=admin,cn=config",
        'l_admin_cn': "admin",
        'ladmin_user': "ladmin",
        'ladmin_pwd': "1",
        'ldap_status': "new",  # yeni ldap kur ya da varolan ldapı konfigüre et 'new' ya da 'conf' parametreleri alıyor

        # Lider Configuration
        'lider_username': "lider_sunucu",
        'lider_user_pwd': "1"
    }

    im = InstallManager()
    im.ssh_connect(data)
    # im.install_mariadb(data)
    im.install_ejabberd(data)
    # im.install_ldap(data)
    # im.install_lider(data)
    im.ssh_disconnect()
