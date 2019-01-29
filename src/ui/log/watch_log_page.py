# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
import time
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QTextEdit)

class WacthLog(QDialog):
    def __init__(self, parent=None):
        super(WacthLog, self).__init__(parent)
        self.log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/installer.log')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))


        ## database parameters
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.watch_button = QPushButton("İzle")
        self.log_text.setMinimumSize(700, 300)
        ## Database Layout
        logGroup = QGroupBox("Lider Ahenk Logger")
        self.logLayout = QGridLayout()
        self.logLayout.addWidget(self.log_text)
        self.logLayout.addWidget(self.watch_button)
        logGroup.setLayout(self.logLayout)
        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(logGroup)
        mainLayout.addSpacing(12)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        # self.watch_log("Lider Ahenk Installer")
        # self.watch_button.clicked.connect(self.watch_log)

    def watch_log(self, line):
        # print("log izliyorum")
        # for line in Pygtail(self.log_file_path):
        #     sys.stdout.write(line)
        self.log_text.append(line)
        QCoreApplication.processEvents()


        # self.log_text.appendPlainText("LINE: {}".format("test message"))

        # ss = ""
        # for l in self.call_logger():
        #     ss += l
        #     self.log_text.appendPlainText("LINE: {}".format(ss))

    def call_logger(self):
        try:
            current = open(self.log_file_path, "r")
            curino = os.fstat(current.fileno() ).st_ino
            while True:
                while True:
                    line = current.readline()
                    if not line:
                        break
                    yield line
                try:
                    if os.stat(self.log_file_path).st_ino != curino:
                        new = open(self.log_file_path, "r")
                        current.close()
                        current = new
                        curino = os.fstat(current.fileno()).st_ino
                        continue
                except IOError:
                    pass
                time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = WacthLog()
    sys.exit(dialog.exec_())
