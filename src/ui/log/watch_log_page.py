#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QPushButton)

class WatchLog(QWidget):
    def __init__(self, parent=None):
        super(WatchLog, self).__init__(parent)
        self.liderdb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/liderdb.json')

        self.log_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/installer.log')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))

        self.data = None

        ## database parameters
        self.log_name = QTextEdit()
        self.log_name.setReadOnly(True)
        self.log_name.setMinimumSize(200, 500)

        self.refreshButton = QPushButton("Yenile")

        ## Log Layout
        logGroup = QGroupBox("Lider Ahenk Kurulum İzle")
        self.logLayout = QGridLayout()
        self.logLayout.addWidget(self.log_name)

        logGroup.setLayout(self.logLayout)

        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.releasesCheckBox)
        mainLayout.addWidget(logGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(self.refreshButton)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        self.append_logger()

        self.refreshButton.clicked.connect(self.append_logger)


    def append_logger(self):
        with open(self.log_out_path) as f:
            for line in f:
                # print(line)
                self.log_name.append(str(line))

