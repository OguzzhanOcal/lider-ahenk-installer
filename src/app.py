#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import time
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDialog, QHBoxLayout, QListView, QListWidget, QListWidgetItem, QPushButton,
                             QStackedWidget, QVBoxLayout, QMenuBar, QAction, QMessageBox, QSlider, QLineEdit, QHeaderView)
import ui.conf.configdialog_rc
from ui.ejabberd.ejabberd_page import EjabberdPage
from ui.database.db_page import DatabasePage
from ui.ldap.ldap_page import OpenLdapPage
from ui.lider.lider_page import LiderPage
from ui.message_box.message_box import MessageBox
from ui.ahenk.ahenk_page import AhenkPage
from ui.log.watch_log_page import WatchLog


class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)

        self.msg_box = MessageBox()

        self.contentsWidget = QListWidget()
        self.contentsWidget.setViewMode(QListView.IconMode)
        self.contentsWidget.setIconSize(QSize(96, 84))
        self.contentsWidget.setMovement(QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setMinimumWidth(128)
        self.contentsWidget.setMinimumHeight(700)
        self.contentsWidget.setSpacing(12)

        #aboutAction = QAction('About', self)
        #aboutAction.setStatusTip('About')
        #aboutAction.triggered.connect(QMessageBox.information(self, None, "Lider Ahenk Kurulum Uygulaması"))

        self.pagesWidget = QStackedWidget()
        self.pagesWidget.setMinimumHeight(700)
        self.pagesWidget.setMinimumWidth(512)

        self.pagesWidget.addWidget(DatabasePage())
        self.pagesWidget.addWidget(OpenLdapPage())
        self.pagesWidget.addWidget(EjabberdPage())
        self.pagesWidget.addWidget(LiderPage())
        self.pagesWidget.addWidget(AhenkPage())
        self.pagesWidget.addWidget(WatchLog())
        closeButton = QPushButton("Kapat")
        self.createIcons()
        self.contentsWidget.setCurrentRow(0)
        closeButton.clicked.connect(self.close)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)

        self.progress = QSlider()
        self.progress.setOrientation(Qt.Horizontal)
        # self.progress.setStyleSheet("background-color:turquoise")
        # self.progress.setOrientation(Qt.AlignTop.())
        self.progress.setMaximumHeight(50)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        #mainLayout.addWidget(menubar)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)


        self.setLayout(mainLayout)
        self.setWindowTitle("Lider Ahenk Kurulum Uygulaması")
        self.setWindowIcon(QIcon(":/images/liderahenk-32.png"))

    def changePage(self, current, previous):
        if not current:
            current = previous
        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def createIcons(self):
        dbButton = QListWidgetItem(self.contentsWidget)
        dbButton.setIcon(QIcon(':/images/database.png'))
        dbButton.setText("Veritabanı")
        dbButton.setTextAlignment(Qt.AlignHCenter)
        dbButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        ldapButton = QListWidgetItem(self.contentsWidget)
        ldapButton.setIcon(QIcon(':/images/ldap.png'))
        ldapButton.setText("OpenLDAP")
        ldapButton.setTextAlignment(Qt.AlignHCenter)
        ldapButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        xmppButton = QListWidgetItem(self.contentsWidget)
        xmppButton.setIcon(QIcon(':/images/ejabberd.png'))
        xmppButton.setText("Ejabberd")
        xmppButton.setTextAlignment(Qt.AlignHCenter)
        xmppButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        liderButton = QListWidgetItem(self.contentsWidget)
        liderButton.setIcon(QIcon(':/images/liderahenk.png'))
        liderButton.setText("Lider")
        liderButton.setTextAlignment(Qt.AlignHCenter)
        liderButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        ahenkButton = QListWidgetItem(self.contentsWidget)
        ahenkButton.setIcon(QIcon(':/images/ahenk-register.png'))
        ahenkButton.setText("Ahenk")
        ahenkButton.setTextAlignment(Qt.AlignHCenter)
        ahenkButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        logButton = QListWidgetItem(self.contentsWidget)
        logButton.setIcon(QIcon(':/images/log.png'))
        logButton.setText("Log")
        logButton.setTextAlignment(Qt.AlignHCenter)
        logButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = ConfigDialog()
    sys.exit(dialog.exec_())    
