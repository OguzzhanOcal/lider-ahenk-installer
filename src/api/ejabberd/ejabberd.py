#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import yaml, os
from api.config.config_manager import ConfigManager
from ruamel.yaml import scalarstring

class EjabberInstaller(object):

    def __init__(self, ssh_api, ssh_status):
        self.ssh_api = ssh_api
        self.ssh_status = ssh_status
        self.jabberd_template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/ejabberd_temp.yml')
        self.jabberd_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ejabberd.yml')

    def install(self, data):
        S = scalarstring.DoubleQuotedScalarString
        config_manager = ConfigManager()
        yml_data = config_manager.read_temp_yml_file(self.jabberd_template_path)

        # configuration ejabberd.yml
        base_dn = self.base_dn_parse(data)
        ldap_root_dn = "cn=admin,"+str(base_dn) #cn=admnin,dc=liderahenk,dc=org

        conf_data = {
            'hosts': [S(data['e_hosts'])],
            'ldap_servers': [S(data['ldap_servers'])],
            'ldap_rootdn': S(str(ldap_root_dn)),
            'ldap_password': S(data['l_admin_pwd']),
            'ldap_base': S(str(base_dn)),
            'host_config': {S(data['e_service_name']): {'auth_method': ['internal', 'ldap', 'anonymous']}}
        }
        for attr in conf_data:
            yml_data[attr] = conf_data[attr]

            config_manager.write_to_yml(yml_data, self.jabberd_out_path)
        cfg_data = config_manager.read()
        #run commands of ejabberd
        if self.ssh_status == 1:

            self.ssh_api.run_command(cfg_data["cmd_ejabberd_install"])
            self.ssh_api.scp_file(self.jabberd_out_path, cfg_data["jabberd_des_path"])
            self.ssh_api.run_command(cfg_data["cmd_cp_conf"].format(cfg_data["jabberd_des_path"], cfg_data["jabberd_conf_path"]))
            self.ssh_api.run_command(cfg_data["cmd_register"].format(cfg_data["jabberd_conf_path"], data["e_username"], data["e_service_name"], data["e_user_pwd"]))
            self.ssh_api.run_command(cfg_data["cmd_register"].format(cfg_data["jabberd_conf_path"], data["lider_username"], data["e_service_name"], data["lider_user_pwd"]))
            self.ssh_api.run_command(cfg_data["cmd_jabberd_start"].format(cfg_data["jabberd_conf_path"]))
            self.ssh_api.run_command(cfg_data["cmd_jabberd_status"].format(cfg_data["jabberd_conf_path"]))
        else:
            print("bağlantı sağlanamadığı için kurulum yapılamadı..")

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