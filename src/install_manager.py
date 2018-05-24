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
        self.ssh_status = None

    def install_mariadb(self, data):
        db_installer = MariaDbInstaller(self.ssh, self.ssh_status)
        db_installer.install(data)

    def install_ejabberd(self, data):
        ejabberd_installer = EjabberInstaller(self.ssh, self.ssh_status)
        ejabberd_installer.install(data)

    def install_ldap(self, data):
        ldap_installer = OpenLdapInstaller(self.ssh, self.ssh_status)
        ldap_installer.install(data)

    def install_lider(self, data):
        lider_installer = LiderInstaller(self.ssh, self.ssh_status)
        lider_installer.install(data)

    def ssh_connect(self, data):
        ssh_status = self.ssh.connect(data["ip"], data["username"], data["password"])
        self.ssh_status = ssh_status
        if ssh_status == 1:
            print("---->> "+str(ssh_status))
            return True
        else:
            return False

    def ssh_disconnect(self):
        self.ssh.disconnect()
        print("baglantı kapatıldı")

if __name__ == "__main__":

    data = {
        # ssh connection information
        'ip': "192.168.56.111",
        'username': "tcolak",
        'password': "1",

        # Database Configuration
        'db_name': "liderdb",
        'db_password': "1",

        # Ejabberd Configuration
        'e_service_name': "im.liderahenk.org",
        'e_username': "admin",
        'e_user_pwd': "1222",
        'e_hosts': "im.liderahenk.org",
        'ldap_servers': "192.168.56.111",

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
        'lider_user_pwd': "1",

        #File Server Configuration
        'file_server': "127.0.0.1",
        'fs_username': "lider",
        'fs_username_pwd': "1",
        'fs_plugin_path': '/home/lider',
        "fs_agreement_path": '/home/lider',
        "fs_agent_file_path": '/home/lider',
        
        #Database cfg Configuration
        'db_server': "localhost",
        'db_username': "root"
    }

    im = InstallManager()
    # im.ssh_connect(data)
    # im.install_mariadb(data)
    im.install_ejabberd(data)
    # im.install_ldap(data)
    # im.install_lider(data)
    # im.ssh_disconnect()
