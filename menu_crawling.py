import requests
from bs4 import BeautifulSoup

print("여성, 뷰티")
print("1. 저칼로리 다이어트 2. 머슬업 다이어트 3. 디톡스 다이어트 4. 변비 5. 피부미용 6. 두피 모발 7. 빈혈예방 8. 골다공증 9. 갱년기 건강")
req = requests.get('https://www.10000recipe.com/theme/list.html?t1=101012')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_title3 = soup.select(
    'div.chef_cont > div > a'
)
for j in range(1, 10):
    print(j)
    for i in range(1, 7):
        req = requests.get('https://www.10000recipe.com/theme/view.html?theme=10101200'+str(j)+'&page={}'.format(i))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        my_titles = soup.select(
            'div > div.theme_list>a'
        )
        for title in my_titles:
            req = requests.get('https://www.10000recipe.com{}'.format(title.get('href')))
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            my_titles2 = soup.select(
                'div.view2_summary > h3'
            )
            for title2 in my_titles2:
                print(title2.text)

print("건강, 질병")
print("1. 위 건강 2. 장 건강 3. 스트레스 해소 4. 피로회복 5. 혈액순환 6. 호흡기 건강 7. 혈당조절 8. 노화방지 9. 암 예방")
req = requests.get('https://www.10000recipe.com/theme/list.html?t1=101014')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_title3 = soup.select(
    'div.chef_cont > div > a'
)
for j in range(1, 10):
    print(j)
    for i in range(1, 7):
        req = requests.get('https://www.10000recipe.com/theme/view.html?theme=10101400'+str(j)+'&page={}'.format(i))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        my_titles = soup.select(
            'div > div.theme_list>a'
        )
        for title in my_titles:
            req = requests.get('https://www.10000recipe.com{}'.format(title.get('href')))
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            my_titles2 = soup.select(
                'div.view2_summary > h3'
            )
            for title2 in my_titles2:
                print(title2.text)

