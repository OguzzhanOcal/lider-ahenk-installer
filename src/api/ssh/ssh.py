#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import paramiko, time
from scp import SCPClient

class Ssh(object):

    def __init__(self):
        self.jabberd_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ejabberd.yml')
        self.ssh = None
        self.ip = {}
        self.user_name = username
        self.pwd = pwd

    def ssh_connect(self, ip):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            ssh_status = self.ssh.connect(hostname=ip, username=self.user_name, password=self.pwd, timeout=10)
            print("ssh connect status --->>>>>>>> " + str(ssh_status))
            if ssh_status is None:
                # print("bağlantı başarıyla sağlandı.....")
                ssh_status = 1
                return ssh_status
        except Exception as e:
            print(str(ip) + "bağlantı sağlanamadı : " + str(e))
            self.writeFile(ip, e)



    def ssh_disconnect(self, ip):
        self.ssh.close()
        print(str(ip) + "ip'li makine bağlantı kapatıldı\n---------------")


    def run_command(self, cmd):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print("komut başarıyla çalıştırıldı...!!")
        except Exception as e:
            print ("komut çalışırken hata oluştu: " + str(e))

    def scp_file(self, ip):
        ssh_status = self.ssh_connect(ip)
        if ssh_status == 1:
            try:
                #scp.put('test', recursive=True, remote_path='/home/user/dump')
                self.scp = SCPClient(self.ssh.get_transport())
                self.scp.put(self.jabberd_out_path)
                self.scp.close()
            except Exception as e:
                print("kopyalama veya paket kurulumu yapılamadı: " + str(e) + "\n")