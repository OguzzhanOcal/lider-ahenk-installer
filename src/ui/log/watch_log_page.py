#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox, QLabel, QLineEdit,
                             QVBoxLayout, QPlainTextEdit, QPushButton)
import os
import time

class DatabasePage(QDialog):
    def __init__(self, parent=None):
        super(DatabasePage, self).__init__(parent)
        self.log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/installer.log')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))


        ## database parameters
        self.log_text = QPlainTextEdit()
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
        self.watch_button.clicked.connect(self.watch_log)

        # self.watch_log()



    def watch_log(self):
        # self.log_text.appendPlainText("LINE: {}".format("test message"))

        ss = ""
        for l in self.call_logger():
            ss += l
            self.log_text.appendPlainText("LINE: {}".format(ss))

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
    dialog = DatabasePage()
    sys.exit(dialog.exec_())

#
# import sys
# from PyQt5 import QtWidgets
# import logging
#
# # Uncomment below for terminal log messages
# # logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# class QTextEditLogger(logging.Handler):
#     def __init__(self, parent):
#         super().__init__()
#         self.widget = QtWidgets.QPlainTextEdit(parent)
#         self.widget.setReadOnly(True)
#
#     def emit(self, record):
#         msg = self.format(record)
#         self.widget.appendPlainText(msg)
#
#
# class MyDialog(QtWidgets.QDialog, QtWidgets.QPlainTextEdit):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         logTextBox = QTextEditLogger(self)
#         # You can format what is printed to text box
#         logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#         logging.getLogger().addHandler(logTextBox)
#         # You can control the logging level
#         logging.getLogger().setLevel(logging.DEBUG)
#
#         self._button = QtWidgets.QPushButton(self)
#         self._button.setText('Test Me')
#
#         layout = QtWidgets.QVBoxLayout()
#         # Add the new logging box widget to the layout
#         layout.addWidget(logTextBox.widget)
#         layout.addWidget(self._button)
#         self.setLayout(layout)
#
#         # Connect signal to slot
#         self._button.clicked.connect(self.test)
#
#     def test(self):
#         logging.debug('damn, a bug')
#         logging.info('something to remember')
#         logging.warning('that\'s not right')
#         logging.error('foobar')
#
# app = QtWidgets.QApplication(sys.argv)
# dlg = MyDialog()
# dlg.show()
# dlg.raise_()
# sys.exit(app.exec_())




