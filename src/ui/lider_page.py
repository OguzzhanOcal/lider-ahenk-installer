#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget, QRadioButton)
from ui.ldap_page import OpenLdapPage
from ui.ejabberd_page import EjabberdPage
from ui.db_page import DatabasePage
from ui.connect_page import ConnectPage
import os
import json

class LiderPage(QWidget):
    def __init__(self, parent=None):
        super(LiderPage, self).__init__(parent)

        self.liderldap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist/lider_ldap.json')
        self.liderejabberd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../dist/lider_ejabberd.json')
        self.liderdb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist/liderdb.json')
        self.lider_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist/lider.json')

        self.ldap_layout = OpenLdapPage()
        self.ejabberd_layout = EjabberdPage()
        self.db_layout = DatabasePage()
        self.connect_layout = ConnectPage()


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
        self.startUpdateButton = QPushButton("Kuruluma Başla")

        self.startUpdateButton.clicked.connect(self.abstract_data)

        liderLdapGroup = QGroupBox("LDAP Konfigürasyon Bilgileri")
        liderXmppGroup = QGroupBox("XMPP Konfigürasyon Bilgileri")
        liderDbGroup = QGroupBox("Veritabanı Konfigürasyon Bilgileri")

        liderLdapGroup.setLayout(self.ldap_layout.ldapLayout)
        liderXmppGroup.setLayout(self.ejabberd_layout.ejabberdLayout)
        liderDbGroup.setLayout(self.db_layout.dbLayout)

        ## Connect Layout
        connectGroup = QGroupBox("Lİder Sunucusu Bağlantı Bilgileri")
        connectGroup.setLayout(self.connect_layout.connectLayout)

        mainLayout = QVBoxLayout()
        # mainLayout = QGridLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(liderLdapGroup)
        mainLayout.addWidget(liderXmppGroup)
        mainLayout.addWidget(liderDbGroup)
        # mainLayout.addSpacing(12)
        mainLayout.addWidget(self.startUpdateButton)
        # mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def abstract_data(self):

        ## get data from ldap json file
        with open(self.liderldap_path) as f:
            ldap_data = json.load(f)
        # self.logger.info("liderahenk.json dosyasından veriler okunuyor")

        self.ldap_layout.ldap_base_dn.setText(ldap_data["l_base_dn"])
        self.ldap_layout.ldap_admin_pwd.setText(ldap_data["l_admin_pwd"])
        self.ldap_layout.l_config_pwd.setText(ldap_data["l_config_pwd"])
        self.ldap_layout.ladmin_user.setText(ldap_data["ladmin_user"])
        self.ldap_layout.ladmin_pwd.setText(ldap_data["ladmin_pwd"])

        ## get data from ejabberd json file
        with open(self.liderejabberd_path) as f:
            ejabberd_data = json.load(f)

        self.ejabberd_layout.e_service_name.setText(ejabberd_data["e_service_name"])
        self.ejabberd_layout.e_user_pwd.setText(ejabberd_data["e_user_pwd"])
        self.ejabberd_layout.lider_user_pwd.setText(ejabberd_data["lider_user_pwd"])
        self.ejabberd_layout.ldap_server.setText(ejabberd_data["ldap_servers"])
        self.ejabberd_layout.ldap_base_dn.setText(ejabberd_data['l_base_dn'])
        self.ejabberd_layout.ldap_admin_pwd.setText(ejabberd_data['l_admin_pwd'])

        ## get data from database json file
        with open(self.liderdb_path) as f:
            db_data = json.load(f)

        self.db_layout.db_name.setText(db_data["db_name"])
        self.db_layout.db_username.setText(db_data["db_username"])
        self.db_layout.db_password.setText(db_data["db_password"])

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
            'db_name': self.db_layout.db_name.text(),
            'db_username': self.db_layout.db_username.text(),
            'db_password': self.db_layout.db_password.text(),

        }
        print(data)

        if os.path.exists(self.lider_path) and os.stat(self.lider_path).st_size != 0:
            with open(self.lider_path) as f:
                read_data = json.load(f)
            read_data.update(data)
            with open(self.lider_path, 'w') as f:
                json.dump(read_data, f, ensure_ascii=False)
            print('Lider Ahenk json dosyası güncellendi')
            # self.logger.info("Lider Ahenk json dosyası güncellendi")
            # self.message_box("Lider Ahenk json dosyası güncellendi")
        else:
            with open(self.lider_path, 'w') as f:
                json.dump(data, f, ensure_ascii=False)
                print("Lider Ahenk json dosyası oluşturuldu")
            # self.logger.info("Lider Ahenk json dosyası oluşturuldu")
            # self.message_box("Lider Ahenk json dosyası oluşturuldu")







