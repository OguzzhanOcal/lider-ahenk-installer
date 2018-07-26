# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(699, 330)
        self.installer_about_text = QtWidgets.QTextBrowser(About)
        self.installer_about_text.setGeometry(QtCore.QRect(30, 20, 641, 231))
        self.installer_about_text.setObjectName("installer_about_text")
        self.exit_button = QtWidgets.QPushButton(About)
        self.exit_button.setGeometry(QtCore.QRect(580, 280, 84, 25))
        self.exit_button.setObjectName("exit_button")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Lider Ahenk Kolay Kurulum Uygulaması Hakkında"))
        self.installer_about_text.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Lider Ahenk Kurulum Uygulaması</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lider Ahenk sunucu kurulumu için geliştirilmiş kolay kurulum uygulamasıdır. Daha fazla bilgiye <span style=\" font-weight:600; color:#a40000;\">http://docs.liderahenk.org/</span><span style=\" color:#a40000;\"> </span>adresinden ulaşabilirsiniz.</p></body></html>"))
        self.exit_button.setText(_translate("About", "Çıkış"))
#
#
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

