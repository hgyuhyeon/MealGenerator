from tkinter import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('아침', self)
        btn1.clicked.connect(btnClickListner1)
        btn2 = QPushButton('점심', self)
        btn2.clicked.connect(btnClickListner2)
        btn3 = QPushButton('저녁', self)
        btn3.clicked.connect(btnClickListner3)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('자동화 식단표')
        self.setGeometry(300, 300, 300, 200)
        self.show()


def btnClickListner1():
    print('click') ##메뉴 프린트

def btnClickListner2():
    print('click') ##메뉴 프린트

def btnClickListner3():
    print('click') ##메뉴 프린트

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

