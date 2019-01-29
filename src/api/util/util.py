#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import select
import paramiko
import subprocess
import shutil
from api.logger.installer_logger import Logger
from api.util.scp import SCPClient
# from app import GuiManager

class Util(object):

    def __init__(self):
        self.ssh = None
        self.ip = {}
        self.password = None
        self.location = None
        self.logger = Logger()
        # self.gui_manager = GuiManager()

    def connect(self, data):
        self.password = data['password']
        self.location = data['location']
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            ssh_status = self.ssh.connect(hostname=data['ip'], username=data['username'], password=data['password'], pkey=None, timeout=10)

            if ssh_status is None:
                self.logger.info(data['ip'] + " ip'li sunucuya bağlantı başarıyla sağlandı")
                return ssh_status
        except Exception as e:
            self.logger.error(str(data['ip']) + " ip'li sunucuya bağlantı sırasında beklenmedik hata oluştu \n" + str(e))

    def disconnect(self):
        self.ssh.close()
        self.logger.info("Bağlantı kapatıldı")

    def run_command(self, command):
        if self.location == 'remote':
            # run command with sudo user
            try:
                # print(command)
                stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=True)
                stdin.write(self.password + '\n')
                stdin.flush()
                # Wait for the command to terminate
                while not stdout.channel.exit_status_ready():
                    # Only print data if there is data to read in the channel
                    if stdout.channel.recv_ready():
                        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
                        if len(rl) > 0:
                            # Print data from stdout
                            print(stdout.channel.recv(1024))
                result_code = stdout.channel.recv_exit_status()
                self.logger.info(str(command) + " komutu çalıştırıldı")
                return result_code

            except Exception as e:
                self.logger.error(str(command) + " komutu çalıştırılırken hata oluştu! " + str(e))
        # if location local server
        else:
            try:
                echo = subprocess.Popen(['echo', self.password], stdout=subprocess.PIPE,)

                sudo = subprocess.Popen(['sudo', '-S', 'su'], stdin=echo.stdout, stdout=subprocess.PIPE)

                process = subprocess.Popen(command, stdin=None, env=None, cwd=None, stderr=subprocess.PIPE,
                                           stdout=subprocess.PIPE, shell=True)
                result_code = process.wait()
                p_out = process.stdout.read().decode("unicode_escape")
                p_err = process.stderr.read().decode("unicode_escape")

                if result_code == 0:
                    self.logger.info(str(command) + " komutu başarıyla çalıştırıldı")
                else:
                    self.logger.error(str(command) + " komutu çalıştırılırken hata oluştu! " + str(p_err))
                return result_code
            except Exception as e:
                self.logger.error(str(command) + " komutu çalıştırılırken hata oluştu! " + str(e))

    # copy file to remote server with SCPClient method
    def scp_file(self, src_path, des_path):
        if self.location == 'remote':
            try:
                self.scp = SCPClient(self.ssh.get_transport())
                result_code = self.scp.put(src_path, recursive=True, remote_path=des_path)
                print("----------------->>>>>>>>"+str(result_code))
                self.logger.info(str(src_path) + " kaynağının " + str(des_path) + " hedefine başarıyla kopyalandı")
            except Exception as e:
                self.logger.error(str(src_path) + " kaynağının " + str(des_path) + " hedefine kopyalanması sırasında hata oluştu! \n" + str(e))
        else:
            ### copf file to local
            try:
                shutil.copy2(str(src_path), str(des_path))

                self.logger.info(str(src_path) + " kaynağının " + str(des_path) + " hedefine başarıyla kopyalandı")
            except Exception as e:
                self.logger.error("kopyalama yaparken beklenmedik hata oluştu" + str(e))


    def move_file(self, src_path, des_path):
        try:
            shutil.move(src_path, des_path)
        except Exception as e:
            raise