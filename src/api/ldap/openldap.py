#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.config.config_manager import ConfigManager

class OpenLdapInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api

    def install(self, data):

        config_manager = ConfigManager()
        cfg_data = config_manager.read()
        print("ldap için veriler: "+str(data))

        self.ssh_api.run_command(cfg_data["ldap_deb_frontend"])
        self.ssh_api.run_command(cfg_data["ldap_debconf_generated_password"].format(data["admin_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_admin_password"].format(data["admin_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_conf"])
        self.ssh_api.run_command(cfg_data["ldap_debconf_domain"].format(data["base_dn"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_organization"].format(data["org_name"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_pwd1"].format(data["admin_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_pwd2"].format(data["admin_pwd"]))
        self.ssh_api.run_command(cfg_data["ldap_debconf_selectdb"])
        self.ssh_api.run_command(cfg_data["ldap_debconf_purgedb"])
        self.ssh_api.run_command(cfg_data["ldap_debconf_movedb"])
        self.ssh_api.run_command(cfg_data["cmd_ldap_install"])
        # self.ssh_api.run_command(cfg_data["cmd_ldap_reconf"])









