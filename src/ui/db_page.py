#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget, QRadioButton)
import json
import os
from ui.connect_page import ConnectPage
from install_manager import InstallManager


class DatabasePage(QWidget):
    def __init__(self, parent=None):
        super(DatabasePage, self).__init__(parent)
        self.liderdb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist/liderdb.json')
        # self.log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/installer.log')
        # self.log_backup_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/installer.log.{0}')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist'))

        self.connect_layout = ConnectPage()
        self.im = InstallManager()

        ## database parameters
        self.dbNameLabel = QLabel("Veritabanı Adı:")
        self.db_name = QLineEdit()
        self.db_name.setPlaceholderText("liderdb")
        self.dbUsernameLabel = QLabel("Veritabanı Kullanıcı Adı:")
        self.db_username = QLineEdit()
        self.db_username.setPlaceholderText("root")
        self.dbPwdLabel = QLabel("Veritabanı Kullanıcı Parolası:")
        self.db_password = QLineEdit()
        self.db_password.setEchoMode(QLineEdit.Password)
        self.db_password.setPlaceholderText("****")
        self.startUpdateButton = QPushButton("Kurulumu Başla")

        ## Database Layout
        dbGroup = QGroupBox("Veritabanı Konfigürasyon Bilgileri")
        self.dbLayout = QGridLayout()
        self.dbLayout.addWidget(self.dbNameLabel, 0, 0)
        self.dbLayout.addWidget(self.db_name, 0, 1)
        self.dbLayout.addWidget(self.dbUsernameLabel, 1, 0)
        self.dbLayout.addWidget(self.db_username, 1, 1)
        self.dbLayout.addWidget(self.dbPwdLabel, 2, 0)
        self.dbLayout.addWidget(self.db_password, 2, 1)
        dbGroup.setLayout(self.dbLayout)

        connectGroup = QGroupBox("Veritabanı Sunucusu Bağlantı Bilgileri")
        connectGroup.setLayout(self.connect_layout.connectLayout)

        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(dbGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(self.startUpdateButton)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        self.startUpdateButton.clicked.connect(self.save_db_data)

    def save_db_data(self):

        if self.connect_layout.serverCombo.currentIndex() == 0:
            location_server = 'remote'
        else:
            location_server = 'local'

        data = {
            'location': location_server,

            # Server Configuration
            'ip': self.connect_layout.server_ip.text(),
            'username': self.connect_layout.username.text(),
            'password': self.connect_layout.password.text(),
            # Database Configuration
            'db_server': self.connect_layout.server_ip.text(),
            'db_name': self.db_name.text(),
            'db_username': self.db_username.text(),
            'db_password': self.db_password.text(),

        }
        print(data)

        if os.path.exists(self.liderdb_path) and os.stat(self.liderdb_path).st_size != 0:
            with open(self.liderdb_path) as f:
                read_data = json.load(f)
            read_data.update(data)
            with open(self.liderdb_path, 'w') as f:
                json.dump(read_data, f, ensure_ascii=False)
            print('Lider Ahenk json dosyası güncellendi')
            # self.logger.info("Lider Ahenk json dosyası güncellendi")
            # self.message_box("Lider Ahenk json dosyası güncellendi")
        else:
            with open(self.liderdb_path, 'w') as f:
                json.dump(data, f, ensure_ascii=False)
                print("Lider Ahenk json dosyası oluşturuldu")
            # self.logger.info("Lider Ahenk json dosyası oluşturuldu")
            # self.message_box("Lider Ahenk json dosyası oluşturuldu")

        self.im.ssh_connect(data)
        self.im.install_mariadb(data)
        self.im.ssh_disconnect()






