#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys
# from api.ssh.ssh import Ssh

class MariaDbInstaller(object):

    def __init__(self):
        self.connect = self.Ssh.connect(ip)
        self.run_command = self.Ssh.run_command(cmd)
        self.cmd_deb_frontend = "export DEBIAN_FRONTEND = \"noninteractive\""
        self.cmd_pwd = "sudo debconf-set-selections <<< \"mariadb-server mysql-server/root_password password {0}\""
        self.cmd_pwd_again = "sudo debconf-set-selections <<< \"mariadb-server mysql-server/root_password_again password {0}\""
        self.cmd_db_install = "sudo apt - get install - y mariadb-server"
        self.cmd_create_db = "mysql -uroot -p{0} -e 'CREATE DATABASE liderdb DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci'"
        self.cmd_db_grant_privileges = "mysql -uroot -p{0} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{1}' WITH GRANT OPTION;\""
        self.cmd_db_replace_bind_addr = "sed -i 's/^bind-address/#&/' /etc/mysql/my.cnf"

    def install(self, ip, root_password):
        self.connect(ip)
        print("veritabanı sunucusuna bağlantı kuruldu")
        self.run_command(self.cmd_deb_frontend)
        self.run_command(self.cmd_pwd.format(root_password))
        self.run_command(self.cmd_pwd_again.format(root_password))
        print("veritabanı root parolaları ayarlandı.")
        self.run_command(self.cmd_db_install)
        # self.run_command(self.cmd_create_db.format(root_password))
        self.run_command(self.cmd_db_replace_bind_addr)
        print("ip: "+ip)
        print("----->>> "+self.cmd_pwd.format(root_password))

if __name__ == "__main__":

    ip = "127.0.0.1"
    root_password = "secret"
    data = {
        'ip': ip,
        'root_password': root_password
    }
    db = MariaDbInstaller()
    db.install(ip, root_password)

