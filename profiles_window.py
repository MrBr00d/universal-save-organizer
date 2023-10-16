# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profiles_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profile_window(object):
    def setupUi(self, profile_window):
        profile_window.setObjectName("profile_window")
        profile_window.resize(516, 395)
        self.centralwidget = QtWidgets.QWidget(profile_window)
        self.centralwidget.setObjectName("centralwidget")
        self.box_games = QtWidgets.QComboBox(self.centralwidget)
        self.box_games.setGeometry(QtCore.QRect(30, 40, 191, 22))
        self.box_games.setObjectName("box_games")
        self.box_games.addItem("")
        self.box_games.addItem("")
        self.box_games.addItem("")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label_game.setObjectName("label_game")
        self.list_profiles = QtWidgets.QListWidget(self.centralwidget)
        self.list_profiles.setGeometry(QtCore.QRect(30, 100, 381, 251))
        self.list_profiles.setObjectName("list_profiles")
        self.button_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_new.setGeometry(QtCore.QRect(420, 120, 91, 23))
        self.button_new.setObjectName("button_new")
        self.button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete.setGeometry(QtCore.QRect(420, 210, 91, 23))
        self.button_delete.setObjectName("button_delete")
        self.button_edit = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit.setGeometry(QtCore.QRect(230, 40, 111, 23))
        self.button_edit.setObjectName("button_edit")
        self.label_profile = QtWidgets.QLabel(self.centralwidget)
        self.label_profile.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_profile.setObjectName("label_profile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 100, 71, 16))
        self.label.setObjectName("label")
        self.button_new_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_new_2.setGeometry(QtCore.QRect(420, 150, 91, 23))
        self.button_new_2.setObjectName("button_new_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 190, 71, 16))
        self.label_2.setObjectName("label_2")
        self.button_delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_2.setGeometry(QtCore.QRect(420, 240, 91, 23))
        self.button_delete_2.setObjectName("button_delete_2")
        profile_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(profile_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        profile_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(profile_window)
        self.statusbar.setObjectName("statusbar")
        profile_window.setStatusBar(self.statusbar)

        self.retranslateUi(profile_window)
        QtCore.QMetaObject.connectSlotsByName(profile_window)

    def retranslateUi(self, profile_window):
        _translate = QtCore.QCoreApplication.translate
        profile_window.setWindowTitle(_translate("profile_window", "Profiles"))
        self.box_games.setItemText(0, _translate("profile_window", "Game 1"))
        self.box_games.setItemText(1, _translate("profile_window", "Game 2"))
        self.box_games.setItemText(2, _translate("profile_window", "Game 3"))
        self.label_game.setText(_translate("profile_window", "Game:"))
        self.button_new.setText(_translate("profile_window", "1. New profile"))
        self.button_delete.setText(_translate("profile_window", "1. Delete profile"))
        self.button_edit.setText(_translate("profile_window", "Edit games..."))
        self.label_profile.setText(_translate("profile_window", "Profiles:"))
        self.label.setText(_translate("profile_window", "Add profile"))
        self.button_new_2.setText(_translate("profile_window", "2. Refresh"))
        self.label_2.setText(_translate("profile_window", "Delete profile"))
        self.button_delete_2.setText(_translate("profile_window", "2. Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_window = QtWidgets.QMainWindow()
    ui = Ui_profile_window()
    ui.setupUi(profile_window)
    profile_window.show()
    sys.exit(app.exec_())
