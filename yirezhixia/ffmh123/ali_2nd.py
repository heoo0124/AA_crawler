import os
import requests
from bs4 import BeautifulSoup

# 漫画网站的URL
url = "https://www.ffmh123.com/chapter/346264"

# 发送GET请求并获取响应
response = requests.get(url)
#print(response.text)

# 解析HTML文档
soup = BeautifulSoup(response.text, 'html.parser')

pic_urls=[]
#detailList = soup.select('div[class]="imgpic" > img')
imgpic_list = soup.find_all(name='div',attrs={"class":"imgpic"})
i = 1
for img in soup.find(name='div',attrs={"class":"imgpic"}).find_all('img'):
    print(img.attrs['src'])
    response = requests.get(img.attrs['src'])
    filename = f'/Users/heoo0124/Desktop/AA/YIREN/comics/529_{i}.jpg'
    with open(filename, 'wb') as f:
            f.write(response.content)
    pic_urls.append(img.attrs['src'])#获取img标签的src属性，即图片网址
    i=i+1

# print(soup.find_all(name='div',attrs={"class":"imgpic"}))