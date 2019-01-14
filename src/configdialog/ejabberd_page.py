#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget)

class EjabberdPage(QWidget):
    def __init__(self, parent=None):
        super(EjabberdPage, self).__init__(parent)

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
        self.checkControlButton = QPushButton("Bağlantı Kontrol")

        ## Ejabberd parameters

       ## Connect Layout
        connectGroup = QGroupBox("XMPP Sunucusu Bağlantı Bilgileri")
        connectLayout = QGridLayout()
        connectLayout.addWidget(self.serverLabel, 0, 0)
        connectLayout.addWidget(self.serverCombo, 0, 1)
        connectLayout.addWidget(self.serverIpLabel, 1, 0)
        connectLayout.addWidget(self.server_ip, 1, 1)
        connectLayout.addWidget(self.usernameLabel, 2, 0)
        connectLayout.addWidget(self.username, 2, 1)
        connectLayout.addWidget(self.passwordLabel, 3, 0)
        connectLayout.addWidget(self.password, 3, 1)
        connectLayout.addWidget(self.checkControlButton, 4, 1)
        connectGroup.setLayout(connectLayout)
        configGroup = QGroupBox("XMPP Sunucu Konfigürasyon Bilgileri")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(configGroup)
        mainLayout.addSpacing(12)
        # mainLayout.addWidget(self.checkControlButton)
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