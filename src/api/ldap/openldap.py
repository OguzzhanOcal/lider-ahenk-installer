#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.config.config_manager import ConfigManager
import os

class OpenLdapInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api
        self.ldapconfig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/ldapconfig_temp')
        self.liderahenk_ldif_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/liderahenk.ldif')
        self.ldapconfig_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ldapconfig')

    def install(self, data):

        config_manager = ConfigManager()
        cfg_data = config_manager.read()
        print("ldap için veriler: "+str(data))

        ### gelen  data['base_dn']: liderahenk.org #BASECN ve #BASEDN için split edildi
        parse_dn = data["base_dn"].split('.')
        base_cn = parse_dn[0]

        dn_list = []
        for dn in parse_dn:
            message = 'dc='+str(dn)+','
            dn_list.append(message)
        base_dn = ''.join(str(x) for x in dn_list)
        base_dn = base_dn.strip(',')
        ###base_dn=dc=liderahenk,dc=org

        #edit ldapconfig_temp script
        self.f1 = open(self.ldapconfig_path, 'r+')
        my_text = self.f1.read()
        ldap_data = {
            "#BASEDN": base_dn,
            "#CNAME": data["base_dn"],
            "#BASECN": base_cn,
            "#ORGANIZATION": data["org_name"],
            "#ADMINCN": "cn=admin",
            "#ADMINPASSWD": data["admin_pwd"],
            "#CNCONFIGADMINDN": "cn=admin,cn=config",
            "#CNCONFIGADMINPASSWD": data["config_pwd"],
            "#LIDERCONSOLEUSER": data["ladmin_user"],
            "#LIDERCONSOLEPWD": data["ladmin_pwd"]
        }
        txt = config_manager.replace_all(my_text, ldap_data)
        self.f2 = open(self.ldapconfig_out_path, 'w+')
        self.f2.write(txt)
        self.f1.close()
        self.f2.close()
        #copy ldapconfig_temp script and liderahenk.ldif to ldap server
        self.ssh_api.scp_file(self.ldapconfig_out_path, '/tmp')
        self.ssh_api.scp_file(self.liderahenk_ldif_path, '/tmp')

        ### install slapd package
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
        self.ssh_api.run_command(cfg_data["cmd_ldap_reconf"])
        self.ssh_api.run_command(cfg_data["cmd_ldapconfig_execute"])
        self.ssh_api.run_command(cfg_data["cmd_ldapconfig_run"])
