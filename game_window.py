from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_game_window(object):
    def setupUi(self, game_window):
        game_window.setObjectName("game_window")
        game_window.resize(505, 365)
        self.centralwidget = QtWidgets.QWidget(game_window)
        self.centralwidget.setObjectName("centralwidget")
        self.list_game = QtWidgets.QListWidget(self.centralwidget)
        self.list_game.setGeometry(QtCore.QRect(20, 40, 351, 271))
        self.list_game.setObjectName("list_game")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_game.setObjectName("label_game")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(380, 40, 111, 23))
        self.button_add.setObjectName("button_add")
        self.button_remove = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove.setGeometry(QtCore.QRect(380, 70, 111, 23))
        self.button_remove.setObjectName("button_remove")
        game_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(game_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 21))
        self.menubar.setObjectName("menubar")
        game_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(game_window)
        self.statusbar.setObjectName("statusbar")
        game_window.setStatusBar(self.statusbar)

        self.retranslateUi(game_window)
        QtCore.QMetaObject.connectSlotsByName(game_window)

    def retranslateUi(self, game_window):
        _translate = QtCore.QCoreApplication.translate
        game_window.setWindowTitle(_translate("game_window", "Games"))
        self.label_game.setText(_translate("game_window", "Games:"))
        self.button_add.setText(_translate("game_window", "Add"))
        self.button_remove.setText(_translate("game_window", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_window = QtWidgets.QMainWindow()
    ui = Ui_game_window()
    ui.setupUi(game_window)
    game_window.show()
    sys.exit(app.exec_())
