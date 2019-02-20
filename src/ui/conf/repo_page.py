#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QLineEdit, QWidget, QPushButton)
from install_manager import InstallManager
from api.util.util import Util
from ui.message_box.message_box import MessageBox


class RepoPage(QWidget):
    def __init__(self, parent=None):
        super(RepoPage, self).__init__(parent)

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))
        self.im = InstallManager()
        self.util = Util()
        self.msgBox = MessageBox()

        ## repository parameters
        self.repoLabel = QLabel("Repo Adresi:")
        self.repo_addr = QLineEdit("deb [arch=amd64] http://repo.liderahenk.org/liderahenk stable main")

        self.repoKeyLdabel = QLabel("Repo Key Dosyası:")
        self.repo_key = QLineEdit("http://repo.liderahenk.org/liderahenk-archive-keyring.asc")

        ## Repository Layout
        self.repoGroup = QGroupBox("Repo Sunucusu Bağlantı Bilgileri")
        self.repoLayout = QGridLayout()
        self.repoLayout.addWidget(self.repoLabel, 0, 0)
        self.repoLayout.addWidget(self.repo_addr, 0, 1)
        self.repoLayout.addWidget(self.repoKeyLdabel, 1, 0)
        self.repoLayout.addWidget(self.repo_key, 1, 1)
        self.repoGroup.setLayout(self.repoLayout)







