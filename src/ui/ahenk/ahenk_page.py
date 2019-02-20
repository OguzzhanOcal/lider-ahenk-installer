#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget,
                             QHeaderView, QTableWidgetItem)
from install_manager import InstallManager
from ui.conf.repo_page import RepoPage
from ui.log.status_page import StatusPage
from ui.message_box.message_box import MessageBox


class AhenkPage(QWidget):
    def __init__(self, parent=None):
        super(AhenkPage, self).__init__(parent)
        self.ahenk_list_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ahenk_list.txt')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))

        self.log_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/installer.log')

        self.status = StatusPage()
        self.im = InstallManager()
        self.msg_box = MessageBox()
        self.data = None
        self.repo = RepoPage()

        ## client connect parameters
        self.serverIpLabel = QLabel("İstemci Adresi:")
        self.server_ip = QLineEdit()
        self.server_ip.setPlaceholderText("192.168.*.*")
        self.usernameLabel = QLabel("Kullanıcı Adı:")
        self.username = QLineEdit()
        self.username.setPlaceholderText("lider")
        self.passwordLabel = QLabel("Kullanıcı Parolası:")
        self.password = QLineEdit()
        self.password.setPlaceholderText("****")
        self.password.setEchoMode(QLineEdit.Password)
        self.checkControlButton = QPushButton("Ekle")

        ## Connect Layout
        self.connectGroup = QGroupBox("Ahenk Kurulucak İstemci Erişim Bilgileri")
        self.connectLayout = QGridLayout()
        self.connectLayout.addWidget(self.serverIpLabel, 0, 0)
        self.connectLayout.addWidget(self.server_ip, 0, 1)
        self.connectLayout.addWidget(self.usernameLabel, 1, 0)
        self.connectLayout.addWidget(self.username, 1, 1)
        self.connectLayout.addWidget(self.passwordLabel, 2, 0)
        self.connectLayout.addWidget(self.password, 2, 1)
        self.connectLayout.addWidget(self.checkControlButton, 0, 2)
        self.connectGroup.setLayout(self.connectLayout)

        repoGroup = QGroupBox("Repo Sunucusu Bilgileri")
        repoGroup.setLayout(self.repo.repoLayout)

        ## ahenk parameters
        self.hostLabel = QLabel("XMPP Sunucu Adresi:")
        self.host = QLineEdit()
        self.host.setPlaceholderText("192.168.*.*")
        # self.serviceNameLabel = QLabel("XMPP Servis Adı:")
        # self.service_name = QLineEdit()
        # self.service_name.setPlaceholderText("im.liderahenk.org")
        # self.resourceLabel = QLabel("Receiverresource:")
        # self.resource = QLineEdit()
        # self.resource.setEchoMode(QLineEdit.Password)
        # self.resource.setPlaceholderText("Smack")
        self.startUpdateButton = QPushButton("Kuruluma Başla")

        ## ahenk Layout
        self.ahenkGroup = QGroupBox("Ahenk Konfigürasyon Bilgileri")
        self.ahenkLayout = QGridLayout()
        self.ahenkLayout.addWidget(self.hostLabel, 0, 0)
        self.ahenkLayout.addWidget(self.host, 0, 1)
        # self.ahenkLayout.addWidget(self.serviceNameLabel, 1, 0)
        # self.ahenkLayout.addWidget(self.service_name, 1, 1)
        # self.ahenkLayout.addWidget(self.resourceLabel, 2, 0)
        # self.ahenkLayout.addWidget(self.resource, 2, 1)
        self.ahenkGroup.setLayout(self.ahenkLayout)

        ## ahenk list table
        self.ahenklistGroup = QGroupBox("Ahenk Kurulucak İstemci Listesi")
        self.ahenklistLayout = QGridLayout()
        self.tableWidget = QTableWidget()
        # self.tableWidget.setMinimumHeight(250)
        ## set read only table
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # set column count
        self.tableWidget.setColumnCount(4)
        headers = self.tableWidget.horizontalHeader()
        headers.setSectionResizeMode(0, QHeaderView.Stretch)
        headers.setSectionResizeMode(1, QHeaderView.Stretch)
        headers.setSectionResizeMode(2, QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["İstemci Adresi", "Kullanıcı Adı", "Kullanıcı Parolası", "İşlem"])
        self.ahenklistLayout.addWidget(self.tableWidget)
        self.ahenklistGroup.setLayout(self.ahenklistLayout)

        # Install Status Layout
        statusGroup = QGroupBox()
        self.status.statusLabel.setText("Ahenk Kurulum Durumu:")
        statusGroup.setLayout(self.status.statusLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.ahenkGroup)
        mainLayout.addWidget(repoGroup)
        mainLayout.addWidget(self.connectGroup)
        mainLayout.addWidget(self.ahenklistGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(self.startUpdateButton)
        mainLayout.addWidget(statusGroup)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        self.startUpdateButton.clicked.connect(self.install_ahenk)
        self.checkControlButton.clicked.connect(self.add_ahenk)

    def add_ahenk(self):

        ip = self.server_ip.text()
        username = self.username.text()
        password = self.password.text()

        ip_status = self.check_ip(ip)
        if ip_status is False:

            if ip is "" or username is "" or password is "":
                self.msg_box.warning("Lütfen istemci adresini, kullanıcı adını ve kullanıcı parolası giriniz!")
            else:
                self.server_ip.setText("")
                self.username.setText("")
                self.password.setText("")

                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                numcols = self.tableWidget.columnCount()
                numrows = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(numrows)
                self.tableWidget.setColumnCount(numcols)
                self.tableWidget.setItem(numrows - 1, 0, QTableWidgetItem(ip))
                self.tableWidget.setItem(numrows - 1, 1, QTableWidgetItem(username))
                self.tableWidget.setItem(numrows - 1, 2, QTableWidgetItem(password))

                self.delButton = QPushButton(self.tableWidget)
                self.delButton.setText('Sil')
                self.delButton.clicked.connect(self.del_ahenk)
                self.tableWidget.setCellWidget(numrows - 1, 3, self.delButton)
        else:
            self.msg_box.warning("Kayıt zaten var")

    def check_ip(self, ip):

        row_count = self.tableWidget.rowCount()
        ip_list = []
        if row_count != 0:
            for row in range(row_count):
                ip_item = self.tableWidget.item(row, 0)
                ip_addr = ip_item.text()
                ip_list.append(ip_addr)

            # check if ip exist in a list return True
            if ip in ip_list:
                return True
            else:
                return False
        else:
            return False

    def del_ahenk(self):

        rows = sorted(set(index.row() for index in
                          self.tableWidget.selectedIndexes()))
        for row in rows:
            self.tableWidget.selectRow(row)
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            self.msg_box.information("Kayıt Silindi")

    def install_ahenk(self):

        ## get item from ahenk list table
        row_count = self.tableWidget.rowCount()
        if row_count != 0:
            for row in range(row_count):
                ip_item = self.tableWidget.item(row, 0)
                ip = ip_item.text()

                username_item = self.tableWidget.item(row, 1)
                username = username_item.text()

                password_item = self.tableWidget.item(row, 2)
                password = password_item.text()

                repo_key = self.repo.repo_key.text()
                repo_addr = self.repo.repo_addr.text()

                self.data = {
                    # Client Configuration
                    'location': "remote",
                    'ip': ip,
                    'username': username,
                    'password': password,
                    # ahenk.conf Configuration
                    'host': self.host.text(),
                    'repo_key': repo_key,
                    'repo_addr': repo_addr
                }

                f = open(self.ahenk_list_file, "a+")
                f.write(ip + "\n")

                ssh_status = self.im.ssh_connect(self.data)
                if ssh_status is True:
                    # self.msg_box.information("Bağlantı Başarılı. Kuruluma Devam Edebilirsiniz.")
                    self.status.install_status.setText("Ahenk kurulumu devam ediyor...")
                    self.im.install_ahenk(self.data)
                    self.im.ssh_disconnect()
                    self.status.install_status.setText("Ahenk kurulumu tamamlandı")

                else:
                    msg = "Bağlantı Sağlanamadı. Bağlantı Ayarlarını Kontrol Ederek Daha Sonra Tekrar Deneyiniz!\n"
                    for col in range(3):
                        self.tableWidget.item(row, col).setBackground(QtGui.QColor(125, 125, 125))
                    #self.msg_box.information(msg)

        else:
            self.msg_box.warning("Kayıt bulunamadı!\n"
                                 "Lütfen istemci bilgisi giriniz")