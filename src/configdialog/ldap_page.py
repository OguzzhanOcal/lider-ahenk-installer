#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget)

class OpenLDAPPage(QWidget):
    def __init__(self, parent=None):
        super(OpenLDAPPage, self).__init__(parent)

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

        #OpenLDAP parameters
        self.ldapStatusLabel = QLabel("LDAP İçin İşlem Seçiniz:")
        self.ldapStatusCombo = QComboBox()
        self.ldapStatusCombo.addItem("OpenLDAP Kur")
        self.ldapStatusCombo.addItem("OpenLDAP Güncelle")
        self.ldapAdminLabel = QLabel("LDAP Admin:")
        self.ldap_admin = QLineEdit()
        self.ldapAdminPwdLabel = QLabel("Ldap Admin Parolası:")
        self.ldap_admin_pwd = QLineEdit()
        self.ldap_admin_pwd.setPlaceholderText("****")
        self.ldap_admin_pwd.setEchoMode(QLineEdit.Password)
        self.ldapBaseDnLabel = QLabel("LDAP Base DN:")
        self.ldap_base_dn = QLineEdit()
        self.ldap_base_dn.setPlaceholderText("liderahenk.org")
        self.ldapConfigPwdLabel = QLabel("LDAP config Kullanıcı Parolası:")
        self.l_config_pwd = QLineEdit()
        self.l_config_pwd.setPlaceholderText("****")
        self.l_config_pwd.setEchoMode(QLineEdit.Password)
        self.ladminLabel = QLabel("Lider Arayüz Kullanıcı Adı:")
        self.ladmin_user = QLineEdit()
        self.ladmin_user.setPlaceholderText("lider_console")
        self.ladminPwdLabel = QLabel("Lider Arayüz Kullanıcı Parolası:")
        self.ladmin_pwd = QLineEdit()
        self.ladmin_pwd.setPlaceholderText("****")
        self.ladmin_pwd.setEchoMode(QLineEdit.Password)

        startUpdateButton = QPushButton("Kurulumu Başla")

        ## Connect Layout
        connectGroup = QGroupBox("OpenLDAP Sunucusu Bağlantı Bilgileri")
        connectLayout = QGridLayout()
        connectLayout.addWidget(self.serverLabel,0,0)
        connectLayout.addWidget(self.serverCombo,0,1)
        connectLayout.addWidget(self.serverIpLabel,1,0)
        connectLayout.addWidget(self.server_ip,1,1)
        connectLayout.addWidget(self.usernameLabel,2,0)
        connectLayout.addWidget(self.username,2,1)
        connectLayout.addWidget(self.passwordLabel,3,0)
        connectLayout.addWidget(self.password,3,1)
        connectLayout.addWidget(self.checkControlButton, 4, 1)
        connectGroup.setLayout(connectLayout)

        ## LDAP configuration Layout
        ldapGroup = QGroupBox("OpenLDAP Konfigürasyon Bilgileri")
        ldapLayout = QGridLayout()
        ldapLayout.addWidget(self.ldapStatusLabel, 0, 0)
        ldapLayout.addWidget(self.ldapStatusCombo, 0, 1)
        ldapLayout.addWidget(self.ldapBaseDnLabel, 1, 0)
        ldapLayout.addWidget(self.ldap_base_dn, 1, 1)
        #ldapLayout.addWidget(self.ldapAdminLabel, 2, 0)
        #ldapLayout.addWidget(self.ldap_admin, 2, 1)
        ldapLayout.addWidget(self.ldapAdminPwdLabel, 3, 0)
        ldapLayout.addWidget(self.ldap_admin_pwd, 3, 1)
        ldapLayout.addWidget(self.ldapConfigPwdLabel, 4, 0)
        ldapLayout.addWidget(self.l_config_pwd, 4, 1)
        ldapLayout.addWidget(self.ladminLabel, 5, 0)
        ldapLayout.addWidget(self.ladmin_user, 5, 1)
        ldapLayout.addWidget(self.ladminPwdLabel, 6, 0)
        ldapLayout.addWidget(self.ladmin_pwd, 6, 1)

        ldapGroup.setLayout(ldapLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(ldapGroup)
        # mainLayout.addWidget(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startUpdateButton)
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