#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from PyQt5.QtWidgets import (QComboBox, QGridLayout, QGroupBox, QLabel, QLineEdit,
                             QPushButton, QWidget)
from install_manager import InstallManager
from api.util.util import Util
from ui.message_box.message_box import MessageBox


class ConnectPage(QWidget):
    def __init__(self, parent=None):
        super(ConnectPage, self).__init__(parent)

        # self.log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/installer.log')
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))
        self.im = InstallManager()
        self.util = Util()
        # self.app = ConfigDialog()
        self.msgBox = MessageBox()

        ## server connect parameters
        self.serverLabel = QLabel("Sunucu:")
        self.serverCombo = QComboBox()
        self.serverCombo.addItem("Uzak Makineye Kur")
        self.serverCombo.addItem("Yerel Makineye Kur")
        self.serverIpLabel = QLabel("Sunucu Adresi:")
        self.server_ip = QLineEdit()
        self.server_ip.setPlaceholderText("192.168.*.*")
        self.usernameLabel = QLabel("Kullanıcı Adı:")
        self.username = QLineEdit()
        self.username.setPlaceholderText("lider")
        self.passwordLabel = QLabel("Kullanıcı Parolası:")
        self.password = QLineEdit()
        self.password.setPlaceholderText("****")
        self.password.setEchoMode(QLineEdit.Password)
        self.checkControlButton = QPushButton("Bağlantı Kontrol")

        ## Connect Layout
        self.connectGroup = QGroupBox("Veritabanı Sunucusu Bağlantı Bilgileri")
        self.connectLayout = QGridLayout()
        self.connectLayout.addWidget(self.serverLabel, 0, 0)
        self.connectLayout.addWidget(self.serverCombo, 0, 1)
        self.connectLayout.addWidget(self.serverIpLabel, 1, 0)
        self.connectLayout.addWidget(self.server_ip, 1, 1)
        self.connectLayout.addWidget(self.usernameLabel, 2, 0)
        self.connectLayout.addWidget(self.username, 2, 1)
        self.connectLayout.addWidget(self.passwordLabel, 3, 0)
        self.connectLayout.addWidget(self.password, 3, 1)
        self.connectLayout.addWidget(self.checkControlButton, 5, 0)
        self.connectGroup.setLayout(self.connectLayout)

        # mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.connectGroup)
        # mainLayout.addSpacing(12)
        # mainLayout.addStretch(1)
        # self.setLayout(mainLayout)

        self.serverCombo.currentIndexChanged.connect(self.check_control_button)
        self.checkControlButton.clicked.connect(self.ssh_control)


    def check_control_button(self, idx):
        ## if select location is remote server
        if idx == 0:
            self.server_ip.setText("")
        else:
            self.server_ip.setText("127.0.0.1")

    def ssh_control(self):

        if self.serverCombo.currentIndex() == 0:
            location_server = 'remote'
        else:
            location_server = 'local'

        data = {

            'location': location_server,
            # Server Configuration
            'ip': self.server_ip.text(),
            'username': self.username.text(),
            'password': self.password.text(),
        }

        if self.serverCombo.currentIndex() == 1 and data["ip"] == "" or data["username"] == "" or data["password"] == "":
            self.msgBox.warning("Lütfen sunucu adresini, kullanıcı adını ve parolasını giriniz!")

        else:
            ssh_status = self.im.ssh_connect(data)
            if ssh_status is True:
                self.msgBox.information("Bağlantı Başarılı. Kuruluma Devam Edebilirsiniz.")
            else:
                msg = "Bağlantı Sağlanamadı. Bağlantı Ayarlarını Kontrol Ederek Daha Sonra Tekrar Deneyiniz!\n"
                self.msgBox.information(msg)









