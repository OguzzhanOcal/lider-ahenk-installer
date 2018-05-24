#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.config.config_manager import ConfigManager
import os


class LiderInstaller(object):

    def __init__(self, ssh_api, ssh_status):
        self.ssh_api = ssh_api
        self.ssh_status = ssh_status
        self.config_manager = ConfigManager()
        self.lider_conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/tr.org.liderahenk.cfg')
        self.db_conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/tr.org.liderahenk.datasource.cfg')
        self.lider_conf_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/tr.org.liderahenk.cfg')
        self.db_conf_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/tr.org.liderahenk.datasource.cfg' )

    def install(self, data):

        if self.ssh_status == 1:
            print("ssh bağlatı durumu: "+str(self.ssh_status))
            cfg_data = self.config_manager.read()
            self.configure_lider_cfg(data)
            self.configure_db_cfg(data)
            # self.ssh_api.run_command(cfg_data["cmd_liderahenk_repo_key"])
            # self.ssh_api.run_command(cfg_data["cmd_liderahenk_repo_add"])
            self.ssh_api.run_command(cfg_data["cmd_update"])
            self.ssh_api.run_command(cfg_data["cmd_lider_install"])
            self.ssh_api.scp_file(self.lider_conf_out_path, cfg_data["lider_des_path"])
            self.ssh_api.scp_file(self.db_conf_out_path, cfg_data["lider_des_path"])
            self.ssh_api.run_command(cfg_data["cmd_cp_lider_cfg"])
            self.ssh_api.run_command(cfg_data["cmd_cp_db_cfg"])
            self.ssh_api.run_command(cfg_data["cmd_lider_service"])
        else:
            print("bağlantı sağlanamadığı için kurulum yapılamadı..")

    def configure_lider_cfg(self, data):
        l_base_dn = self.base_dn_parse(data)
        l_admin_dn = "cn=admin,"+str(l_base_dn)

        lider_data = {
            "#LDAP_SERVER": data['ldap_servers'],
            "#LDAP_ADMIN_DN": l_admin_dn,
            "#LDAP_ADMIN_PWD": data['l_admin_pwd'],
            "#LDAP_ROOT_DN": l_base_dn,
            "#XMPP_SERVER": data['e_hosts'],
            "#LIDER_USERNAME": data['lider_username'],
            "#XMPP_USER_PWD": data['lider_user_pwd'],
            "#XMPP_SERVICE_NAME": data['e_service_name'],
            "#LDAP_BASE_DN": l_base_dn,
            "#FILE_SERVER": data['file_server'],
            "#FS_USERNAME": data['fs_username'],
            "#FS_PASSWORD": data['fs_username_pwd'],
            "#PLUGIN_PATH": data['fs_plugin_path'],
            "#AGREEMENT_PATH": data['fs_agreement_path'],
            "#AGENT_FILE_PATH": data['fs_agent_file_path']
        }

        self.f_lider = open(self.lider_conf_path, 'r+')
        lider_text = self.f_lider.read()

        txt = self.config_manager.replace_all(lider_text, lider_data)
        self.f_lider_out = open(self.lider_conf_out_path, 'w+')
        self.f_lider_out.write(txt)
        self.f_lider.close()
        self.f_lider_out.close()

    def configure_db_cfg(self, data):
        db_data = {
            "#DBADDRESS": data['db_server'],
            "#DBDATABASE": data['db_name'],
            "#DBUSERNAME": data['db_username'],
            "#DBPASSWORD": data['db_password']
        }
        self.f_db = open(self.db_conf_path, 'r+')
        db_text = self.f_db.read()
        txt = self.config_manager.replace_all(db_text, db_data)
        self.f_db_out = open(self.db_conf_out_path, 'w+')
        self.f_db_out.write(txt)
        self.f_db.close()
        self.f_db_out.close()

    def base_dn_parse(self, data):
        ### split for get data['base_dn']: liderahenk.org #BASECN and #BASEDN
        parse_dn = data["l_base_dn"].split('.')
        dn_list = []
        for dn in parse_dn:
            message = 'dc=' + str(dn) + ','
            dn_list.append(message)
        base_dn = ''.join(str(x) for x in dn_list)
        base_dn = base_dn.strip(',')
        return base_dn
