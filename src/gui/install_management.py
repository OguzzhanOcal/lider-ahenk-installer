# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5 import QtCore, QtGui, QtWidgets
import installerUi
from get_data import GetData
import sys, os, paramiko,json
import os.path

try:
    _fromUtf8 = QtCore.QStringListModel.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class InstallerManagement(QtWidgets.QWizard, installerUi.Ui_Installer):
    def __init__(self, parent=None):
        self.liderahenk_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dist/liderahenk.json')
        super(InstallerManagement, self).__init__(parent)
        self.setupUi(self)
        self.get_data = GetData()
        label = QtWidgets.QLabel(self.info)
        pixmap = QtGui.QPixmap('image/liderahenk.png')
        label.setPixmap(pixmap)
        self.msgBox = QtWidgets.QMessageBox()

        self.menubar = QtWidgets.QMenuBar(self)
        self.menu = self.menubar.addMenu('Lider Ahenk')
        self.menubar_action = QtWidgets.QAction(self)
        self.menubar_action.setText('Hakkında')
        self.menu.addAction(self.menubar_action)
        # self.menubar_action.triggered.connect(QtWidgets.QMessageBox.about(self, "Lider Ahenk", "Lider Ahenk Kolay Kurulum Uygulaması"))
        self.set_connect()

    def set_connect(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.hakkinda = QtWidgets.QMenu(self)
        self.hakkinda.setWindowTitle("Hakkında")
        self.menubar.addMenu(self.hakkinda)
        self.ssh_comboBox.addItems(["", "Uzak Makineye Kur", "Yerel Makineye Kur"])
        self.ssh_control_button.clicked.connect(self.ssh_control)
        self.save_button.clicked.connect(self.write_file)
        # self.next_install_button.clicked.connect(self.abstract_data)

    def ssh_control(self):
        data = GetData.get_data
        # bu satırda sunucunun nereye kurulacağı belirleniyor.
        ssh_combo_box = str(self.ssh_comboBox.currentText())
        if self.ssh_comboBox.currentIndex() == 1:
            print("1. index seçildi"+str(self.ssh_comboBox.currentIndex()))
        else:
            print("diğer index seçildi"+str(self.ssh_comboBox.currentIndex()))
        if data['ip'] is None:
            print(data['ip'])
            self.message("lütfen zorunlu alanları doldurunuz")
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            ssh_status = self.ssh.connect(hostname=ip, username=username, password=password, timeout=10)
            if ssh_status is None:
                self.message_box("Bağlantı Başarılı. Kuruluma Devam Edebilirsiniz.")
        except Exception as e:
            msg = "Bağlantı Sağlanamadı. Bağlantı Ayarlarını Kontrol Ederek Daha Sonra Tekrar Deneyiniz!"
            self.message_box(msg)

    def message_box(self, message):
        self.msgBox.setIcon(self.msgBox.Information)
        self.msgBox.setWindowTitle("Bilgilendirme")
        self.msgBox.setInformativeText(_fromUtf8(str(message)))
        self.msgBox.addButton(QtWidgets.QPushButton("Tamam"), QtWidgets.QMessageBox.NoRole)
        # self.msgBox.setDefaultButton(QtWidgets.QMessageBox.Close)
        self.ret = self.msgBox.exec_()

    def write_file(self):
        data = GetData.get_data

        if os.path.exists(self.liderahenk_data_path) and os.stat(self.liderahenk_data_path).st_size != 0:
            with open(self.liderahenk_data_path) as f:
                read_data = json.load(f)
            read_data.update(data)
            with open(self.liderahenk_data_path, 'w') as f:
                json.dump(read_data, f, ensure_ascii=False)
            print("data update edildi")
        else:
            with open(self.liderahenk_data_path, 'w') as f:
                json.dump(data, f, ensure_ascii=False)
            print("data oluşturuldu")

    # def abstract_data(self):
    #     abstract_2 = QPlainTextEdit()
    #     file = open(self.liderahenk_data_path)
    #     data = file.read()
    #     abstract_2.setPlainText(data)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = InstallerManagement()
    form.show()
    app.exec_()