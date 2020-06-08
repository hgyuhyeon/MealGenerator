#입력은 아무 값이나 써도 식단이 랜덤 출력됩니다.
#DB오류가 간혹 있습니다.
from tkinter import *
import pymysql

##connect to server##
con = pymysql.connect(host='localhost', user='user',
                password='123456**', db='foods', charset='utf8')
curs = con.cursor()

class daily:

    def __init__(self):
        self.kcal = 0
        self.protein = 0
        self.fat = 0
        self.carbohydrate = 0

        self.namelist = []  # 식단표 리스트
        self.catelist = []  # 카테고리 리스트
        self.nutlist = []  # 영양정보 리스트

    def getdata(self):
        sql = "SELECT * FROM nutrient ORDER BY RAND() LIMIT 1"
        curs.execute(sql)
        data = curs.fetchall()

        return data

    def convertdata(data):
        tup = data  # 튜플형인 데이터 가져오기
        templ = list(tup)  # 튜플을 리스트형으로 변환
        string = " ".join(str(templ))  # 리스트를 /로 구분지어 문자열로 변환
        l = string.split(",")  # 문자열을 다시 열이 구분된 리스트로 변환

        for j in range(0, 12, 1):
            l[j] = re.sub(r'[][''\()[]', '', l[j])  # 리스트 값의 각종 특수기호들을 제거
            l[j] = l[j].replace(" ", "")

        return l

    def makedata(self):

        for i in range(0, 4, 1):
            if(self.kcal >= 800):
                break
            data = daily.getdata(self)  # 데이터를 얻고
            l = daily.convertdata(data)  # 그 데이터를 리스트로 변환하여

            if str(l[3]).replace(" ", "") in self.catelist:
                continue  # 같은 카테의 데이터가 있으면 continue(거름)

            self.catelist.append(str(l[3]))
            self.namelist.append(str(l[0]))  # 식단표 안에 음식이름 추가
            self.kcal += float(l[8])
            self.protein += float(l[9])
            self.fat += float(l[10])
            self.carbohydrate += float(l[11])

        self.nutlist.append(self.kcal)
        self.nutlist.append(self.protein)
        self.nutlist.append(self.fat)
        self.nutlist.append(self.carbohydrate)


def printfoodata(food):
    print("메뉴: ")
    for i in range(len(food.namelist)):
        print(food.namelist[i])  # 메뉴 출력

    print('칼로리(kcal): ' + str(food.nutlist[0]))
    print('탄수화물: ' + str(food.nutlist[3]))
    print('단백질: ' + str(food.nutlist[1]))
    print('지방: ' + str(food.nutlist[2]))


if __name__ == "__main__":
    while(1):
        command = input("얻을 데이터(입력값 없을 시 종료): ")

        if(command == ""):
            break
        else:
            food = daily()
            food.makedata()
            printfoodata(food)

    con.close()
