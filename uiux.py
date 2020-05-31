from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
def func_open1() :
    window = Tk()
    window.geometry("400x200")
    window.title("아침 식단표 생성")

    mainMenu = Menu(window)
    window.config(menu=mainMenu)
    effectMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "영양 정보", menu=effectMenu)

    effectMenu.add_command(label = "칼로리 정보", command=func_kcal)




def func_open2() :
    window = Tk()
    window.geometry("400x200")
    window.title("점심 식단표 생성")

    mainMenu = Menu(window)
    window.config(menu=mainMenu)
    effectMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "영양 정보", menu=effectMenu)

    effectMenu.add_command(label = "칼로리 정보", command=func_kcal)

def func_open3() :
    window = Tk()
    window.geometry("400x200")
    window.title("저녁 식단표 생성")

    mainMenu = Menu(window)
    window.config(menu=mainMenu)
    effectMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "영양 정보", menu=effectMenu)

    effectMenu.add_command(label = "칼로리 정보", command=func_kcal)

def func_exit() :
    window.quit()
    window.destroy()

def func_kcal() :
    window = Tk()
    window.geometry("200x400")
    window.title("영양 정보")
    

## 메인 코드  부분 ##
window = Tk()
window.geometry("400x400")
window.title("다이어트 식단표")

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "식단표", menu=fileMenu)

fileMenu.add_command(label = "아침 식단표", command=func_open1)
fileMenu.add_separator()
fileMenu.add_command(label = "점심 식단표", command=func_open2)
fileMenu.add_separator()
fileMenu.add_command(label = "저녁 식단표", command=func_open3)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command=func_exit)

window.mainloop()
