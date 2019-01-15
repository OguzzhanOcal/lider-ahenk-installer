#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

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

        ## Ejabberd parameters
        self.ejabberdServiceLabel = QLabel("XMPP Servis Adı:")
        self.e_service_name = QLineEdit()
        self.e_service_name.setPlaceholderText("im.liderahenk.org")
        self.ejabberdAdminLabel = QLabel("XMPP Admin Kullanıcı Adı:")
        self.e_username = QLineEdit()
        self.e_username.setPlaceholderText("admin")
        self.ejabberdAdminPwdLabel = QLabel("XMPP Admin Kullanıcı Parolası:")
        self.e_user_pwd = QLineEdit()
        self.e_user_pwd.setEchoMode(QLineEdit.Password)
        self.e_user_pwd.setPlaceholderText("****")
        self.ejabberdLiderUserLabel = QLabel("XMPP Lider Kullanıcı Adı:")
        self.lider_username = QLineEdit()
        self.lider_username.setPlaceholderText("lider_sunucu")
        self.ejabberdLiderPwdLAbel = QLabel("XMPP Lider Kullanıcı Parolası:")
        self.lider_user_pwd = QLineEdit()
        self.lider_user_pwd.setPlaceholderText("****")
        self.lider_user_pwd.setEchoMode(QLineEdit.Password)
        self.ldapServerLabel = QLabel("LDAP Sunucu Adresi:")
        self.ldap_servers = QLineEdit()
        self.ldap_servers.setPlaceholderText("192.168.*.*")

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

        ## XMPP configuration Layout
        ejabberdGroup = QGroupBox("XMPP Sunucu Konfigürasyon Bilgileri")
        self.ejabberdLayout = QGridLayout()
        self.ejabberdLayout.addWidget(self.ejabberdServiceLabel, 0, 0)
        self.ejabberdLayout.addWidget(self.e_service_name, 0, 1)
        self.ejabberdLayout.addWidget(self.ejabberdAdminLabel, 1, 0)
        self.ejabberdLayout.addWidget(self.e_username, 1, 1)
        self.ejabberdLayout.addWidget(self.ejabberdAdminPwdLabel, 2, 0)
        self.ejabberdLayout.addWidget(self.e_user_pwd, 2, 1)
        self.ejabberdLayout.addWidget(self.ejabberdLiderUserLabel, 3, 0)
        self.ejabberdLayout.addWidget(self.lider_username, 3, 1)
        self.ejabberdLayout.addWidget(self.ejabberdLiderPwdLAbel, 4, 0)
        self.ejabberdLayout.addWidget(self.lider_user_pwd, 4, 1)
        self.ejabberdLayout.addWidget(self.ldapServerLabel, 5, 0)
        self.ejabberdLayout.addWidget(self.ldap_servers, 5, 1)

        ejabberdGroup.setLayout(self.ejabberdLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(ejabberdGroup)
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