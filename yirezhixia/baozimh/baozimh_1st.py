import requests
from bs4 import BeautifulSoup
import os

# 漫画网站的URL
chapter_url = f"https://www.hbmanga.com/comic/chapter/yirenzhixia-dongmantang/0_432.html"
chapter_response = requests.get(chapter_url)
# 解析HTML文档
chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')

imgpic_list = chapter_soup.find(name='ul',attrs={"class":"comic-contain"}).find_all('amp-img')

for img in imgpic_list:
    print(img['data-src'])








