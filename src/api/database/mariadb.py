#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.config.config_manager import ConfigManager

class MariaDbInstaller(object):

    def __init__(self, ssh_api, ssh_status):
        self.ssh_api = ssh_api
        self.ssh_status = ssh_status

    def install(self, data):

        config_manager = ConfigManager()
        cfg_data = config_manager.read()
        # print(cfg_data)
        if self.ssh_status == 1:
            self.ssh_api.run_command(cfg_data["cmd_liderahenk_repo_key"])
            self.ssh_api.run_command(cfg_data["cmd_liderahenk_repo_add"])
            self.ssh_api.run_command(cfg_data["cmd_update"])
            self.ssh_api.run_command(cfg_data["cmd_deb_frontend"])
            self.ssh_api.run_command(cfg_data["db_debconf_pwd"].format(data["db_password"]))
            self.ssh_api.run_command(cfg_data["db_debconf_pwd_again"].format(data["db_password"]))
            self.ssh_api.run_command(cfg_data["cmd_db_install"])
            self.ssh_api.run_command(cfg_data["cmd_db_dep"])
            self.ssh_api.run_command(cfg_data["cmd_create_db"].format(data["db_password"], data["db_name"]))
            self.ssh_api.run_command(cfg_data["cmd_db_grant_privileges"])
            # self.ssh_api.run_command(cfg_data["cmd_db_replace_bind_addr"])
            self.ssh_api.run_command(cfg_data["cmd_db_service"])
        else:
            print("bağlantı sağlanamadığı için kurulum yapılamadı..")
