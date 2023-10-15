# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_add_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Main import Organizer, Game

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 215)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_browse = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_browse.setGeometry(QtCore.QRect(160, 100, 25, 19))
        self.toolButton_browse.setObjectName("toolButton_browse")
        self.lineEdit_game = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_game.setGeometry(QtCore.QRect(40, 40, 113, 20))
        self.lineEdit_game.setObjectName("lineEdit_game")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label_game.setObjectName("label_game")
        self.lineEdit_savefile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_savefile.setGeometry(QtCore.QRect(40, 100, 113, 20))
        self.lineEdit_savefile.setObjectName("lineEdit_savefile")
        self.label_save = QtWidgets.QLabel(self.centralwidget)
        self.label_save.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.label_save.setObjectName("label_save")
        self.Button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ok.setGeometry(QtCore.QRect(40, 140, 75, 23))
        self.Button_ok.setObjectName("Button_ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 244, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_browse.setText(_translate("MainWindow", "..."))
        self.label_game.setText(_translate("MainWindow", "Game Name"))
        self.label_save.setText(_translate("MainWindow", "Savefile location"))
        self.Button_ok.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())