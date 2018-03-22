#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.config.config_manager import ConfigManager

class OpenLdapInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api

    def install(self, data, ssh_data):

        config_manager = ConfigManager()
        cfg_data = config_manager.read()
        print("ldap için veriler: "+str(data))
        print("ldap için veriler: " + str(ssh_data))

        self.ssh_api.run_command(cfg_data["ldap_deb_frontend"])
        self.ssh_api.run_command(cfg_data["ldap_debconf_generated_password"].format(ssh_data["password"], data["admin_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_admin_password"].format(ssh_data["password"], data["admin_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_pwd1"].format(ssh_data["password"], data["config_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_pwd2"].format(ssh_data["password"], data["config_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_domain"].format(ssh_data["password"], data["base_dn"]))

        self.ssh_api.run_command(cfg_data["cmd_ldap_install"].format(ssh_data["password"]))








