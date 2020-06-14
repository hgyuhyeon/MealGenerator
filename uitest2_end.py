from tkinter import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import dailydata2 as day


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
    print('아침') ##메뉴 프린트
    food = day.daily()
    day.makefoodata(food)

def btnClickListner2():
    print('점심') ##메뉴 프린트
    food = day.daily()
    day.makefoodata(food)

def btnClickListner3():
    print('저녁') ##메뉴 프린트
    food = day.daily()
    day.makefoodata(food)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())