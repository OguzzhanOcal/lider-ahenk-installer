#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys, os

class MariaDbInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api

        self.cmd_deb_frontend = "export DEBIAN_FRONTEND=\"noninteractive\""
        self.cmd_pwd = "echo {0} | sudo -S debconf-set-selections <<< \"mariadb-server mysql-server/root_password password {1}\""
        self.cmd_pwd_again = "echo {0} | sudo -S debconf-set-selections <<< \"mariadb-server mysql-server/root_password_again password {1}\""
        self.cmd_db_install = "echo {0} | sudo -S apt install -y mariadb-server"
        self.cmd_db_dep = "echo {0} | sudo -S apt -f install"
        self.cmd_create_db = "echo {0} | sudo -S mysql -uroot -p{1} -e \'CREATE DATABASE liderdb DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci\'"
        self.cmd_db_grant_privileges = "mysql -uroot -p{0} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{1}' WITH GRANT OPTION;\""
        self.cmd_db_replace_bind_addr = "echo {0} | sudo -S sed -i 's/^bind-address/#&/' /etc/mysql/my.cnf"
        self.cmd_db_service = "echo {0} | sudo -S systemctl restart mysql.service"

    def install(self, data):
        print("veritabanı root parolası: "+str(data["db_pwd"]))
        print("sudo yetkili kullanıcı parolası: "+str(data["password"]))
        print(self.cmd_deb_frontend)
        self.ssh_api.run_command(self.cmd_deb_frontend)
        print(self.cmd_pwd.format(data["password"], data["db_pwd"]))
        self.ssh_api.run_command(self.cmd_pwd.format(data["password"], data["db_pwd"]))
        print(self.cmd_pwd_again.format(data["password"], data["db_pwd"]))
        self.ssh_api.run_command(self.cmd_pwd_again.format(data["password"], data["db_pwd"]))
        print(self.cmd_db_install.format(data["password"]))
        self.ssh_api.run_command(self.cmd_db_install.format(data["password"]))
        print(self.cmd_db_dep.format(data["password"]))
        self.ssh_api.run_command(self.cmd_db_dep.format(data["password"]))
        print(self.cmd_create_db.format(data["password"]), data["db_pwd"])
        self.ssh_api.run_command(self.cmd_create_db.format(data["password"], data["db_pwd"]))
        # self.ssh_api.run_command(self.cmd_db_replace_bind_addr.format(data["password"]))
        print(self.cmd_db_service.format(data["password"]))
        self.ssh_api.run_command(self.cmd_db_service.format(data["password"]))
