#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys
import time
from api.database.mariadb import MariaDbInstaller
from api.ssh.ssh import Ssh

class InstallManager(object):

    def __init__(self):
        self.ssh = Ssh()

    def install_mariadb(self, db_data):
        db_installer = MariaDbInstaller(self.ssh)
        db_installer.install(db_data)

    def ssh_connect(self, ssh_data):
        ssh_status = self.ssh.connect(ssh_data["ip"], ssh_data["username"], ssh_data["password"])
        if ssh_status == 1:
            return True
        else:
            return False
    def ssh_disconnect(self):
        self.ssh.disconnect()
        print("baglantı kapatıldı")

if __name__ == "__main__":

    ssh_data = {
        "ip": "127.0.0.1",
        "username": "username",
        "password": "secret"
    }

    db_data = {
        'password': "secret",
        'db_pwd': "secret"
    }
    im = InstallManager()
    im.ssh_connect(ssh_data)
    im.install_mariadb(db_data)
    im.ssh_disconnect()
