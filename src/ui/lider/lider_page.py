#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>


import os
import json
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QWidget)
from ui.ldap.ldap_page import OpenLdapPage
from ui.ejabberd.ejabberd_page import EjabberdPage
from ui.database.db_page import DatabasePage
from ui.connect.connect_page import ConnectPage
from install_manager import InstallManager
from ui.message_box.message_box import MessageBox

class LiderPage(QWidget):
    def __init__(self, parent=None):
        super(LiderPage, self).__init__(parent)

        self.liderldap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/lider_ldap.json')
        self.liderejabberd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/lider_ejabberd.json')
        self.liderdb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/liderdb.json')
        self.lider_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/lider.json')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))

        self.ldap_layout = OpenLdapPage()
        self.ejabberd_layout = EjabberdPage()
        self.db_layout = DatabasePage()
        self.connect_layout = ConnectPage()
        self.im = InstallManager()
        self.msg_box = MessageBox()
        self.data = None

        ## db parameters
        self.dbServerLabel = QLabel("Veritabanı Sunucu Adresi:")
        self.db_server = QLineEdit()
        self.db_server.setPlaceholderText("192.168.*.*")

        # OpenLDAP parameters
        self.ldapServerLabel = QLabel("LDAP Sunucu Adresi:")
        self.ldap_server = QLineEdit()
        self.ldap_server.setPlaceholderText("192.168.*.*")

        # Ejabberd parameters
        self.ejabberdServerLabel = QLabel("XMPP Sunucu Adresi:")
        self.ejabberd_server = QLineEdit()
        self.ejabberd_server.setPlaceholderText("192.168.*.*")

        self.fileServerLabel = QLabel("Dosya Sunucu Adresi:")
        self.file_server = QLineEdit()
        self.file_server.setPlaceholderText("192.168.*.*")
        self.file_server.setDisabled(True)

        self.getDataButton = QPushButton("Verileri Getir")
        self.getDataButton.clicked.connect(self.get_data)

        self.installButton = QPushButton("Kaydet ve Kur")
        self.installButton.clicked.connect(self.save_lider_data)

        self.liderLdapGroup = QGroupBox("LDAP Konfigürasyon Bilgileri")
        self.liderXmppGroup = QGroupBox("XMPP Konfigürasyon Bilgileri")
        self.liderDbGroup = QGroupBox("Veritabanı Konfigürasyon Bilgileri")

        # add server ip to database layout
        self.db_layout.dbLayout.addWidget(self.dbServerLabel, 3, 0)
        self.db_layout.dbLayout.addWidget(self.db_server, 3, 1)
        self.liderDbGroup.setLayout(self.db_layout.dbLayout)

        # add server ip to ldap layout
        self.ldap_layout.ldapLayout.addWidget(self.ldapServerLabel)
        self.ldap_layout.ldapLayout.addWidget(self.ldap_server)
        self.ldap_layout.ldapLayout.removeWidget(self.ldap_layout.ldapStatusCombo)
        self.ldap_layout.ldapLayout.removeWidget(self.ldap_layout.ldapStatusLabel)
        self.liderLdapGroup.setLayout(self.ldap_layout.ldapLayout)

        # add server ip to ejabberd layout
        self.ejabberd_layout.ejabberdLayout.removeWidget(self.ejabberd_layout.ldapServerLabel)
        self.ejabberd_layout.ejabberdLayout.removeWidget(self.ejabberd_layout.ldap_server)
        self.ejabberd_layout.ejabberdLayout.addWidget(self.ejabberdServerLabel, 8, 0)
        self.ejabberd_layout.ejabberdLayout.addWidget(self.ejabberd_server, 8, 1)
        self.liderXmppGroup.setLayout(self.ejabberd_layout.ejabberdLayout)

        ## Connect Layout
        self.connect_layout.serverCombo.currentIndexChanged.connect(self.check_control_button)
        self.connectGroup = QGroupBox("Lİder Sunucusu Bağlantı Bilgileri")
        self.connect_layout.connectLayout.addWidget(self.fileServerLabel, 4, 0)
        self.connect_layout.connectLayout.addWidget(self.file_server, 4, 1)
        self.connectGroup.setLayout(self.connect_layout.connectLayout)

        # mainLayout = QVBoxLayout()
        mainLayout = QGridLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(self.connectGroup,0,0)
        mainLayout.addWidget(self.liderLdapGroup,0,1)
        mainLayout.addWidget(self.liderXmppGroup,1,0)
        mainLayout.addWidget(self.liderDbGroup,1,1)
        # mainLayout.addSpacing(12)
        mainLayout.addWidget(self.getDataButton)
        mainLayout.addWidget(self.installButton)
        # mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def check_control_button(self, idx):
        ## if select location is remote server
        if idx == 0:
            # self.checkControlButton.setEnabled(True)
            self.file_server.setDisabled(True)
        else:
            self.file_server.setDisabled(False)

    def get_data(self):

        if os.path.exists(self.liderldap_path):

            ## get data from ldap json file
            with open(self.liderldap_path) as f:
                ldap_data = json.load(f)
            # self.logger.info("liderahenk.json dosyasından veriler okunuyor")

            self.ldap_layout.ldap_base_dn.setText(ldap_data["l_base_dn"])
            self.ldap_layout.ldap_admin_pwd.setText(ldap_data["l_admin_pwd"])
            self.ldap_layout.l_config_pwd.setText(ldap_data["l_config_pwd"])
            self.ldap_layout.ladmin_user.setText(ldap_data["ladmin_user"])
            self.ldap_layout.ladmin_pwd.setText(ldap_data["ladmin_pwd"])
        else:
            self.msg_box.information("Kayıtlı OpenLDAP bilgileri bulunumadı.\n\n"
                                     "Lider konfigürasyonu için Lider sayfasındaki alanları doldurarak kuruluma devam edebilirsiniz.")

        if os.path.exists(self.liderejabberd_path):

            ## get data from ejabberd json file
            with open(self.liderejabberd_path) as f:
                ejabberd_data = json.load(f)

            self.ejabberd_layout.e_service_name.setText(ejabberd_data["e_service_name"])
            self.ejabberd_layout.e_user_pwd.setText(ejabberd_data["e_user_pwd"])
            self.ejabberd_layout.lider_user_pwd.setText(ejabberd_data["lider_user_pwd"])
            self.ldap_server.setText(ejabberd_data["ldap_servers"])
            self.ejabberd_layout.ldap_base_dn.setText(ejabberd_data['l_base_dn'])
            self.ejabberd_layout.ldap_admin_pwd.setText(ejabberd_data['l_admin_pwd'])
            self.ejabberd_server.setText(ejabberd_data['ip'])
        else:
            self.msg_box.information("Kayıtlı  XMPP bilgileri bulunumadı.\n\n"
                                     "Lider konfigürasyonu için Lider sayfasındaki alanları doldurarak kuruluma devam edebilirsiniz.")

        if os.path.exists(self.liderdb_path):
            ## get data from database json file
            with open(self.liderdb_path) as f:
                db_data = json.load(f)

            if db_data["ip"] == self.connect_layout.server_ip.text():
                db_server = "127.0.0.1"
            else:
                db_server = db_data["ip"]

            self.db_server.setText(db_server)
            self.db_layout.db_name.setText(db_data["db_name"])
            self.db_layout.db_username.setText(db_data["db_username"])
            self.db_layout.db_password.setText(db_data["db_password"])

        else:
            self.msg_box.information("Kayıtlı Veritabanı bilgileri bulunumadı.\n\n"
                                     "Lider konfigürasyonu için Lider sayfasındaki alanları doldurarak kuruluma devam edebilirsiniz.")

    def save_lider_data(self):

        if self.connect_layout.serverCombo.currentIndex() == 0:
            location_server = 'remote'
            file_server = self.connect_layout.server_ip.text()
        else:
            location_server = 'local'
            file_server = self.file_server.text()

        l_org_name = self.ldap_layout.ldap_base_dn.text().split('.')
        l_org_name = l_org_name[0]

        self.data = {
            'location': location_server,

            # Server Configuration
            'ip': self.connect_layout.server_ip.text(),
            'username': self.connect_layout.username.text(),
            'password': self.connect_layout.password.text(),
            # Database Configuration
            'db_server': self.db_server.text(),
            'db_name': self.db_layout.db_name.text(),
            'db_username': self.db_layout.db_username.text(),
            'db_password': self.db_layout.db_password.text(),

            # Ejabberd Configuration
            'e_service_name': self.ejabberd_layout.e_service_name.text(),
            'e_username': self.ejabberd_layout.e_username.text(),
            'e_user_pwd': self.ejabberd_layout.e_user_pwd.text(),
            'e_hosts': self.ejabberd_server.text(),
            'lider_username': 'lider_sunucu',
            'lider_user_pwd': self.ejabberd_layout.lider_user_pwd.text(),

            # OpenLDAP Configuration
            'l_base_dn': self.ldap_layout.ldap_base_dn.text(),
            'l_config_pwd': self.ldap_layout.l_config_pwd.text(),
            'l_org_name': l_org_name,
            'l_config_admin_dn': "cn=admin,cn=config",
            'l_admin_cn': "admin",
            'ladmin_user': self.ldap_layout.ladmin_user.text(),
            'l_admin_pwd': self.ldap_layout.ldap_admin_pwd.text(),
            'ladmin_pwd': self.ldap_layout.ladmin_pwd.text(),
            'ldap_servers': self.ldap_server.text(),

            # File Server Configuration
            'file_server': file_server,
            'fs_username': self.connect_layout.username.text(),
            'fs_username_pwd': self.connect_layout.password.text(),
            'fs_plugin_path': '/home/{username}'.format(username=self.connect_layout.username.text()),
            "fs_agreement_path": '/home/{username}'.format(username=self.connect_layout.username.text()),
            "fs_agent_file_path": '/home/{username}'.format(username=self.connect_layout.username.text()),
        }

        if self.data['l_base_dn'] == "" or self.data['l_config_pwd'] == "" or self.data['ladmin_user'] == "" or self.data['l_admin_pwd'] == "" or self.data['ladmin_pwd'] == ""\
                or self.data['db_name'] == "" or self.data['db_username'] == "" or self.data['db_password'] == ""\
                or self.data['e_service_name'] == "" or self.data['e_user_pwd'] == "" or self.data['ldap_servers'] == "" or self.data['l_base_dn'] == "" or self.data['lider_user_pwd'] == "" or self.data['l_admin_pwd'] ==""\
                or self.data['ip'] =="" or self.data['username'] == "" or self.data['password'] =="":
            self.msg_box.warning("Lütfen aşağıdaki alanları doldurunuz.\n"
                                     "- Lider sunucu bağlantı bilgileri\n"
                                     "- LDAP bilgileri\n"
                                     "- Veritabanı bilgileri\n"
                                     "- XMPP bilgileri")
        else:

            if os.path.exists(self.lider_path) and os.stat(self.lider_path).st_size != 0:
                with open(self.lider_path) as f:
                    read_data = json.load(f)
                read_data.update(self.data)
                with open(self.lider_path, 'w') as f:
                    json.dump(read_data, f, ensure_ascii=False)
                print('Lider Ahenk json dosyası güncellendi')
                # self.logger.info("Lider Ahenk json dosyası güncellendi")
                self.msg_box.information("Lider bilgileri güncellendi\n"
                                         "Lider kurulumana başlanacak.")
            else:
                with open(self.lider_path, 'w') as f:
                    json.dump(self.data, f, ensure_ascii=False)
                    print("Lider Ahenk json dosyası oluşturuldu")
                # self.logger.info("Lider Ahenk json dosyası oluşturuldu")
                self.msg_box.information("Lider bilgileri kaydedildi\n"
                                         "Lider kurulumuna başlanacak.")


            if self.data['location'] == 'remote':
                self.im.ssh_connect(self.data)
                self.im.install_lider(self.data)
                self.im.ssh_disconnect()
            else:
                self.im.install_lider(self.data)










