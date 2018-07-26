#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

# interface management module of the Lider Ahenk Installer application

import sys
from ui.about import Ui_About
from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QStringListModel.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
class AboutManager(QtWidgets.QWidget, Ui_About):

    def __int__(self):
        super(AboutManager, self).__init__()

        self.setupUi(self)
        #

    def config(self):
        self.setWindowIcon(QtGui.QIcon('image/cancel-16.png' ))
        self.setFixedSize(self.size())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())



