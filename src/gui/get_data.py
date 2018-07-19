# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5 import QtCore, QtWidgets
from gui.installerUi import Ui_Installer

try:
    _fromUtf8 = QtCore.QStringListModel.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class GetData(QtWidgets.QWizard, Ui_Installer):
    def __init__(self):
        super(GetData, self).__init__()
        self.location_server = None
        print("veriler alınıyor")
    #get data from installer gui_old

    def get_data(self):

        # if ldap status is Yeni
        # print(self.ldap_status.currentIndex())
        # index = self.ldap_status.currentIndex
        # print(index)
        if self.ldap_status.currentIndex() == 0:
            ldap_status = 'new'
        else:
            # if ldap_status is 'Güncelle'
            ldap_status = 'update'
        if self.location.currentIndex() == 1:
            self.location_server = 'remote'
        else:
            self.location_server = 'local'

        data = {
            'location': str(self.location_server),
            
            # Server Configuration
            'ip': self.server_host.text(),
            'username': self.username.text(),
            'password': self.user_password.text(),

            # Database Configuration
            'db_server': self.server_host.text(),
            'db_name': self.db_name.text(),
            'db_username': self.db_username.text(),
            'db_password': self.db_password.text(),

            # Ejabberd Configuration
            'e_service_name': self.e_service_name.text(),
            'e_username': self.e_username.text(),
            'e_user_pwd': self.e_user_pwd.text(),
            'e_hosts': self.server_host.text(),
            'ldap_servers': self.server_host.text(),

            # OpenLDAP Configuration
            'l_base_dn': self.l_base_dn.text(),
            'l_config_pwd': self.l_config_pwd.text(),
            'l_org_name': self.l_org_name.text(),
            'l_config_admin_dn': self.l_config_admin_dn.text(),
            'l_admin_cn': self.ldap_admin_cn.text(),
            'ladmin_user': self.lider_console_user.text(),
            'l_admin_pwd': self.l_admin_pwd.text(),
            'ladmin_pwd': self.lider_console_user_pwd.text(),
            'ldap_status': str(ldap_status),
            # yeni ldap kur ya da varolan ldapı konfigüre et 'new' ya da 'update' parametreleri alıyor

            # Lider Configuration
            'lider_username': self.e_lider_username.text(),
            'lider_user_pwd': self.e_lider_username_pwd.text(),

            # File Server Configuration
            'file_server': self.server_host.text(),
            'fs_username': self.fs_username.text(),
            'fs_username_pwd': self.fs_username_pwd.text(),
            'fs_plugin_path': self.fs_plugin_path.text(),
            "fs_agreement_path": self.fs_agreement_path.text(),
            "fs_agent_file_path": self.fs_agent_files_path.text()
        }
        return data


    def server_abstract(self):

        self.ldap_ip.setText(self.ip.text())
        self.ldap_admin_cn.setText(self.l_admin_cn.text())
        self.ldap_admin_pwd.setText(self.l_admin_pwd.text())
        self.ldap_base.setText(self.l_base_dn.text())
        self.e_host.setText(self.ip.text())
        self.lider_sunucu.setText(self.e_lider_username.text())
        self.lider_sunucu_pwd_2.setText(self.lider_sunucu_pwd.text())
        self.ejabberd_service.setText(self.e_service_name.text())
        self.file_server_2.setText(self.file_server.text())
        self.fs_username_2.setText(self.fs_username.text())
        self.fs_username_pwd_2.setText(self.fs_username_pwd.text())
        self.fs_plugin_path_2.setText(self.fs_plugin_path.text())
        self.fs_agreement_path_2.setText(self.fs_agreement_path.text())
        self.fs_agent_files_path_2.setText(self.fs_agent_files_path.text())
        self.db_server.setText(self.ip.text())
        self.db_username_2.setText(self.db_username.text())
        self.db_username_pwd.setText(self.db_password.text())
        self.db_name_2.setText(self.db_name.text())