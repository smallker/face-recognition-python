# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settingwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(324, 430)
        self.centralwidget = QtWidgets.QWidget(SettingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbSave = QtWidgets.QPushButton(self.centralwidget)
        self.pbSave.setGeometry(QtCore.QRect(160, 360, 61, 25))
        self.pbSave.setObjectName("pbSave")
        self.pbCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pbCancel.setGeometry(QtCore.QRect(230, 360, 71, 25))
        self.pbCancel.setObjectName("pbCancel")
        self.userid = QtWidgets.QTextEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(20, 80, 281, 31))
        self.userid.setObjectName("userid")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 281, 17))
        self.label.setObjectName("label")
        self.bot_token = QtWidgets.QTextEdit(self.centralwidget)
        self.bot_token.setGeometry(QtCore.QRect(20, 130, 281, 31))
        self.bot_token.setObjectName("bot_token")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 281, 17))
        self.label_2.setObjectName("label_2")
        self.db_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.db_ip.setGeometry(QtCore.QRect(20, 190, 281, 31))
        self.db_ip.setObjectName("db_ip")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 271, 20))
        self.label_3.setObjectName("label_3")
        self.db_user = QtWidgets.QTextEdit(self.centralwidget)
        self.db_user.setGeometry(QtCore.QRect(20, 240, 281, 31))
        self.db_user.setObjectName("db_user")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 271, 20))
        self.label_4.setObjectName("label_4")
        self.db_password = QtWidgets.QTextEdit(self.centralwidget)
        self.db_password.setGeometry(QtCore.QRect(20, 290, 281, 31))
        self.db_password.setObjectName("db_password")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 271, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 281, 17))
        self.label_6.setObjectName("label_6")
        self.camera_num = QtWidgets.QTextEdit(self.centralwidget)
        self.camera_num.setGeometry(QtCore.QRect(20, 30, 281, 31))
        self.camera_num.setObjectName("camera_num")
        self.pbDefault = QtWidgets.QPushButton(self.centralwidget)
        self.pbDefault.setGeometry(QtCore.QRect(20, 360, 61, 25))
        self.pbDefault.setObjectName("pbDefault")
        SettingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 22))
        self.menubar.setObjectName("menubar")
        SettingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingWindow)
        self.statusbar.setObjectName("statusbar")
        SettingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Settings"))
        self.pbSave.setText(_translate("SettingWindow", "Save"))
        self.pbCancel.setText(_translate("SettingWindow", "Cancel"))
        self.label.setText(_translate("SettingWindow", "Telegram chat ID"))
        self.label_2.setText(_translate("SettingWindow", "Bot token"))
        self.label_3.setText(_translate("SettingWindow", "Database IP"))
        self.label_4.setText(_translate("SettingWindow", "Database user"))
        self.label_5.setText(_translate("SettingWindow", "Database password"))
        self.label_6.setText(_translate("SettingWindow", "Camera num (0-5)"))
        self.pbDefault.setText(_translate("SettingWindow", "Default"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingWindow()
    ui.setupUi(SettingWindow)
    SettingWindow.show()
    sys.exit(app.exec_())
