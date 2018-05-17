#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.config.config_manager import ConfigManager
import os

class OpenLdapInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api
        self.ldap_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/ldapconfig_temp')
        self.update_ldap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/update_ldap_temp')
        self.liderahenk_ldif_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/liderahenk.ldif')
        self.ldap_config_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ldapconfig')
        self.update_ldap_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/update_ldap')

    def install(self, data):

        config_manager = ConfigManager()
        cfg_data = config_manager.read()

        base_dn = self.base_dn_parse(data)
        l_admin_cn = "cn="+str(data['l_admin_cn'])

        ldap_data = {
            "#BASEDN": base_dn[0],
            "#CNAME": data["l_base_dn"],
            "#BASECN": base_dn[1],
            "#ORGANIZATION": data["l_org_name"],
            "#ADMINCN": l_admin_cn,
            "#ADMINPASSWD": data["l_admin_pwd"],
            "#CNCONFIGADMINDN": data['l_config_admin_dn'],
            "#CNCONFIGADMINPASSWD": data["l_config_pwd"],
            "#LIDERCONSOLEUSER": data["ladmin_user"],
            "#LIDERCONSOLEPWD": data["ladmin_pwd"]
        }

        # copy liderahenk.ldif file to ldap server
        self.ssh_api.scp_file(self.liderahenk_ldif_path, '/tmp')

        if data["ldap_status"] == "new":

            #edit ldap_install_temp script
            self.f1 = open(self.ldap_config_path, 'r+')
            my_text = self.f1.read()

            txt = config_manager.replace_all(my_text, ldap_data)
            self.f2 = open(self.ldap_config_out_path, 'w+')
            self.f2.write(txt)
            self.f1.close()
            self.f2.close()

            #copy ldap_install  script to ldap server
            self.ssh_api.scp_file(self.ldap_config_out_path, '/tmp')

            ### install slapd package
            self.ssh_api.run_command(cfg_data["ldap_deb_frontend"])
            self.ssh_api.run_command(cfg_data["ldap_debconf_generated_password"].format(data["l_admin_pwd"]))
            self.ssh_api.run_command(cfg_data["ldap_debconf_admin_password"].format(data["l_admin_pwd"]))
            self.ssh_api.run_command(cfg_data["ldap_debconf_conf"])
            self.ssh_api.run_command(cfg_data["ldap_debconf_domain"].format(data["l_base_dn"]))
            self.ssh_api.run_command(cfg_data["ldap_debconf_organization"].format(data["l_org_name"]))
            self.ssh_api.run_command(cfg_data["ldap_debconf_pwd1"].format(data["l_admin_pwd"]))
            self.ssh_api.run_command(cfg_data["ldap_debconf_pwd2"].format(data["l_admin_pwd"]))
            self.ssh_api.run_command(cfg_data["ldap_debconf_selectdb"])
            self.ssh_api.run_command(cfg_data["ldap_debconf_purgedb"])
            self.ssh_api.run_command(cfg_data["ldap_debconf_movedb"])
            self.ssh_api.run_command(cfg_data["cmd_ldap_install"])
            self.ssh_api.run_command(cfg_data["cmd_ldap_reconf"])
            self.ssh_api.run_command(cfg_data["cmd_ldapconfig_execute"])
            self.ssh_api.run_command(cfg_data["cmd_ldapconfig_run"])
            print ("yeni ldap kurulumu tamamlandı.....")

        else:
            self.f1 = open(self.update_ldap_path, 'r+')
            my_text = self.f1.read()
            txt = config_manager.replace_all(my_text, ldap_data)
            self.f2 = open(self.update_ldap_out_path, 'w+')
            self.f2.write(txt)
            self.f1.close()
            self.f2.close()
            # copy ldap_config  script to ldap server
            self.ssh_api.scp_file(self.update_ldap_out_path, '/tmp')
            self.ssh_api.run_command(cfg_data["cmd_update_ldap_execute"])
            self.ssh_api.run_command(cfg_data["cmd_update_ldap_run"])
            print("varolan ldap konfigüre edildi.")

    def base_dn_parse(self, data):
        ### split for get data['base_dn']: liderahenk.org #BASECN and #BASEDN
        parse_dn = data["l_base_dn"].split('.')
        base_cn = parse_dn[0]
        dn_list = []
        for dn in parse_dn:
            message = 'dc=' + str(dn) + ','
            dn_list.append(message)
        base_dn = ''.join(str(x) for x in dn_list)
        base_dn = base_dn.strip(',')
        return base_dn, base_cn