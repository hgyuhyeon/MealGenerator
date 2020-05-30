#조건 추가 필요 - 같은 카테고리의 음식이 선택되었을 때 거르기
from tkinter import *
import pymysql




def isfull(kcal): # 칼로리가 전부 찼는가?
    if(kcal>300):
        return True
    else:
        return False

def getdata():
    sql = "SELECT * FROM material WHERE category NOT IN ('주류','커피','떡','과자류') ORDER BY RAND() LIMIT 1"
    curs.execute(sql)
    data = curs.fetchall()

    return data


def convertdata(data):
    tup = getdata()  # 튜플형인 데이터 가져오기
    templ = list(tup)  # 튜플을 리스트형으로 변환
    string = " ".join(str(templ))  # 리스트를 /로 구분지어 문자열로 변환
    l = string.split(",")  # 문자열을 다시 열이 구분된 리스트로 변환

    for j in range(0, 5, 1):
        l[j] = re.sub('[][]', '', l[j])  # 리스트 값의 각종 특수기호들을 제거

    return l


class daily:
    def __init__(self):
        self.namelist = []
        self.kcal = 0

    def makedata(kcal):
        while(kcal <= 300):
            data = getdata()  # 데이터를 얻고
            l = convertdata(data)  # 그 데이터를 리스트로 변환하여
            namelist.append(str(l[1].replace(" ", "")))  # 식단표 안에 음식이름 추가
            kcal += float(l[2].replace(" ", ""))

            if(isfull(kcal)==True):
                namelist.append(kcal)
                break

        return namelist

    def makelist(self):
        print("\n\n오늘의 랜덤식단!")
        daily.printonedaydata(self)
        #print(kcal)

    def printonedaydata(self):
        for i in range(0, 3, 1):
            if (i==0):
                print("아침")
            elif (i==1):
                print("점심")
            else:
                print("저녁")
            once = daily.makedata(kcal)
            print(once)
            # print(kcal)
            del once[:]


class weekly:
    def makelist(self):
        print("\n\n이번 주 랜덤식단!")
        for i in range(0, 7, 1):
            daily.printonedaydata(self)

class monthly:
    def makelist(self):
        print("\n\n이번 달 랜덤식단!")
        for i in range(1, 5, 1):
            print(str(i)+"주차")
            for j in range(0, 7, 1):
                daily.printonedaydata(self)

if __name__ == "__main__":
    ##connect to server##
    con = pymysql.connect(host='localhost', user='user',
                           password='123456**', db='foods', charset='utf8')
    curs = con.cursor()

    while(1):
        command = input("얻을 데이터(d: 일일, w: 주간, m: 월간, 입력값 없을 시 종료): ")
        ##변수 선언##
        namelist = []  # 식단표 리스트
        kcal = 0

        if(command == "d"):
            daily.makelist("")
        elif(command == "w"):
            weekly.makelist("")
        elif(command == "m"):
           monthly.makelist("")
        elif(command == ""):
            break
        else:
            print("잘못된 입력")



    #insert - 크롤링 데이터 insert
    #sql = "INSERT INTO rice (fname, kcal) VALUES(%s,%s)"
    #value = (str(name), str(kcal))
    #curs.execute(sql, value)
    #con.commit()


    # 5. 연결 끊기
    con.close()
