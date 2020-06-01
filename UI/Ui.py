import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt
from PyQt5 import uic

form_window = uic.loadUiType("ui_files/window.ui")[0]
form_female = uic.loadUiType("ui_files/female.ui")[0]
form_body=uic.loadUiType("ui_files/body.ui")[0]
form_diet=uic.loadUiType("ui_files/diet.ui")[0]

class MyMainWindow(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.female.clicked.connect(self.fem_clicked)
        self.body.clicked.connect(self.body_clicked)
        self.diet.clicked.connect(self.diet_clicked)

    def fem_clicked(self):
        fem_menu(self)

    def body_clicked(self):
        body_menu(self)

    def diet_clicked(self):
        diet_menu(self)

class fem_menu(QDialog, form_female):
    def __init__(self,parent):
        super(fem_menu,self).__init__(parent)
        self.setupUi(self)
        self.show()

class body_menu(QDialog, form_body):
    def __init__(self,parent):
        super(body_menu,self).__init__(parent)
        self.setupUi(self)
        self.show()

class diet_menu(QDialog, form_diet):
    def __init__(self,parent):
        super(diet_menu,self).__init__(parent)
        self.setupUi(self)
        self.show()

if __name__=='__main__':  # name : 현재 모듈의 이름이 저장되는 내장변수, 여기서 name==team_
    app=QApplication(sys.argv)  # 객체 생성
    myWindow=MyMainWindow()
    myWindow.show()
    app.exec_()