#웹 타이틀 크롤링
import requests
import re
from bs4 import BeautifulSoup

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup.p.string)

#print(soup.find_all("h2"))  #원하는 부분 가져오기

#soup.select(".card-region-name")

#텍스트만 읽어오기
for x in range(0,10):
    print(soup.select(".card-title")[x].get_text())
