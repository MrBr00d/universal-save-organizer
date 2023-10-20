from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_game_window(object):
    def open_add_game_window(self):
        self.add_game_window = QtWidgets.QMainWindow()
        self.add_game_window_ui = Ui_add_game_window()
        self.add_game_window_ui.setupUi(self.add_game_window)
        self.add_game_window.show()

    def delete_game(self):
        m.remove_game(self.list_game.currentItem().text()) #m (organizer) needs to be instantiated at the start of the script

    def refresh(self):
        self.list_game.clear()
        self.list_game.addItems(m.get_games())

    def setupUi(self, game_window):
        game_window.setObjectName("game_window")
        game_window.resize(505, 365)
        self.centralwidget = QtWidgets.QWidget(game_window)
        self.centralwidget.setObjectName("centralwidget")
        self.list_game = QtWidgets.QListWidget(self.centralwidget)
        self.list_game.setGeometry(QtCore.QRect(20, 40, 351, 271))
        self.list_game.setObjectName("list_game")
        self.list_game.addItems(m.get_games())
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_game.setObjectName("label_game")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(380, 60, 111, 23))
        self.button_add.setObjectName("button_add")
        self.button_add.clicked.connect(self.open_add_game_window)
        self.button_remove = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove.setGeometry(QtCore.QRect(380, 150, 111, 23))
        self.button_remove.setObjectName("button_remove")
        self.button_remove.clicked.connect(self.delete_game)
        self.label_add = QtWidgets.QLabel(self.centralwidget)
        self.label_add.setGeometry(QtCore.QRect(380, 40, 61, 16))
        self.label_add.setObjectName("label_add")
        self.label_remove = QtWidgets.QLabel(self.centralwidget)
        self.label_remove.setGeometry(QtCore.QRect(380, 130, 81, 16))
        self.label_remove.setObjectName("label_remove")
        self.button_add_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_2.setGeometry(QtCore.QRect(380, 90, 111, 23))
        self.button_add_2.setObjectName("button_add_2")
        self.button_add_2.clicked.connect(self.refresh)
        self.button_remove_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove_2.setGeometry(QtCore.QRect(380, 180, 111, 23))
        self.button_remove_2.setObjectName("button_remove_2")
        self.button_remove_2.clicked.connect(self.refresh)
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
        self.button_add.setText(_translate("game_window", "1. Add game"))
        self.button_remove.setText(_translate("game_window", "1. Remove game"))
        self.label_add.setText(_translate("game_window", "Add game"))
        self.label_remove.setText(_translate("game_window", "Remove game"))
        self.button_add_2.setText(_translate("game_window", "2. Refresh list"))
        self.button_remove_2.setText(_translate("game_window", "2. Refresh list"))
