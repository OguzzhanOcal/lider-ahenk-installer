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
        print("veriler alınıyor")
    #get data from installer gui_old

    def get_data(self):

        # if ldap status is Yeni
        # print(self.ldap_status.currentIndex())
        if self.ldap_status.currentIndex() == 0:
            ldap_status = 'new'
        else:
            # if ldap_status is 'Güncelle'
            ldap_status = 'update'

        data = {
            # Server Configuration
            'ip': self.ip.text(),
            'username': self.username.text(),
            'password': self.password.text(),

            # Database Configuration
            'db_server': self.ip.text(),
            'db_name': self.db_name.text(),
            'db_username': self.db_username.text(),
            'db_password': self.db_password.text(),

            # Ejabberd Configuration
            'e_service_name': self.e_service_name.text(),
            'e_username': self.e_username.text(),
            'e_user_pwd': self.e_user_pwd.text(),
            'e_hosts': self.e_host.text(),
            'ldap_servers': self.ip.text(),

            # OpenLDAP Configuration
            'l_base_dn': self.l_base_dn.text(),
            'l_config_pwd': self.l_config_admin_pwd.text(),
            'l_org_name': self.l_org_name.text(),
            'l_config_admin_dn': self.l_config_user.text(),
            'l_admin_cn': self.l_admin_cn.text(),
            'ladmin_user': self.lider_console_user.text(),
            'l_admin_pwd': self.l_admin_pwd.text(),
            'ladmin_pwd': self.lider_console_user_pwd.text(),
            'ldap_status': str(ldap_status),
            # yeni ldap kur ya da varolan ldapı konfigüre et 'new' ya da 'conf' parametreleri alıyor

            # Lider Configuration
            'lider_username': self.e_lider_username.text(),
            'lider_user_pwd': self.lider_sunucu_pwd.text(),

            # File Server Configuration
            'file_server': self.file_server.text(),
            'fs_username': self.fs_username.text(),
            'fs_username_pwd': self.fs_username_pwd.text(),
            'fs_plugin_path': self.fs_plugin_path.text(),
            "fs_agreement_path": self.fs_agreement_path.text(),
            "fs_agent_file_path": self.fs_agent_files_path.text()
        }
        return data