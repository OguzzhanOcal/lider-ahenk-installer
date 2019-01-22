#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget, QRadioButton)
import json
import os
from ui.connect_page import ConnectPage
from install_manager import InstallManager
from ui.message_box import MessageBox
import time



class DatabasePage(QDialog):
    def __init__(self, parent=None):
        super(DatabasePage, self).__init__(parent)
        self.liderdb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist/liderdb.json')
        # self.log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/installer.log')
        # self.log_backup_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/installer.log.{0}')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist'))

        self.connect_layout = ConnectPage()
        self.im = InstallManager()
        self.msg_box = MessageBox()

        ## database parameters
        self.dbNameLabel = QLabel("Veritabanı Adı:")
        self.db_name = QLineEdit()

        ## Database Layout
        dbGroup = QGroupBox("Veritabanı Konfigürasyon Bilgileri")
        self.dbLayout = QGridLayout()

        self.dbLayout.addWidget(self.db_name)



        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(dbGroup)
        mainLayout.addSpacing(12)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = DatabasePage()
    sys.exit(dialog.exec_())





