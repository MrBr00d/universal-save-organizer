from PyQt5 import QtCore, QtGui, QtWidgets
from game_add_window import Ui_add_game_window
from Main import Organizer, Game
m = Organizer()
class Ui_game_window(object):
    # m = Organizer()

    def refresh(self):
        self.list_game.clear()
        self.list_game.addItems(m.get_games())

    def open_add_game_window(self):
        self.add_game_window = QtWidgets.QMainWindow()
        self.add_game_window_ui = Ui_add_game_window()
        self.add_game_window_ui.setupUi(self.add_game_window)
        self.add_game_window.show()
        
    def delete_game(self):
        m.remove_game(self.list_game.currentItem().text())
        self.refresh()

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
        self.button_add.setGeometry(QtCore.QRect(380, 40, 111, 23))
        self.button_add.setObjectName("button_add")
        self.button_add.clicked.connect(self.open_add_game_window)
        self.button_remove = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove.setGeometry(QtCore.QRect(380, 70, 111, 23))
        self.button_remove.setObjectName("button_remove")
        self.button_remove.clicked.connect(self.delete_game)
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

class Ui_add_game_window(object):
    def open_game_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit_savefile.setText(file[0])
        return(file[0])
    
    def add_game(self):
        m.add_game(self.lineEdit_game.text(), self.lineEdit_savefile.text())
        Ui_game_window.refresh(ui)
        self.add_game_window.close()

    def setupUi(self, add_game_window):
        self.add_game_window = add_game_window
        add_game_window.setObjectName("add_game_window")
        add_game_window.resize(446, 215)
        self.centralwidget = QtWidgets.QWidget(add_game_window)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_browse = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_browse.setGeometry(QtCore.QRect(400, 100, 25, 19))
        self.toolButton_browse.setObjectName("toolButton_browse")
        self.toolButton_browse.clicked.connect(self.open_game_file)
        self.lineEdit_game = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_game.setGeometry(QtCore.QRect(40, 40, 351, 20))
        self.lineEdit_game.setObjectName("lineEdit_game")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label_game.setObjectName("label_game")
        self.lineEdit_savefile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_savefile.setGeometry(QtCore.QRect(40, 100, 351, 20))
        self.lineEdit_savefile.setObjectName("lineEdit_savefile")
        self.label_save = QtWidgets.QLabel(self.centralwidget)
        self.label_save.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.label_save.setObjectName("label_save")
        self.Button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ok.setGeometry(QtCore.QRect(40, 140, 75, 23))
        self.Button_ok.setObjectName("Button_ok")
        self.Button_ok.clicked.connect(self.add_game)
        add_game_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_game_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 21))
        self.menubar.setObjectName("menubar")
        add_game_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_game_window)
        self.statusbar.setObjectName("statusbar")
        add_game_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_game_window)
        QtCore.QMetaObject.connectSlotsByName(add_game_window)

    def retranslateUi(self, add_game_window):
        _translate = QtCore.QCoreApplication.translate
        add_game_window.setWindowTitle(_translate("add_game_window", "Add game"))
        self.toolButton_browse.setText(_translate("add_game_window", "..."))
        self.label_game.setText(_translate("add_game_window", "Game Name"))
        self.label_save.setText(_translate("add_game_window", "Savefile location"))
        self.Button_ok.setText(_translate("add_game_window", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_window = QtWidgets.QMainWindow()
    ui = Ui_game_window()
    ui.setupUi(game_window)
    game_window.show()
    sys.exit(app.exec_())
