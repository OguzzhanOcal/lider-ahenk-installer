#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import paramiko, time
from scp import SCPClient

class Ssh(object):

    def __init__(self):
        self.ssh = None
        self.ip = {}
        self.user_name = "username"
        self.pwd = "password"

    def connect(self, ip):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            ssh_status = self.ssh.connect(hostname=ip, username=self.user_name, password=self.pwd, timeout=10)
            print("ssh connect status --->>>>>>>> " + str(ssh_status))
            if ssh_status is None:
                print("bağlantı başarıyla sağlandı.....")
                ssh_status = 1
                return ssh_status
        except Exception as e:
            print(str(ip) + "bağlantı sağlanamadı : " + str(e))
            # self.writeFile(ip, e)

    def disconnect(self, ip):
        self.ssh.close()
        print(str(ip) + "ip'li makine bağlantı kapatıldı\n---------------")

    def run_command(self, cmd):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            exit_status = stdout.channel.recv_exit_status()
            print(exit_status)
            if exit_status == 0:
                print("komut başarıyla çalıştırıldı...!!")
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

if __name__ == "__main__":

    # test copy file and run command
    ip = "127.0.0.1"
    des_path = "/home/tcolak"
    src_path = "/home/tcolak/server.pem"
    cmd = "ls >> /home/tcolak/liste"
    ssh = Ssh()
    ssh.connect(ip)
    ssh.scp_file(src_path, des_path)
    ssh.run_command(cmd)
    ssh.disconnect(ip)