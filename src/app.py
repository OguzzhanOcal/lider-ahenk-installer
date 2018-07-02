#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

# interface management module of the Lider Ahenk Installer application

import json
import os
import sys
from api.logger.installer_logger import Logger
from api.ssh.ssh import Ssh
from install_manager import InstallManager
from gui.installerUi import Ui_Installer
from gui.get_data import GetData
from PyQt5 import QtCore, QtGui, QtWidgets

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

        ## add backround image
        label = QtWidgets.QLabel(self.info)
        pixmap = QtGui.QPixmap('gui/image/liderahenk.png')
        label.setPixmap(pixmap)
        ## set window icon
        self.setWindowIcon(QtGui.QIcon('gui/image/liderahenk-32.png'))
        ## set fixed size
        self.setFixedSize(self.size())
        ## set text Qwizard button (next, back,cancel, finish)
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.NextButton, 'İleri')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.BackButton, 'Geri')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.CancelButton, 'İptal')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.FinishButton, 'Bitti')
        QtWidgets.QWizard.setButtonText(self, QtWidgets.QWizard.HelpButton, 'Yardım' )

        ### Menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menu = self.menubar.addMenu('Lider Ahenk')
        self.open_file_action = QtWidgets.QAction(QtGui.QIcon('gui/image/arrow-up-16.png' ), 'Yükle', self)
        self.open_file_action.setShortcut('Ctrl+O')
        self.open_file_action.triggered.connect(self.open_file)
        self.menu.addAction(self.open_file_action)

        ## Action button
        self.exitButton = QtWidgets.QAction(QtGui.QIcon('gui/image/cancel-16.png' ), 'Çıkış', self)
        self.exitButton.setShortcut('Ctrl+X')
        self.exitButton.triggered.connect(self.close)
        self.menu.addAction(self.exitButton)
        self.save_button.clicked.connect(self.write_file)
        self.ssh_control_button.clicked.connect(self.ssh_control)
        self.next_install_button.clicked.connect(self.install_manager.start_install)

    def open_file(self):
        print("open file dialoggggg")


    def start_install(self):
        with open(self.liderahenk_data_path) as f:
            data = json.load(f)
        self.logger.info("liderahenk.json dosyasından veriler okunuyor")
        # self.ssh_connect(data)
        self.run_gui.set_connect()
        a = GetData.get_data(self)
        self.logger.info(a)

    def ssh_control(self):
        data = GetData.get_data(self)
        ip = self.ip.text()
        username = self.username.text()
        password = self.password.text()
        # bu satırda sunucunun nereye kurulacağı belirleniyor.
        if self.ssh_comboBox.currentIndex() == 1:
            print("1. index seçildi" + str(self.ssh_comboBox.currentIndex()))
        else:
            print("diğer index seçildi" + str(self.ssh_comboBox.currentIndex()))
        if data['ip'] is None:
            print(data['ip'])
            self.message("lütfen zorunlu alanları doldurunuz" )

        ssh_status = self.ssh.connect(ip, username, password)
        print(ssh_status)
        if ssh_status == 1:
            self.message_box("Bağlantı Başarılı. Kuruluma Devam Edebilirsiniz.")
        else:
            msg = "Bağlantı Sağlanamadı. Bağlantı Ayarlarını Kontrol Ederek Daha Sonra Tekrar Deneyiniz!"
            self.message_box(msg)

    def message_box(self, message):
        self.msgBox.setIcon(self.msgBox.Information)
        self.msgBox.setWindowTitle("Bilgilendirme")
        self.msgBox.setInformativeText(_fromUtf8(str(message)))
        self.msgBox.addButton(QtWidgets.QPushButton("Tamam"), QtWidgets.QMessageBox.NoRole)
        # self.msgBox.setDefaultButton(QtWidgets.QMessageBox.Close)
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
            print("data update edildi")
        else:
            with open(self.liderahenk_data_path, 'w') as f:
                json.dump(data, f, ensure_ascii=False)
            print("data oluşturuldu")
            self.logger.info("Lider Ahenk json dosyası oluşturuldu")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    im = GuiManager()
    im.show()
    app.exec_()