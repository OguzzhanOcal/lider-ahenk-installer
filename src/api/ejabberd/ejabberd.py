#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import yaml, os
from api.config.config_manager import ConfigManager

class EjabberInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api
        self.jabberd_template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/ejabberd_temp.yml')
        self.jabberd_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ejabberd.yml')

    def install(self, data, register_data, ssh_data):

        config_manager = ConfigManager()
        yml_data = config_manager.read_temp_yml_file(self.jabberd_template_path)

        for attr in data:
            yml_data[attr] = data[attr]

        config_manager.write_to_yml(yml_data, self.jabberd_out_path)
        cfg_data = config_manager.read()
        # self.ssh_api.run_command(cfg_data["cmd_ejabberd_install"].format(user_data["user_pwd"]))
        # self.ssh_api.scp_file(cfg_data["jabberd_out_path"], cfg_data["jabberd_des_path"])
        # self.ssh_api.run_command(cfg_data["cmd_cp_conf"].format(ssh_data["password"]))
        # self.ssh_api.run_command(cfg_data["cmd_register"].format(data["password"], register_data["username"], register_data["service_name"], register_data["user_pwd"]))