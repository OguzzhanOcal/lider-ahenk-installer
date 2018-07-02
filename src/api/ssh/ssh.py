#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import select
import paramiko
from api.logger.installer_logger import Logger
from api.ssh.scp import SCPClient

class Ssh(object):

    def __init__(self):
        self.ssh = None
        self.ip = {}
        self.password = None
        self.logger = Logger()

    def connect(self, hostname, username, password):
        self.password = password
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            ssh_status = self.ssh.connect(hostname=hostname, username=username, password=password, pkey=None, timeout=10)
            # print("ssh connect status --->>>>>>>> " + str(ssh_status))
            if ssh_status is None:
                # print("bağlantı başarıyla sağlandı.....")
                self.logger.info(str(hostname) + " ip'li sunucuya ssh bağlantısı başarıyla sağlandı")
                ssh_status = 1
                return ssh_status
        except Exception as e:
            pass
            self.logger.error(str(hostname) + " ip'li sunucuya ssh bağlantısı sırasında beklenmedik hata oluştu \n" + str(e))

    def disconnect(self):
        #ip = self.ssh.ip
        self.ssh.close()
        self.logger.info("Bağlantı kapatıldı")

    def run_command(self, cmd):
        # run command with sudo user
        try:
            # print(cmd)
            stdin, stdout, stderr = self.ssh.exec_command(cmd, get_pty=True)
            stdin.write(self.password + '\n')
            stdin.flush()

            # Wait for the command to terminate
            while not stdout.channel.exit_status_ready():
                # Only print data if there is data to read in the channel
                if stdout.channel.recv_ready():
                    rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
                    if len(rl) > 0:
                        # Print data from stdout
                        print (stdout.channel.recv(1024))
                        # self.logger.info(str(cmd) + " Komutu başarıyla çalıştırıldı")
            self.logger.info(str(cmd) + " komutu başarıyla çalıştırıldı")
        except Exception as e:
            self.logger.error(str(cmd) + " komutu çalıştırılırken hata oluştu! " + str(e))

    # copy file with SCPClient method
    def scp_file(self, src_path, des_path):
        try:
            self.scp = SCPClient(self.ssh.get_transport())
            self.scp.put(src_path, recursive=True, remote_path=des_path)
            self.logger.info(str(src_path) + " kaynağının " + str(des_path) + " hedefine başarıyla kopyalandı")
        except Exception as e:
            self.logger.error(str(src_path) + " kaynağının " + str(des_path) + " hedefine kopyalanması sırasında hata oluştu! \n" + str(e))
