import pymysql

# 1. 데이터베이스 연결
con = pymysql.connect(host='localhost', user='user',
                       password='123456**', db='foods', charset='utf8')

# 2. 커서 생성
curs = con.cursor()


# 3. SQL문 실행

#insert
#sql = "INSERT INTO rice (fname, kcal) VALUES(%s,%s)"
#value = (str(name), str(kcal))
#curs.execute(sql, value)
#con.commit()

#select
sql = "SELECT rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal FROM category ORDER by rand() limit 1"
curs.execute(sql)

# 4. 데이터 가져오기
data = curs.fetchall()


print("\n\n오늘의 랜덤식단!")
print(data)

# 5. 연결 끊기
con.close()
