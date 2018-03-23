#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys, paramiko, time
from api.ssh.scp import SCPClient
import select

class Ssh(object):

    def __init__(self):
        self.ssh = None
        self.ip = {}
        self.password = None

    def connect(self, ip, username, password):
        self.password = password
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            ssh_status = self.ssh.connect(hostname=ip, username=username, password=password, timeout=10)
            print("ssh connect status --->>>>>>>> " + str(ssh_status))
            if ssh_status is None:
                print("bağlantı başarıyla sağlandı.....")
                ssh_status = 1
                return ssh_status
        except Exception as e:
            print(str(ip) + "bağlantı sağlanamadı : " + str(e))

    def disconnect(self):
        #ip = self.ssh.ip
        self.ssh.close()

    def run_command(self, cmd):
        # run command with sudo user
        try:
            # print("run command -->>> "+str(cmd))
            print(cmd)
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
        except Exception as e:
            print ("komut çalışırken hata oluştu: " + str(e))

    # copy file with SCPClient method
    def scp_file(self, src_path, des_path):
        try:
            self.scp = SCPClient(self.ssh.get_transport())
            self.scp.put(src_path, recursive=True, remote_path=des_path)
            print("kopyalama tamamlandı")
        except Exception as e:
            print("kopyalama veya paket kurulumu yapılamadı: " + str(e) + "\n")
