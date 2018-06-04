# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Installer(object):
    def setupUi(self, Installer):
        Installer.setObjectName("Installer")
        Installer.setWindowModality(QtCore.Qt.NonModal)
        Installer.setEnabled(True)
        Installer.resize(1152, 864)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Installer.sizePolicy().hasHeightForWidth())
        Installer.setSizePolicy(sizePolicy)
        Installer.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/image/liderahenk-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Installer.setWindowIcon(icon)
        Installer.setAutoFillBackground(True)
        Installer.setSizeGripEnabled(True)
        Installer.setModal(False)
        Installer.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        self.info = QtWidgets.QWizardPage()
        self.info.setAutoFillBackground(False)
        self.info.setStyleSheet("")
        self.info.setObjectName("info")
        Installer.addPage(self.info)
        self.connect = QtWidgets.QWizardPage()
        self.connect.setObjectName("connect")
        self.ip = QtWidgets.QLineEdit(self.connect)
        self.ip.setGeometry(QtCore.QRect(560, 300, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip.sizePolicy().hasHeightForWidth())
        self.ip.setSizePolicy(sizePolicy)
        self.ip.setMinimumSize(QtCore.QSize(321, 0))
        self.ip.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ip.setFrame(True)
        self.ip.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ip.setObjectName("ip")
        self.ssh_comboBox = QtWidgets.QComboBox(self.connect)
        self.ssh_comboBox.setGeometry(QtCore.QRect(560, 200, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ssh_comboBox.sizePolicy().hasHeightForWidth())
        self.ssh_comboBox.setSizePolicy(sizePolicy)
        self.ssh_comboBox.setMinimumSize(QtCore.QSize(321, 0))
        self.ssh_comboBox.setObjectName("ssh_comboBox")
        self.username = QtWidgets.QLineEdit(self.connect)
        self.username.setGeometry(QtCore.QRect(560, 360, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QtCore.QSize(321, 0))
        self.username.setFrame(True)
        self.username.setObjectName("username")
        self.textBrowser_48 = QtWidgets.QTextBrowser(self.connect)
        self.textBrowser_48.setGeometry(QtCore.QRect(390, 90, 341, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_48.sizePolicy().hasHeightForWidth())
        self.textBrowser_48.setSizePolicy(sizePolicy)
        self.textBrowser_48.setMinimumSize(QtCore.QSize(341, 0))
        self.textBrowser_48.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_48.setObjectName("textBrowser_48")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.connect)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 360, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(321, 0))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.connect)
        self.textBrowser.setGeometry(QtCore.QRect(220, 200, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(321, 0))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.connect)
        self.textBrowser_4.setGeometry(QtCore.QRect(220, 420, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(321, 0))
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.connect)
        self.textBrowser_3.setGeometry(QtCore.QRect(220, 300, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(321, 0))
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.password = QtWidgets.QLineEdit(self.connect)
        self.password.setGeometry(QtCore.QRect(560, 420, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(321, 0))
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password.setObjectName("password")
        self.ssh_control_button = QtWidgets.QPushButton(self.connect)
        self.ssh_control_button.setEnabled(True)
        self.ssh_control_button.setGeometry(QtCore.QRect(770, 500, 111, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ssh_control_button.sizePolicy().hasHeightForWidth())
        self.ssh_control_button.setSizePolicy(sizePolicy)
        self.ssh_control_button.setMinimumSize(QtCore.QSize(111, 0))
        self.ssh_control_button.setCheckable(True)
        self.ssh_control_button.setChecked(False)
        self.ssh_control_button.setObjectName("ssh_control_button")
        Installer.addPage(self.connect)
        self.db = QtWidgets.QWizardPage()
        self.db.setObjectName("db")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.db)
        self.textBrowser_5.setGeometry(QtCore.QRect(210, 210, 321, 31))
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.db_name = QtWidgets.QLineEdit(self.db)
        self.db_name.setGeometry(QtCore.QRect(550, 210, 321, 31))
        self.db_name.setObjectName("db_name")
        self.db_password = QtWidgets.QLineEdit(self.db)
        self.db_password.setGeometry(QtCore.QRect(550, 330, 321, 31))
        self.db_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.db_password.setObjectName("db_password")
        self.db_username = QtWidgets.QLineEdit(self.db)
        self.db_username.setGeometry(QtCore.QRect(550, 270, 321, 31))
        self.db_username.setObjectName("db_username")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.db)
        self.textBrowser_6.setGeometry(QtCore.QRect(210, 270, 321, 31))
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_47 = QtWidgets.QTextBrowser(self.db)
        self.textBrowser_47.setGeometry(QtCore.QRect(380, 80, 341, 31))
        self.textBrowser_47.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_47.setObjectName("textBrowser_47")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.db)
        self.textBrowser_7.setGeometry(QtCore.QRect(210, 330, 321, 31))
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_7.setObjectName("textBrowser_7")
        Installer.addPage(self.db)
        self.ldap = QtWidgets.QWizardPage()
        self.ldap.setObjectName("ldap")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_13.setGeometry(QtCore.QRect(220, 510, 321, 31))
        self.textBrowser_13.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.l_config_user = QtWidgets.QLineEdit(self.ldap)
        self.l_config_user.setGeometry(QtCore.QRect(560, 450, 321, 31))
        self.l_config_user.setObjectName("l_config_user")
        self.l_base_dn = QtWidgets.QLineEdit(self.ldap)
        self.l_base_dn.setGeometry(QtCore.QRect(560, 210, 321, 31))
        self.l_base_dn.setObjectName("l_base_dn")
        self.l_admin_pwd = QtWidgets.QLineEdit(self.ldap)
        self.l_admin_pwd.setGeometry(QtCore.QRect(560, 390, 321, 31))
        self.l_admin_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.l_admin_pwd.setObjectName("l_admin_pwd")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_9.setGeometry(QtCore.QRect(220, 270, 321, 31))
        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.l_org_name = QtWidgets.QLineEdit(self.ldap)
        self.l_org_name.setGeometry(QtCore.QRect(560, 270, 321, 31))
        self.l_org_name.setObjectName("l_org_name")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_11.setGeometry(QtCore.QRect(220, 390, 321, 31))
        self.textBrowser_11.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.ldap_status = QtWidgets.QComboBox(self.ldap)
        self.ldap_status.setGeometry(QtCore.QRect(560, 160, 321, 31))
        self.ldap_status.setObjectName("ldap_status")
        self.ldap_status.addItem("")
        self.ldap_status.addItem("")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_16.setGeometry(QtCore.QRect(220, 160, 321, 31))
        self.textBrowser_16.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.lider_console_user = QtWidgets.QLineEdit(self.ldap)
        self.lider_console_user.setGeometry(QtCore.QRect(560, 570, 321, 31))
        self.lider_console_user.setObjectName("lider_console_user")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_10.setGeometry(QtCore.QRect(220, 330, 321, 31))
        self.textBrowser_10.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.lider_console_user_pwd = QtWidgets.QLineEdit(self.ldap)
        self.lider_console_user_pwd.setGeometry(QtCore.QRect(560, 630, 321, 31))
        self.lider_console_user_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lider_console_user_pwd.setObjectName("lider_console_user_pwd")
        self.l_config_admin_pwd = QtWidgets.QLineEdit(self.ldap)
        self.l_config_admin_pwd.setGeometry(QtCore.QRect(560, 510, 321, 31))
        self.l_config_admin_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.l_config_admin_pwd.setObjectName("l_config_admin_pwd")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_8.setGeometry(QtCore.QRect(220, 210, 321, 31))
        self.textBrowser_8.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_12.setGeometry(QtCore.QRect(220, 450, 321, 31))
        self.textBrowser_12.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_46 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_46.setGeometry(QtCore.QRect(390, 80, 341, 31))
        self.textBrowser_46.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_46.setObjectName("textBrowser_46")
        self.l_admin_cn = QtWidgets.QLineEdit(self.ldap)
        self.l_admin_cn.setGeometry(QtCore.QRect(560, 330, 321, 31))
        self.l_admin_cn.setObjectName("l_admin_cn")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_15.setGeometry(QtCore.QRect(220, 630, 321, 31))
        self.textBrowser_15.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.ldap)
        self.textBrowser_14.setGeometry(QtCore.QRect(220, 570, 321, 31))
        self.textBrowser_14.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_14.setObjectName("textBrowser_14")
        Installer.addPage(self.ldap)
        self.xmpp = QtWidgets.QWizardPage()
        self.xmpp.setObjectName("xmpp")
        self.e_service_name = QtWidgets.QLineEdit(self.xmpp)
        self.e_service_name.setGeometry(QtCore.QRect(570, 220, 321, 31))
        self.e_service_name.setObjectName("e_service_name")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_17.setGeometry(QtCore.QRect(230, 270, 321, 31))
        self.textBrowser_17.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.e_lider_username = QtWidgets.QLineEdit(self.xmpp)
        self.e_lider_username.setGeometry(QtCore.QRect(570, 450, 321, 31))
        self.e_lider_username.setObjectName("e_lider_username")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_20.setGeometry(QtCore.QRect(230, 390, 321, 31))
        self.textBrowser_20.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.e_username = QtWidgets.QLineEdit(self.xmpp)
        self.e_username.setGeometry(QtCore.QRect(570, 330, 321, 31))
        self.e_username.setObjectName("e_username")
        self.textBrowser_21 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_21.setGeometry(QtCore.QRect(230, 330, 321, 31))
        self.textBrowser_21.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.textBrowser_45 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_45.setGeometry(QtCore.QRect(390, 90, 341, 31))
        self.textBrowser_45.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_45.setObjectName("textBrowser_45")
        self.e_user_pwd = QtWidgets.QLineEdit(self.xmpp)
        self.e_user_pwd.setGeometry(QtCore.QRect(570, 390, 321, 31))
        self.e_user_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.e_user_pwd.setObjectName("e_user_pwd")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_18.setGeometry(QtCore.QRect(230, 220, 321, 31))
        self.textBrowser_18.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.ldap_servers = QtWidgets.QLineEdit(self.xmpp)
        self.ldap_servers.setGeometry(QtCore.QRect(570, 270, 321, 31))
        self.ldap_servers.setObjectName("ldap_servers")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_19.setGeometry(QtCore.QRect(230, 450, 321, 31))
        self.textBrowser_19.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.lider_sunucu_pwd_2 = QtWidgets.QLineEdit(self.xmpp)
        self.lider_sunucu_pwd_2.setGeometry(QtCore.QRect(570, 510, 321, 31))
        self.lider_sunucu_pwd_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lider_sunucu_pwd_2.setObjectName("lider_sunucu_pwd_2")
        self.textBrowser_22 = QtWidgets.QTextBrowser(self.xmpp)
        self.textBrowser_22.setGeometry(QtCore.QRect(230, 510, 321, 31))
        self.textBrowser_22.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_22.setObjectName("textBrowser_22")
        Installer.addPage(self.xmpp)
        self.fs = QtWidgets.QWizardPage()
        self.fs.setObjectName("fs")
        self.textBrowser_25 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_25.setGeometry(QtCore.QRect(230, 400, 321, 31))
        self.textBrowser_25.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_25.setObjectName("textBrowser_25")
        self.l_config_admin_dn_2 = QtWidgets.QLineEdit(self.fs)
        self.l_config_admin_dn_2.setGeometry(QtCore.QRect(570, 520, 321, 31))
        self.l_config_admin_dn_2.setObjectName("l_config_admin_dn_2")
        self.textBrowser_26 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_26.setGeometry(QtCore.QRect(230, 340, 321, 31))
        self.textBrowser_26.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.fs_plugin_path = QtWidgets.QLineEdit(self.fs)
        self.fs_plugin_path.setGeometry(QtCore.QRect(570, 400, 321, 31))
        self.fs_plugin_path.setObjectName("fs_plugin_path")
        self.textBrowser_24 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_24.setGeometry(QtCore.QRect(230, 220, 321, 31))
        self.textBrowser_24.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_24.setObjectName("textBrowser_24")
        self.textBrowser_28 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_28.setGeometry(QtCore.QRect(230, 280, 321, 31))
        self.textBrowser_28.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_28.setObjectName("textBrowser_28")
        self.textBrowser_23 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_23.setGeometry(QtCore.QRect(230, 460, 321, 31))
        self.textBrowser_23.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_23.setObjectName("textBrowser_23")
        self.fs_username_pwd = QtWidgets.QLineEdit(self.fs)
        self.fs_username_pwd.setGeometry(QtCore.QRect(570, 340, 321, 31))
        self.fs_username_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.fs_username_pwd.setObjectName("fs_username_pwd")
        self.file_server = QtWidgets.QLineEdit(self.fs)
        self.file_server.setGeometry(QtCore.QRect(570, 220, 321, 31))
        self.file_server.setObjectName("file_server")
        self.fs_agreement_path = QtWidgets.QLineEdit(self.fs)
        self.fs_agreement_path.setGeometry(QtCore.QRect(570, 460, 321, 31))
        self.fs_agreement_path.setObjectName("fs_agreement_path")
        self.fs_username = QtWidgets.QLineEdit(self.fs)
        self.fs_username.setGeometry(QtCore.QRect(570, 280, 321, 31))
        self.fs_username.setObjectName("fs_username")
        self.textBrowser_44 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_44.setGeometry(QtCore.QRect(380, 90, 341, 31))
        self.textBrowser_44.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_44.setObjectName("textBrowser_44")
        self.textBrowser_27 = QtWidgets.QTextBrowser(self.fs)
        self.textBrowser_27.setGeometry(QtCore.QRect(230, 520, 321, 31))
        self.textBrowser_27.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_27.setObjectName("textBrowser_27")
        Installer.addPage(self.fs)
        self.lider = QtWidgets.QWizardPage()
        self.lider.setObjectName("lider")
        self.textBrowser_42 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_42.setGeometry(QtCore.QRect(220, 630, 321, 30))
        self.textBrowser_42.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_42.setObjectName("textBrowser_42")
        self.fs_username_pwd_2 = QtWidgets.QLineEdit(self.lider)
        self.fs_username_pwd_2.setGeometry(QtCore.QRect(560, 510, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_username_pwd_2.sizePolicy().hasHeightForWidth())
        self.fs_username_pwd_2.setSizePolicy(sizePolicy)
        self.fs_username_pwd_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.fs_username_pwd_2.setObjectName("fs_username_pwd_2")
        self.file_server_2 = QtWidgets.QLineEdit(self.lider)
        self.file_server_2.setGeometry(QtCore.QRect(560, 430, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_server_2.sizePolicy().hasHeightForWidth())
        self.file_server_2.setSizePolicy(sizePolicy)
        self.file_server_2.setObjectName("file_server_2")
        self.textBrowser_40 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_40.setGeometry(QtCore.QRect(220, 550, 321, 30))
        self.textBrowser_40.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_40.setObjectName("textBrowser_40")
        self.textBrowser_36 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_36.setGeometry(QtCore.QRect(220, 150, 321, 30))
        self.textBrowser_36.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_36.setObjectName("textBrowser_36")
        self.textBrowser_32 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_32.setGeometry(QtCore.QRect(220, 350, 321, 30))
        self.textBrowser_32.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_32.setObjectName("textBrowser_32")
        self.fs_username_2 = QtWidgets.QLineEdit(self.lider)
        self.fs_username_2.setGeometry(QtCore.QRect(560, 470, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_username_2.sizePolicy().hasHeightForWidth())
        self.fs_username_2.setSizePolicy(sizePolicy)
        self.fs_username_2.setObjectName("fs_username_2")
        self.textBrowser_39 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_39.setGeometry(QtCore.QRect(220, 510, 321, 30))
        self.textBrowser_39.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_39.setObjectName("textBrowser_39")
        self.l_base_dn_2 = QtWidgets.QLineEdit(self.lider)
        self.l_base_dn_2.setGeometry(QtCore.QRect(560, 110, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_base_dn_2.sizePolicy().hasHeightForWidth())
        self.l_base_dn_2.setSizePolicy(sizePolicy)
        self.l_base_dn_2.setObjectName("l_base_dn_2")
        self.textBrowser_37 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_37.setGeometry(QtCore.QRect(220, 470, 321, 30))
        self.textBrowser_37.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_37.setObjectName("textBrowser_37")
        self.xmpp_sunucu = QtWidgets.QTextBrowser(self.lider)
        self.xmpp_sunucu.setGeometry(QtCore.QRect(220, 270, 321, 30))
        self.xmpp_sunucu.setFrameShape(QtWidgets.QFrame.Box)
        self.xmpp_sunucu.setObjectName("xmpp_sunucu")
        self.ejabberd_service = QtWidgets.QLineEdit(self.lider)
        self.ejabberd_service.setGeometry(QtCore.QRect(560, 390, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ejabberd_service.sizePolicy().hasHeightForWidth())
        self.ejabberd_service.setSizePolicy(sizePolicy)
        self.ejabberd_service.setObjectName("ejabberd_service")
        self.textBrowser_34 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_34.setGeometry(QtCore.QRect(220, 390, 321, 30))
        self.textBrowser_34.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_34.setObjectName("textBrowser_34")
        self.textBrowser_33 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_33.setGeometry(QtCore.QRect(220, 190, 321, 30))
        self.textBrowser_33.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_33.setObjectName("textBrowser_33")
        self.pushButton = QtWidgets.QPushButton(self.lider)
        self.pushButton.setGeometry(QtCore.QRect(770, 700, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_38 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_38.setGeometry(QtCore.QRect(220, 430, 321, 30))
        self.textBrowser_38.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_38.setObjectName("textBrowser_38")
        self.textBrowser_35 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_35.setGeometry(QtCore.QRect(220, 310, 321, 30))
        self.textBrowser_35.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_35.setObjectName("textBrowser_35")
        self.textBrowser_31 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_31.setGeometry(QtCore.QRect(220, 230, 321, 30))
        self.textBrowser_31.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_31.setObjectName("textBrowser_31")
        self.ldap_admin_cn = QtWidgets.QLineEdit(self.lider)
        self.ldap_admin_cn.setGeometry(QtCore.QRect(560, 150, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ldap_admin_cn.sizePolicy().hasHeightForWidth())
        self.ldap_admin_cn.setSizePolicy(sizePolicy)
        self.ldap_admin_cn.setObjectName("ldap_admin_cn")
        self.fs_plugin_path_2 = QtWidgets.QLineEdit(self.lider)
        self.fs_plugin_path_2.setGeometry(QtCore.QRect(560, 550, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_plugin_path_2.sizePolicy().hasHeightForWidth())
        self.fs_plugin_path_2.setSizePolicy(sizePolicy)
        self.fs_plugin_path_2.setObjectName("fs_plugin_path_2")
        self.fs_agent_files_path = QtWidgets.QLineEdit(self.lider)
        self.fs_agent_files_path.setGeometry(QtCore.QRect(560, 630, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_agent_files_path.sizePolicy().hasHeightForWidth())
        self.fs_agent_files_path.setSizePolicy(sizePolicy)
        self.fs_agent_files_path.setObjectName("fs_agent_files_path")
        self.textBrowser_43 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_43.setGeometry(QtCore.QRect(380, 50, 341, 31))
        self.textBrowser_43.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_43.setObjectName("textBrowser_43")
        self.lider_sunucu_pwd = QtWidgets.QLineEdit(self.lider)
        self.lider_sunucu_pwd.setGeometry(QtCore.QRect(560, 350, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lider_sunucu_pwd.sizePolicy().hasHeightForWidth())
        self.lider_sunucu_pwd.setSizePolicy(sizePolicy)
        self.lider_sunucu_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lider_sunucu_pwd.setObjectName("lider_sunucu_pwd")
        self.ldap_base = QtWidgets.QLineEdit(self.lider)
        self.ldap_base.setGeometry(QtCore.QRect(560, 230, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ldap_base.sizePolicy().hasHeightForWidth())
        self.ldap_base.setSizePolicy(sizePolicy)
        self.ldap_base.setObjectName("ldap_base")
        self.ldap_admin_pwd = QtWidgets.QLineEdit(self.lider)
        self.ldap_admin_pwd.setGeometry(QtCore.QRect(560, 190, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ldap_admin_pwd.sizePolicy().hasHeightForWidth())
        self.ldap_admin_pwd.setSizePolicy(sizePolicy)
        self.ldap_admin_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ldap_admin_pwd.setObjectName("ldap_admin_pwd")
        self.textBrowser_30 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_30.setGeometry(QtCore.QRect(220, 110, 321, 30))
        self.textBrowser_30.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_30.setObjectName("textBrowser_30")
        self.lider_sunucu = QtWidgets.QLineEdit(self.lider)
        self.lider_sunucu.setGeometry(QtCore.QRect(560, 310, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lider_sunucu.sizePolicy().hasHeightForWidth())
        self.lider_sunucu.setSizePolicy(sizePolicy)
        self.lider_sunucu.setObjectName("lider_sunucu")
        self.e_host = QtWidgets.QLineEdit(self.lider)
        self.e_host.setGeometry(QtCore.QRect(560, 270, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e_host.sizePolicy().hasHeightForWidth())
        self.e_host.setSizePolicy(sizePolicy)
        self.e_host.setObjectName("e_host")
        self.fs_agreement_path_2 = QtWidgets.QLineEdit(self.lider)
        self.fs_agreement_path_2.setGeometry(QtCore.QRect(560, 590, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_agreement_path_2.sizePolicy().hasHeightForWidth())
        self.fs_agreement_path_2.setSizePolicy(sizePolicy)
        self.fs_agreement_path_2.setObjectName("fs_agreement_path_2")
        self.textBrowser_41 = QtWidgets.QTextBrowser(self.lider)
        self.textBrowser_41.setGeometry(QtCore.QRect(220, 590, 321, 30))
        self.textBrowser_41.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_41.setObjectName("textBrowser_41")
        self.label = QtWidgets.QLabel(self.lider)
        self.label.setGeometry(QtCore.QRect(340, 700, 421, 21))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        Installer.addPage(self.lider)
        self.save = QtWidgets.QWizardPage()
        self.save.setObjectName("save")
        self.save_button = QtWidgets.QPushButton(self.save)
        self.save_button.setGeometry(QtCore.QRect(900, 720, 83, 24))
        self.save_button.setStyleSheet("")
        self.save_button.setObjectName("save_button")
        self.next_install_button = QtWidgets.QPushButton(self.save)
        self.next_install_button.setGeometry(QtCore.QRect(1030, 720, 83, 24))
        self.next_install_button.setStyleSheet("")
        self.next_install_button.setObjectName("next_install_button")
        Installer.addPage(self.save)
        self.watchlog = QtWidgets.QWizardPage()
        self.watchlog.setObjectName("watchlog")
        Installer.addPage(self.watchlog)

        self.retranslateUi(Installer)
        QtCore.QMetaObject.connectSlotsByName(Installer)

    def retranslateUi(self, Installer):
        _translate = QtCore.QCoreApplication.translate
        Installer.setWindowTitle(_translate("Installer", "Lider Ahenk Kolay Kurulum Uygulaması"))
        self.ip.setText(_translate("Installer", "192.168.56.1"))
        self.username.setText(_translate("Installer", "tcolak"))
        self.textBrowser_48.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Bağlantı Ayarları</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Kullanıcı Adı:</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Bileşenler Nereye Kurulsun?</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Kullanıcı Parolası</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Sunucu ip:</span></p></body></html>"))
        self.password.setText(_translate("Installer", "secret"))
        self.ssh_control_button.setText(_translate("Installer", "Bağlantı Kontrol"))
        self.textBrowser_5.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Veritabanı Adı:</span></p></body></html>"))
        self.db_name.setText(_translate("Installer", "liderdb"))
        self.db_password.setText(_translate("Installer", "secret"))
        self.db_username.setText(_translate("Installer", "root"))
        self.textBrowser_6.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Kullanıcı Adı:</span></p></body></html>"))
        self.textBrowser_47.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Veritabanı Sunucu Konfigürasyonu</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Kullanıcı Parolası:</span></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Config Admin Parolası</span></p></body></html>"))
        self.l_config_user.setText(_translate("Installer", "cn=admin,cn=config"))
        self.l_base_dn.setText(_translate("Installer", "liderahenk.org"))
        self.l_admin_pwd.setText(_translate("Installer", "secret"))
        self.textBrowser_9.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Organizasyon Adı:</span></p></body></html>"))
        self.l_org_name.setText(_translate("Installer", "ULAKBİM"))
        self.textBrowser_11.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Admin Parolası:</span></p></body></html>"))
        self.ldap_status.setItemText(0, _translate("Installer", "Yeni"))
        self.ldap_status.setItemText(1, _translate("Installer", "Güncelle"))
        self.textBrowser_16.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">LDAP İçin İşlem Seçiniz</span></p></body></html>"))
        self.lider_console_user.setText(_translate("Installer", "lider_console"))
        self.textBrowser_10.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Admin CN:</span></p></body></html>"))
        self.lider_console_user_pwd.setText(_translate("Installer", "secret"))
        self.l_config_admin_pwd.setText(_translate("Installer", "secret"))
        self.textBrowser_8.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">LDAP CN:</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Config Admin DN:</span></p></body></html>"))
        self.textBrowser_46.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">OpenLDAP Sunucu Konfigürasyonu</span></p></body></html>"))
        self.l_admin_cn.setText(_translate("Installer", "admin"))
        self.textBrowser_15.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Lider Arayüz Kullanıcı Parolası</span></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Lider Arayüz Kullanıcı Adı</span></p></body></html>"))
        self.e_service_name.setText(_translate("Installer", "im.liderahenk.org"))
        self.textBrowser_17.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">LDAP Sunucu Adresi</span></p></body></html>"))
        self.e_lider_username.setText(_translate("Installer", "lider_sunucu"))
        self.textBrowser_20.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Ejabberd Kullanıcı Parolası</span></p></body></html>"))
        self.e_username.setText(_translate("Installer", "admin"))
        self.textBrowser_21.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Ejabberd Kullanıcı Adı</span></p></body></html>"))
        self.textBrowser_45.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Ejabberd Sunucu Konfigürasyonu</span></p></body></html>"))
        self.e_user_pwd.setText(_translate("Installer", "secret"))
        self.textBrowser_18.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Ejabberd Servis Adı</span></p></body></html>"))
        self.ldap_servers.setText(_translate("Installer", "127.0.0.1"))
        self.textBrowser_19.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Lider Sunucu Kullanıcı Adı</span></p></body></html>"))
        self.lider_sunucu_pwd_2.setText(_translate("Installer", "secret"))
        self.textBrowser_22.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Lider Sunucu Kullanıcı Parolası</span></p></body></html>"))
        self.textBrowser_25.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Eklenti Yolu</span></p></body></html>"))
        self.l_config_admin_dn_2.setText(_translate("Installer", "/home/lider"))
        self.textBrowser_26.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Dosya Sunucu Kullanıcı Parolası</span></p></body></html>"))
        self.fs_plugin_path.setText(_translate("Installer", "/home/lider"))
        self.textBrowser_24.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Dosya Sunucu Adresi</span></p></body></html>"))
        self.textBrowser_28.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Dosya Sunucu Kullanıcı Adı</span></p></body></html>"))
        self.textBrowser_23.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Kullanıcı Sözleşmesi Yolu</span></p></body></html>"))
        self.fs_username_pwd.setText(_translate("Installer", "secret"))
        self.file_server.setText(_translate("Installer", "127.0.0.1"))
        self.fs_agreement_path.setText(_translate("Installer", "/home/lider"))
        self.fs_username.setText(_translate("Installer", "lider"))
        self.textBrowser_44.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Dosya Sunucu Konfigürasyonu</span></p></body></html>"))
        self.textBrowser_27.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Ahenk Dosyaları Yolu</span></p></body></html>"))
        self.textBrowser_42.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Ahenk Dosyaları Yolu</span></p></body></html>"))
        self.fs_username_pwd_2.setText(_translate("Installer", "secret"))
        self.file_server_2.setText(_translate("Installer", "127.0.0.1"))
        self.textBrowser_40.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Eklenti Yolu</span></p></body></html>"))
        self.textBrowser_36.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">LDAP Admin Kullanıcı Adı</span></p></body></html>"))
        self.textBrowser_32.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Ejabberd Lider Kullanıcı Parolası</span></p></body></html>"))
        self.fs_username_2.setText(_translate("Installer", "lider"))
        self.textBrowser_39.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Dosya Sunucu Kullanıcı Parolası</span></p></body></html>"))
        self.l_base_dn_2.setText(_translate("Installer", "127.0.0.1"))
        self.textBrowser_37.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Dosya Sunucu Kullanıcı Adı</span></p></body></html>"))
        self.xmpp_sunucu.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Ejabberd Sunucu Adresi</span></p></body></html>"))
        self.ejabberd_service.setText(_translate("Installer", "im.liderahenk.org"))
        self.textBrowser_34.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Ejabberd Servis Adı</span></p></body></html>"))
        self.textBrowser_33.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">LDAP Admin Kullanıcısı Parolası</span></p></body></html>"))
        self.pushButton.setText(_translate("Installer", "Verileri Getir"))
        self.textBrowser_38.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Dosya Sunucu Adresi</span></p></body></html>"))
        self.textBrowser_35.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Ejabberd Lider Kullanıcı Adı</span></p></body></html>"))
        self.textBrowser_31.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">LDAP Base DN</span></p></body></html>"))
        self.ldap_admin_cn.setText(_translate("Installer", "admin"))
        self.fs_plugin_path_2.setText(_translate("Installer", "/home/lider"))
        self.fs_agent_files_path.setText(_translate("Installer", "/home/lider"))
        self.textBrowser_43.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Lider Sunucu Konfigürasyonu</span></p></body></html>"))
        self.lider_sunucu_pwd.setText(_translate("Installer", "secret"))
        self.ldap_base.setText(_translate("Installer", "dc=liderahenk,dc=org"))
        self.ldap_admin_pwd.setText(_translate("Installer", "secret"))
        self.textBrowser_30.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">LDAP Sunucu Adresi</span></p></body></html>"))
        self.lider_sunucu.setText(_translate("Installer", "lider_sunucu"))
        self.e_host.setText(_translate("Installer", "127.0.0.1"))
        self.fs_agreement_path_2.setText(_translate("Installer", "/home/lider"))
        self.textBrowser_41.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Kullanıcı Sözleşmesi Yolu</span></p></body></html>"))
        self.label.setText(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Lider sunucu ayarlarını getirmek için butota tıklayınız.</span></p></body></html>"))
        self.save_button.setText(_translate("Installer", "Kaydet"))
        self.next_install_button.setText(_translate("Installer", "Kur"))

