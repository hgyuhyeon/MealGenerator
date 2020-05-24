#블로그 검색 결과 중 100개 저장
import csv
import requests
import time
from bs4 import BeautifulSoup



def blog_crawling(page=1):
    url = "https://search.naver.com/search.naver?sm=tab_sug.top&where=post&query=%EB%8B%A8%EC%B2%B4%EA%B8%89%EC%8B%9D%EB%A9%94%EB%89%B4&oquery=%EA%B8%89%EC%8B%9D+%EB%A9%94%EB%89%B4&tqi=UVoJWsprvN8ssEC3Mfwssssssf4-097445&acq=%EA%B8%89%EC%8B%9D+%EB%A9%94%EB%89%B4&acr=1&qdt=0&sm=tab_pge&srchby=all&st=sim&where=post&start={}".format(page)


    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    blog_post_list = []

    for links in soup.select('li.sh_blog_top > dl'):
        title = links.select('dt > a')
        content = links.select('dd.sh_blog_passage')
        author = links.select('dd.txt_block a')

        title = title[0].get('title')
        content = content[0].text
        author = author[0].text
        blog_post = {'author': author, 'title': title, 'content': content}  # 블로그 데이터를 사전으로
        blog_post_list.append(blog_post)
    return blog_post_list

def save_data(blog_post):
    keys = blog_post[0].keys()
    with open('백종원 레시피_crawling2.csv', 'w') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(blog_post)

blog_post_list = []
for i in range(1, 100, 10):
    blog_post_list.extend( blog_crawling(page=i) )
    time.sleep(2)

save_data(blog_post_list)
