#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys, yaml, os, io
from api.config.config_manager import ConfigManager

class MariaDbInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api

    def install(self, data):

        config_manager = ConfigManager()
        cfg_data = config_manager.read()

        self.ssh_api.run_command(cfg_data["cmd_deb_frontend"])
        self.ssh_api.run_command(cfg_data["cmd_pwd"].format(data["password"], data["db_pwd"]))
        self.ssh_api.run_command(cfg_data["cmd_pwd_again"].format(data["password"], data["db_pwd"]))
        self.ssh_api.run_command(cfg_data["cmd_db_install"].format(data["password"]))
        self.ssh_api.run_command(cfg_data["cmd_db_dep"].format(data["password"]))
        self.ssh_api.run_command(cfg_data["cmd_create_db"].format(data["password"], data["db_pwd"]))
        # self.ssh_api.run_command(self.cmd_db_replace_bind_addr.format(data["password"]))
        self.ssh_api.run_command(cfg_data["cmd_db_service"].format(data["password"]))
