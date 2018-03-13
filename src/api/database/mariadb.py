#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys
from api.ssh.ssh import Ssh

class MariaDbInstaller(object):

    def __init__(self):
        self.connect = self.Ssh.connect(ip)
        self.run_command = self.Ssh.run_command(cmd)
        # cmd_deb_frontend = "export DEBIAN_FRONTEND = \"noninteractive"\"
        # cmd_pwd = "sudo debconf - set - selections << < \"mariadb-server mysql-server/root_password password $PASSWORD\""
        # cmd_pwd_again = "sudo debconf - set - selections << < \"mariadb-server mysql-server/root_password_again password $PASSWORD\""
        # cmd_db_install = "sudo apt - get install - y mariadb-server"
        # cmd_create_db = "mysql -uroot -p{0} -e 'CREATE DATABASE liderdb DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci'"
        # cmd_db_grant_privileges = "mysql -uroot -p{0} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{1}' WITH GRANT OPTION;\""
        # cmd_db_replace_bind_addr = "sed -i 's/^bind-address/#&/' /etc/mysql/my.cnf"

    def install(self, ip):
        self.connect(ip)
        print("veritabanı sunucusuna bağlantı kuruldu")
        self.run_command("mkdir /home/tcolak/db_file.txt")


if __name__ == "__main__":
    ip = "127.0.0.1"
    cmd_pwd = "secret"
    cmd_pwd_again = "secret"
    db = MariaDbInstaller()
    # db.install(ip, cmd_pwd, cmd_pwd_again)
    db.install(ip)
