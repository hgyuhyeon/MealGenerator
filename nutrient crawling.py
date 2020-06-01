import requests
from bs4 import BeautifulSoup

for i in range(1, 279):
    print(i)
    req = requests.get('https://terms.naver.com/list.nhn?cid=42800&categoryId=60463&page={}'.format(i))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    for j in range(1, 16):
        my_titles = soup.select(
            'div.list_wrap > ul > li:nth-child({})'.format(j) + '> div > p'
        )
        my_title2 = soup.select(
            'div.list_wrap > ul > li:nth-child({})'.format(j) + '> div.info_area> div.subject > strong >a:nth-child(1)'
        )
        for title2 in my_title2:
            print(title2.text)
        for title in my_titles:
            print(title.text)
