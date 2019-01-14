#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget, QRadioButton)

import time


class DatabasePage(QWidget):
    def __init__(self, parent=None):
        super(DatabasePage, self).__init__(parent)

        ## server connect parameters
        self.serverLabel = QLabel("Server:")
        self.serverCombo = QComboBox()
        self.serverCombo.addItem("Uzak Makineye Kur")
        self.serverCombo.addItem("Yerel Makineye Kur")
        self.serverIpLabel = QLabel("Sunucu Bilgisi:")
        self.server_ip = QLineEdit()
        self.usernameLabel = QLabel("Kullanıcı Adı:")
        self.username = QLineEdit()
        self.passwordLabel = QLabel("Kullanıcı Parolası")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.checkControlButton = QPushButton("Bağlantı Kontrol")

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
        self.startQueryButton = QPushButton("Kuruluma Başla")

        ## Database Layout
        dbGroup = QGroupBox("Veritabanı Konfigürasyon Bilgileri")
        dbLayout = QGridLayout()
        dbLayout.addWidget(self.dbNameLabel, 0, 0)
        dbLayout.addWidget(self.db_name, 0, 1)
        dbLayout.addWidget(self.dbUsernameLabel, 1, 0)
        dbLayout.addWidget(self.db_username, 1, 1)
        dbLayout.addWidget(self.dbPwdLabel, 2, 0)
        dbLayout.addWidget(self.db_password, 2, 1)
        dbGroup.setLayout(dbLayout)

        ## Connect Layout
        connectGroup = QGroupBox("Veritabanı Sunucusu Bağlantı Bilgileri")
        connectLayout = QGridLayout()
        connectLayout.addWidget(self.serverLabel, 0, 0)
        connectLayout.addWidget(self.serverCombo, 0, 1)
        connectLayout.addWidget(self.serverIpLabel, 1, 0)
        connectLayout.addWidget(self.server_ip, 1, 1)
        connectLayout.addWidget(self.usernameLabel, 2, 0)
        connectLayout.addWidget(self.username, 2, 1)
        connectLayout.addWidget(self.passwordLabel, 3, 0)
        connectLayout.addWidget(self.password, 3, 1)
        connectLayout.addWidget(self.checkControlButton,4,1)
        connectGroup.setLayout(connectLayout)

        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(dbGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(self.startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

        self.serverCombo.currentIndexChanged.connect(self.check_control_button)

    def check_control_button(self, idx):
        print(idx)
        ## if select location is remote server
        if idx == 0:
            self.checkControlButton.setEnabled(True)
        ## if select location is local server
        else:
            self.checkControlButton.setEnabled(False)





