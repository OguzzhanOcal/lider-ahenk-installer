#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget, QRadioButton)
from ui.ldap_page import OpenLDAPPage
from ui.ejabberd_page import EjabberdPage
from ui.db_page import DatabasePage

class LiderPage(QWidget):
    def __init__(self, parent=None):
        super(LiderPage, self).__init__(parent)

        self.ldap_layout = OpenLDAPPage()
        self.ejabberd_layout = EjabberdPage()
        self.db_layout = DatabasePage()

        ## server connect parameters
        self.serverLabel = QLabel("Sunucu:")
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

        ## lider parameters
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
        liderLdapGroup = QGroupBox("LDAP Konfigürasyon Bilgileri")
        liderXmppGroup = QGroupBox("XMPP Konfigürasyon Bilgileri")
        liderDbGroup = QGroupBox("Veritabanı Konfigürasyon Bilgileri")

        liderLdapGroup.setLayout(self.ldap_layout.ldapLayout)
        liderXmppGroup.setLayout(self.ejabberd_layout.ejabberdLayout)
        liderDbGroup.setLayout(self.db_layout.dbLayout)

        ## Connect Layout
        connectGroup = QGroupBox("Lİder Sunucusu Bağlantı Bilgileri")
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

        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(liderLdapGroup)
        mainLayout.addWidget(liderXmppGroup)
        mainLayout.addWidget(liderDbGroup)
        # mainLayout.addSpacing(12)
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





