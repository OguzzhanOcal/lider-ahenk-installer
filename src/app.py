#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5.QtCore import QDate, QSize, Qt, QStringListModel
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, QPushButton, QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget, QMessageBox)

import ui.configdialog_rc

from ui.ejabberd_page import EjabberdPage
from ui.db_page import DatabasePage
from ui.ldap_page import OpenLdapPage
from ui.lider_page import LiderPage

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)

        self.contentsWidget = QListWidget()
        self.contentsWidget.setViewMode(QListView.IconMode)
        self.contentsWidget.setIconSize(QSize(96, 84))
        self.contentsWidget.setMovement(QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setMinimumWidth(128)
        self.contentsWidget.setMinimumHeight(512)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QStackedWidget()
        # self.pagesWidget.setMinimumHeight(600)
        self.pagesWidget.setMinimumWidth(512)

        self.pagesWidget.addWidget(DatabasePage())
        self.pagesWidget.addWidget(OpenLdapPage())
        self.pagesWidget.addWidget(EjabberdPage())
        self.pagesWidget.addWidget(LiderPage())

        closeButton = QPushButton("Kapat")

        self.msgBox = QMessageBox()
        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.clicked.connect(self.close)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
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
        queryButton = QListWidgetItem(self.contentsWidget)
        queryButton.setIcon(QIcon(':/images/database.png'))
        queryButton.setText("Veritabanı")
        queryButton.setTextAlignment(Qt.AlignHCenter)
        queryButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        updateButton = QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QIcon(':/images/ldap.png'))
        updateButton.setText("OpenLDAP")
        updateButton.setTextAlignment(Qt.AlignHCenter)
        updateButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        xmppButton = QListWidgetItem(self.contentsWidget)
        xmppButton.setIcon(QIcon(':/images/ejabberd.png'))
        xmppButton.setText("Ejabberd")
        xmppButton.setTextAlignment(Qt.AlignHCenter)
        xmppButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        configButton = QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QIcon(':/images/liderahenk.png'))
        configButton.setText("Lider")
        configButton.setTextAlignment(Qt.AlignHCenter)
        configButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = ConfigDialog()
    sys.exit(dialog.exec_())    
