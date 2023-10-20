from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *

m = Organizer()
class Ui_MainWindow(QtWidgets.QDialog):    
    def open_add_profile_window(self):
        self.add_profile_window = QtWidgets.QMainWindow()
        self.add_profile_window_ui = Ui_profile_window()
        self.add_profile_window_ui.setupUi(self.add_profile_window)
        self.add_profile_window.show()

    def init_load(self):
        if m.Game_dict:
            self.dropdown_game.addItems(m.get_games())
            self.dropdown_profile.addItems(m.Game_dict[self.dropdown_game.currentText()].show_profile())
            self.section_view.addItems(m.Game_dict[self.dropdown_game.currentText()].get_sections(self.dropdown_profile.currentText()))
        else:
            pass    
    def refresh_main(self):
        if not m.Game_dict:
            self.dropdown_game.clear()
            self.dropdown_profile.clear()
            self.section_view.clear()
        elif self.dropdown_game.currentIndex() == -1:
            self.dropdown_game.addItems(m.get_games())
            self.dropdown_profile.clear()
            self.dropdown_profile.addItems(m.Game_dict[self.dropdown_game.currentText()].show_profile())
            self.section_view.addItems(m.Game_dict[self.dropdown_game.currentText()].get_sections(self.dropdown_profile.currentText()))
        else:
            try:
                li_g = self.dropdown_game.currentIndex()
                li_p = self.dropdown_profile.currentIndex()
                self.dropdown_game.clear()
                self.dropdown_game.addItems(m.get_games())
                self.dropdown_game.setCurrentIndex(li_g)
                self.dropdown_profile.clear()
                self.dropdown_profile.addItems(m.Game_dict[self.dropdown_game.currentText()].show_profile())
                self.dropdown_profile.setCurrentIndex(li_p)
                self.section_view.clear()
                self.section_view.addItems(m.Game_dict[self.dropdown_game.currentText()].get_sections(self.dropdown_profile.currentText()))
            except:
                self.dropdown_game.setCurrentIndex(0)
                self.dropdown_profile.setCurrentIndex(0)
                li_g = self.dropdown_game.currentIndex()
                li_p = self.dropdown_profile.currentIndex()
                self.dropdown_game.clear()
                self.dropdown_game.addItems(m.get_games())
                self.dropdown_game.setCurrentIndex(li_g)
                self.dropdown_profile.clear()
                self.dropdown_profile.addItems(m.Game_dict[self.dropdown_game.currentText()].show_profile())
                self.dropdown_profile.setCurrentIndex(li_p)
                self.section_view.clear()

    def add_section(self):
        name, _ = QtWidgets.QInputDialog.getText(
        self, 'Input Dialog', 'Enter Section name:')  
        if name:
            m.Game_dict[self.dropdown_game.currentText()].create_section(self.dropdown_profile.currentText(), name)
            self.refresh_main()

    def remove_section(self):
        name = self.section_view.currentItem()
        if name:
            qm = QtWidgets.QMessageBox
            ret = qm.question(self,'', "Are you you want to remove this secion? deleted secions cannot be recovered", qm.Yes | qm.No)
            if ret == qm.Yes:
                m.Game_dict[self.dropdown_game.currentText()].remove_section(self.dropdown_profile.currentText(), name.text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Success!")
                msg.setText("Action Successful!")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                _ = msg.exec_()
                self.refresh_main()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Failed!")
            msg.setText("Operation failed, did you select a section?")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            _ = msg.exec_()

    def import_save(self):
        m.Game_dict[self.dropdown_game.currentText()].import_save(self.dropdown_profile.currentText(), self.section_view.currentItem().text())
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Action Successful!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        _ = msg.exec_()

    def load_save(self):
        m.Game_dict[self.dropdown_game.currentText()].load_save(self.dropdown_profile.currentText(), self.section_view.currentItem().text())
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Action Successful!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        _ = msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dropdown_game = QtWidgets.QComboBox(self.centralwidget)
        self.dropdown_game.setGeometry(QtCore.QRect(20, 70, 251, 22))
        self.dropdown_game.setMouseTracking(False)
        self.dropdown_game.setObjectName("dropdown_game")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(20, 40, 111, 20))
        self.label_game.setObjectName("label_game")
        self.dropdown_profile = QtWidgets.QComboBox(self.centralwidget)
        self.dropdown_profile.setGeometry(QtCore.QRect(280, 70, 261, 22))
        self.dropdown_profile.setObjectName("dropdown_profile")
        self.label_profile = QtWidgets.QLabel(self.centralwidget)
        self.label_profile.setGeometry(QtCore.QRect(280, 40, 111, 20))
        self.label_profile.setObjectName("label_profile")
        self.button_profile = QtWidgets.QPushButton(self.centralwidget)
        self.button_profile.setGeometry(QtCore.QRect(554, 70, 91, 23))
        self.button_profile.setObjectName("button_profile")
        self.button_profile.clicked.connect(self.open_add_profile_window)
        self.button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_refresh.setGeometry(QtCore.QRect(20, 110, 111, 20))
        self.button_refresh.setObjectName("button_profile")
        self.button_refresh.clicked.connect(self.refresh_main)
        self.section_view = QtWidgets.QListWidget(self.centralwidget)
        self.section_view.setGeometry(QtCore.QRect(20, 140, 531, 331))
        self.section_view.setObjectName("section_view")
        self.button_import = QtWidgets.QPushButton(self.centralwidget)
        self.button_import.setGeometry(QtCore.QRect(20, 490, 231, 23))
        self.button_import.setObjectName("button_import")
        self.button_import.clicked.connect(self.import_save)
        self.button_load = QtWidgets.QPushButton(self.centralwidget)
        self.button_load.setGeometry(QtCore.QRect(320, 490, 231, 23))
        self.button_load.setObjectName("button_load")
        self.button_load.clicked.connect(self.load_save)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 140, 111, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 170, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_section)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 210, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.remove_section)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.init_load()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Universal Save Organizer"))
        self.label_game.setText(_translate("MainWindow", "Game:"))
        self.label_profile.setText(_translate("MainWindow", "Profile:"))
        self.button_profile.setText(_translate("MainWindow", "Edit profiles..."))
        self.button_import.setText(_translate("MainWindow", "Import savefile"))
        self.button_load.setText(_translate("MainWindow", "Load savefile"))
        self.label.setText(_translate("MainWindow", "Modify selected section"))
        self.pushButton.setText(_translate("MainWindow", "Add section"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove section"))
        self.button_refresh.setText(_translate("MainWindow", "Refesh window"))

class Ui_profile_window(QtWidgets.QDialog):
    def init_load(self):
        if m.Game_dict:
            self.box_games.addItems(m.get_games())
            self.list_profiles.addItems(m.Game_dict[self.box_games.currentText()].show_profile())
        else:
            pass

    def refresh(self):
        if not m.Game_dict:
            self.box_games.clear()
            self.list_profiles.clear()
        elif self.box_games.currentIndex() == -1:
            self.box_games.addItems(m.get_games())
            self.list_profiles.clear()
            self.list_profiles.addItems(m.Game_dict[self.box_games.currentText()].show_profile())
        else:
            li = self.box_games.currentIndex()
            self.box_games.clear()
            self.box_games.addItems(m.get_games())
            self.box_games.setCurrentIndex(li)
            self.list_profiles.clear()
            self.list_profiles.addItems(m.Game_dict[self.box_games.currentText()].show_profile())

    def add_profile(self):
        name, _ = QtWidgets.QInputDialog.getText(
        self, 'Input Dialog', 'Enter profile name:')  
        if name:
            m.Game_dict[self.box_games.currentText()].create_profile(name)
            self.refresh()

    def remove_profile(self):
        name = self.list_profiles.currentItem()
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Are you you want to remove this profile? deleted profiles cannot be recovered", qm.Yes | qm.No)
        if ret == qm.Yes:
            if name:
                m.Game_dict[self.box_games.currentText()].remove_profile(self.list_profiles.currentItem().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Success!")
                msg.setText("Action Successful!")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                _ = msg.exec_()
                self.refresh()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Failed!")
            msg.setText("Operation failed, did you select a profile?")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            _ = msg.exec_()

    def open_edit_game_window(self):
        self.edit_game_window = QtWidgets.QMainWindow()
        self.edit_game_window_ui = Ui_game_window()
        self.edit_game_window_ui.setupUi(self.edit_game_window)
        self.edit_game_window.show()

    def setupUi(self, profile_window):
        profile_window.setObjectName("profile_window")
        profile_window.resize(516, 395)
        self.centralwidget = QtWidgets.QWidget(profile_window)
        self.centralwidget.setObjectName("centralwidget")
        self.box_games = QtWidgets.QComboBox(self.centralwidget)
        self.box_games.setGeometry(QtCore.QRect(30, 40, 191, 22))
        self.box_games.setObjectName("box_games")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label_game.setObjectName("label_game")
        self.list_profiles = QtWidgets.QListWidget(self.centralwidget)
        self.list_profiles.setGeometry(QtCore.QRect(30, 100, 381, 251))
        self.list_profiles.setObjectName("list_profiles")
        self.button_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_new.setGeometry(QtCore.QRect(420, 120, 91, 23))
        self.button_new.setObjectName("button_new")
        self.button_new.clicked.connect(self.add_profile)
        self.button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete.setGeometry(QtCore.QRect(420, 210, 91, 23))
        self.button_delete.setObjectName("button_delete")
        self.button_delete.clicked.connect(self.remove_profile)
        self.button_edit = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit.setGeometry(QtCore.QRect(400, 40, 111, 23))
        self.button_edit.setObjectName("button_edit")
        self.button_edit.clicked.connect(self.open_edit_game_window)
        self.label_profile = QtWidgets.QLabel(self.centralwidget)
        self.label_profile.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_profile.setObjectName("label_profile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 100, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 190, 71, 16))
        self.label_2.setObjectName("label_2")
        self.button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_refresh.setGeometry(QtCore.QRect(230, 40, 75, 23))
        self.button_refresh.setObjectName("button_refresh")
        self.button_refresh.clicked.connect(self.refresh)
        profile_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(profile_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        profile_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(profile_window)
        self.statusbar.setObjectName("statusbar")
        profile_window.setStatusBar(self.statusbar)

        self.init_load()
        self.retranslateUi(profile_window)
        QtCore.QMetaObject.connectSlotsByName(profile_window)

    def retranslateUi(self, profile_window):
        _translate = QtCore.QCoreApplication.translate
        profile_window.setWindowTitle(_translate("profile_window", "Profiles"))
        self.label_game.setText(_translate("profile_window", "Game:"))
        self.button_new.setText(_translate("profile_window", "New profile"))
        self.button_delete.setText(_translate("profile_window", "Delete profile"))
        self.button_edit.setText(_translate("profile_window", "Edit games..."))
        self.label_profile.setText(_translate("profile_window", "Profiles:"))
        self.label.setText(_translate("profile_window", "Add profile"))
        # self.button_new_2.setText(_translate("profile_window", "2. Refresh"))
        self.label_2.setText(_translate("profile_window", "Delete profile"))
        # self.button_delete_2.setText(_translate("profile_window", "2. Refresh"))
        self.button_refresh.setText(_translate("profile_window", "Refresh"))

class Ui_game_window(object):
    def open_add_game_window(self):
        self.add_game_window = QtWidgets.QMainWindow()
        self.add_game_window_ui = Ui_add_game_window()
        self.add_game_window_ui.setupUi(self.add_game_window)
        self.add_game_window.show()

    def delete_game(self):
        if self.list_game.currentItem():
            m.remove_game(self.list_game.currentItem().text())
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Failed!")
            msg.setText("Operation failed, did you select a game?")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            _ = msg.exec_() 

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

class Ui_add_game_window(object):

    def open_game_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit_savefile.setText(file[0])
        return(file[0])
    
    def add_game(self):
        m.add_game(self.lineEdit_game.text(), self.lineEdit_savefile.text())
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
