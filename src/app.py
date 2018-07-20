#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

# interface management module of the Lider Ahenk Installer application

import json
import os
import sys
import subprocess
from api.logger.installer_logger import Logger
from api.ssh.ssh import Ssh
from install_manager import InstallManager
from gui.installerUi import Ui_Installer
# from gui.about import Ui_About
from gui.get_data import GetData
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

try:
    _fromUtf8 = QtCore.QStringListModel.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class GuiManager(QtWidgets.QWizard, Ui_Installer):

    def __init__(self):
        super(GuiManager, self).__init__()
        self.ssh = Ssh()
        self.setupUi(self)
        self.logger = Logger()
        self.get_data = GetData()
        self.msgBox = QtWidgets.QMessageBox()
        self.install_manager = InstallManager()
        self.liderahenk_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/liderahenk.json')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist'))

        ### add backround image
        label = QtWidgets.QLabel(self.info)
        pixmap = QtGui.QPixmap('gui/image/liderahenk.png')
        label.setPixmap(pixmap)
        ### set window icon
        self.setWindowIcon(QtGui.QIcon('gui/image/liderahenk-32.png'))
        ### set fixed size
        self.setFixedSize(self.size())

        ## set background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

        ### set text Qwizard button (next, back,cancel, finish)
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.NextButton, 'İleri')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.BackButton, 'Geri')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.CancelButton, 'İptal')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.FinishButton, 'Bitti')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.HelpButton, 'Yardım')

        ### Menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menu = self.menubar.addMenu('Menü')
        self.open_file_action = QtWidgets.QAction(QtGui.QIcon('gui/image/arrow-up-16.png' ), 'Yükle', self)
        self.open_file_action.setShortcut('Ctrl+O')
        self.open_file_action.triggered.connect(self.open_file)
        self.menu.addAction(self.open_file_action)

        ### Action button
        self.exitButton = QtWidgets.QAction(QtGui.QIcon('gui/image/cancel-16.png'), 'Çıkış', self)
        self.exitButton.setShortcut('Ctrl+X')
        self.exitButton.triggered.connect(self.close)
        self.menu.addAction(self.exitButton)

        ### Abaout button
        self.aboutButton = QtWidgets.QAction('Hakkında', self)
        self.aboutButton.triggered.connect(self.show_about)
        self.menu.addAction(self.aboutButton)

        ### Buttons role
        self.save_button.clicked.connect(self.write_file)
        self.next_install_button.clicked.connect(self.install_manager.start_install)
        self.button_ssh_control.clicked.connect(self.ssh_control)
        self.location.currentIndexChanged.connect(self.location_change)
        self.save_button.clicked.connect(self.save_button_control)

        ## if not patt exists liderahenk.json file set disabled
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/liderahenk.json')):
            self.next_install_button.setDisabled(True)


        if self.location.currentIndex() == 0:
            self.button_ssh_control.setEnabled(False)

    def open_file(self):
        print("open file dialoggggg")
        # self.lider.show()

    def save_button_control(self):
        self.next_install_button.setEnabled(True)

    def location_change(self, idx):
        ## if select location is remote server
        if idx == 1:
            self.server_host.setEnabled(True)
            self.button_ssh_control.setEnabled(True)
        ## if select location is local server
        else:
            self.button_ssh_control.setEnabled(False)


    def abstract(self):
        GetData.server_abstract(self)

    def start_install(self):
        with open(self.liderahenk_data_path) as f:
            data = json.load(f)
        self.logger.info("liderahenk.json dosyasından veriler okunuyor")
        # self.ssh_connect(data)
        a = GetData.get_data(self)
        self.logger.info(a)

    def ssh_control(self):
        ssh_data = {
            'ip': self.server_host.text(),
            'username': self.username.text(),
            'password': self.user_password.text(),
            'location': 'remote'
        }

        # bu satırda sunucunun nereye kurulacağı belirleniyor.
        if self.location.currentIndex() == 1 and ssh_data["ip"] == "" or ssh_data["username"] == "" or ssh_data["password"] == "":
            print(ssh_data['ip'])
            self.message_box("Lütfen sunucu adresini, kullanıcı adını ve parolasını giriniz!" )
        else:
            ssh_status = self.ssh.connect(ssh_data)
            print(ssh_data["ip"])
            print(ssh_status)
            if ssh_status == 1:
                self.message_box("Bağlantı Başarılı. Kuruluma İleri Butonuna Tıklayarak Devam Edebilirsiniz.")
            else:
                msg = "Bağlantı Sağlanamadı. Bağlantı Ayarlarını Kontrol Ederek Daha Sonra Tekrar Deneyiniz!"
                self.message_box(msg)

    def message_box(self, message):
        self.msgBox.setIcon(self.msgBox.Information)
        self.msgBox.setWindowTitle("Bilgilendirme")
        self.msgBox.setInformativeText(_fromUtf8(str(message)))
        self.msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec_()

    def write_file(self):
        data = GetData.get_data(self)
        print(data)

        if os.path.exists(self.liderahenk_data_path) and os.stat(self.liderahenk_data_path).st_size != 0:
            with open(self.liderahenk_data_path) as f:
                read_data = json.load(f)
            read_data.update(data)
            with open(self.liderahenk_data_path, 'w') as f:
                json.dump(read_data, f, ensure_ascii=False)
            self.logger.info("Lider Ahenk json dosyası güncellendi")
            self.message_box("Lider Ahenk json dosyası güncellendi")
        else:
            with open(self.liderahenk_data_path, 'w') as f:
                json.dump(data, f, ensure_ascii=False)
            self.logger.info("Lider Ahenk json dosyası oluşturuldu")
            self.message_box("Lider Ahenk json dosyası oluşturuldu")

    def show_about(self):
        command = "/usr/bin/python3 gui/about_config.py "
        process = subprocess.Popen(command, stdin=None, env=None, cwd=None, stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE, shell=True)
        result_code = process.wait()
        p_out = process.stdout.read().decode("unicode_escape")
        p_err = process.stderr.read().decode("unicode_escape")
        # message = "Lider Ahenk Kurulum Uygulaması \nLider Ahenk sunucu kurulumu için geliştirilmiş kolay kurulum uygulamasıdır. Daha fazla bilgiye http://docs.liderahenk.org/ adresinden ulaşabilirsiniz."
        # self.message_box(message)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    im = GuiManager()
    im.show()
    app.exec_()