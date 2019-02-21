#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
import json
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget)
from install_manager import InstallManager
from ui.conf.repo_page import RepoPage
from ui.message_box.message_box import MessageBox
from ui.connect.connect_page import ConnectPage
from ui.log.status_page import StatusPage

class EjabberdPage(QWidget):
    def __init__(self, parent=None):
        super(EjabberdPage, self).__init__(parent)

        self.liderejabberd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/lider_ejabberd.json')
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))

        self.data = None
        self.im = InstallManager()
        self.msg_box = MessageBox()
        self.status = StatusPage()
        self.repo = RepoPage()

        self.connect_layout = ConnectPage()
        self.startUpdateButton = QPushButton("Kuruluma Başla")
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
        self.ldap_server = QLineEdit()
        self.ldap_server.setPlaceholderText("192.168.*.*")
        self.ldapBaseDnLabel = QLabel("LDAP Base DN:")
        self.ldap_base_dn = QLineEdit()
        self.ldap_base_dn.setPlaceholderText("liderahenk.org")
        self.ldapAdminPwdLabel = QLabel("Ldap Admin Parolası:")
        self.ldap_admin_pwd = QLineEdit()
        self.ldap_admin_pwd.setPlaceholderText("****")
        self.ldap_admin_pwd.setEchoMode(QLineEdit.Password)

        ## Connect Layout
        connectGroup = QGroupBox("XMPP Sunucusu Bağlantı Bilgileri")
        connectGroup.setLayout(self.connect_layout.connectLayout)

        # repo layout
        repoGroup = QGroupBox("Repo Sunucusu Bilgileri")
        repoGroup.setLayout(self.repo.repoLayout)

        # Install Status Layout
        statusGroup = QGroupBox()
        self.status.statusLabel.setText("XMPP Kurulum Durumu:")
        statusGroup.setLayout(self.status.statusLayout)

        ## XMPP configuration Layout
        ejabberdGroup = QGroupBox("XMPP Sunucu Konfigürasyon Bilgileri")
        self.ejabberdLayout = QGridLayout()
        self.ejabberdLayout.addWidget(self.ejabberdServiceLabel, 0, 0)
        self.ejabberdLayout.addWidget(self.e_service_name, 0, 1)
        # self.ejabberdLayout.addWidget(self.ejabberdAdminLabel, 1, 0)
        # self.ejabberdLayout.addWidget(self.e_username, 1, 1)
        self.ejabberdLayout.addWidget(self.ejabberdAdminPwdLabel, 2, 0)
        self.ejabberdLayout.addWidget(self.e_user_pwd, 2, 1)
        # self.ejabberdLayout.addWidget(self.ejabberdLiderUserLabel, 3, 0)
        # self.ejabberdLayout.addWidget(self.lider_username, 3, 1)
        self.ejabberdLayout.addWidget(self.ejabberdLiderPwdLAbel, 4, 0)
        self.ejabberdLayout.addWidget(self.lider_user_pwd, 4, 1)
        self.ejabberdLayout.addWidget(self.ldapServerLabel, 5, 0)
        self.ejabberdLayout.addWidget(self.ldap_server, 5, 1)
        self.ejabberdLayout.addWidget(self.ldapBaseDnLabel, 6, 0)
        self.ejabberdLayout.addWidget(self.ldap_base_dn, 6, 1)
        self.ejabberdLayout.addWidget(self.ldapAdminPwdLabel, 7, 0)
        self.ejabberdLayout.addWidget(self.ldap_admin_pwd, 7, 1)

        ejabberdGroup.setLayout(self.ejabberdLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(connectGroup)
        mainLayout.addWidget(repoGroup)
        mainLayout.addWidget(ejabberdGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(self.startUpdateButton)
        mainLayout.addWidget(statusGroup)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        self.startUpdateButton.clicked.connect(self.save_ejabberd_data)

    def save_ejabberd_data(self):

        if self.connect_layout.serverCombo.currentIndex() == 0:
            location_server = 'remote'
        else:
            location_server = 'local'

        self.data = {

            'location': location_server,
            # Server Configuration
            'ip': self.connect_layout.server_ip.text(),
            'username': self.connect_layout.username.text(),
            'password': self.connect_layout.password.text(),
            # Ejabberd Configuration
            'e_service_name': self.e_service_name.text(),
            'e_username': 'admin',
            'e_user_pwd': self.e_user_pwd.text(),
            'e_hosts': self.connect_layout.server_ip.text(),
            'ldap_servers': self.ldap_server.text(),
            'l_base_dn': self.ldap_base_dn.text(),

            # Lider Configuration
            'lider_username': 'lider_sunucu',
            'lider_user_pwd': self.lider_user_pwd.text(),
            'l_admin_pwd': self.ldap_admin_pwd.text(),
            'repo_key': self.repo.repo_key.text(),
            'repo_addr': self.repo.repo_addr.text()
        }

        if self.data['e_service_name'] == "" or self.data['e_user_pwd'] == "" or self.data['ldap_servers'] == "" or self.data['l_base_dn'] == "" or self.data['lider_user_pwd'] == "" or self.data['l_admin_pwd'] == ""\
                or self.data['ip'] =="" or self.data['username'] == "" or self.data['password'] =="":
            self.msg_box.warning("Lütfen aşağıdaki alanları doldurunuz.\n"
                                     "- XMPP sunucu bağlantı bilgileri\n"
                                     "- XMPP servis adı\n"
                                     "- XMPP admin parolası\n"
                                     "- lider_sunucu parolası\n"
                                     "- LDAP bilgileri")

        else:
            self.status.install_status.setText("XMPP kurulumu devam ediyor...")
            self.status.install_status.setStyleSheet("background-color: green")
            if os.path.exists(self.liderejabberd_path) and os.stat(self.liderejabberd_path).st_size != 0:
                with open(self.liderejabberd_path) as f:
                    read_data = json.load(f)
                read_data.update(self.data)
                with open(self.liderejabberd_path, 'w') as f:
                    json.dump(read_data, f, ensure_ascii=False)
                print("Lider Ahenk json dosyası güncellendi")
                # self.logger.info("Lider Ahenk json dosyası güncellendi")
                self.msg_box.information("XMPP bilgileri güncellendi\n"
                                         "XMPP kurulumuna başlanacak.")
            else:
                with open(self.liderejabberd_path, 'w') as f:
                    json.dump(self.data, f, ensure_ascii=False)
                    print("Lider Ahenk json dosyası oluşturuldu")
                # self.logger.info("Lider Ahenk json dosyası oluşturuldu")
                self.msg_box.information("XMPP bilgileri kaydedildi\n"
                                         "XMPP kurulumuna başlanacak.")

            if self.data['location'] == 'remote':
                self.im.ssh_connect(self.data)
                self.im.install_ejabberd(self.data)
                self.im.ssh_disconnect()
            else:
                self.im.install_ejabberd(self.data)

            self.status.install_status.setText("XMPP kurulumu tamamlandı")
            self.status.install_status.setStyleSheet("background-color: cyan")
            self.msg_box.information("XMPP kurulumu tamamlandı")

