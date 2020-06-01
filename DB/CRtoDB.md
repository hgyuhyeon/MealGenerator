# 크롤링 데이터의 DB insert manual.
기타 자료형은 직접 말하기

1. sql = "INSERT INTO (tablename) (foodname, kcal) VALUES(%s,%s)"
2. value = (str(name), str(kcal)) < 자료형별 수정 위치
3. curs.execute(sql, value)
4. con.commit()


# for int, float, double, etc number
value = (str(foodname), str(kcal))

# for tuple
사용 모듈: tkinter
templist = list(tuple)  # 튜플을 리스트형으로 변환

string = " ".join(str(templist))  # 리스트를 /로 구분지어 문자열로 변환

l = string.split(",")  # 문자열을 다시 열이 구분된 리스트로 변환

for j in range(0, 2, 1):
    l[j] = re.sub('[][]', '', l[j])  # 리스트 값의 각종 특수기호들을 제거
    
value = (str(l[0]), str(l[1]))

# for list
value = (str(l[0]), str(l[1]))
