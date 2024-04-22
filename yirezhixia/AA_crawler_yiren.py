import os
import requests
from bs4 import BeautifulSoup
import time

# base
yiren_url = "http://pp1.tupian.run/static/upload/book/3137/cover.jpg"
base_url = "https://www.ffmh123.com"
target_path = "/Users/heoo0124/Desktop/AA/YIREN/comics/"

# 一人之下的URL
index_url = "https://www.ffmh123.com/book/3137"

# 发送GET请求并获取响应
index_response = requests.get(index_url)

# 解析HTML文档
index_soup = BeautifulSoup(index_response.text, 'html.parser')

# 获取所有话
chapter_links = index_soup.select('ul.detail-list-select > li > a')

k = 0   

for item in chapter_links:
    k=k+1                                      #遍历列表元素
    chapter_name = item.string                              #本话的名字
    # if(chapter_name == "1.姐姐1"):continue
    if(k<200):continue
    chapter_url = base_url + item['href']                   #本话的地址
    chapter_response = requests.get(chapter_url)
    # 解析HTML文档
    chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')
    chapter_path = target_path + chapter_name
    os.makedirs(chapter_path, exist_ok=True)
    i = 1

    for img in chapter_soup.find(name='div',attrs={"class":"imgpic"}).find_all('img'):
        img_url = ""
        for key in img.attrs:
            if(key == "class"):continue
            # test = img.attrs[key]
            # j = img.attrs[key].find("http")
            if(img.attrs[key].find("http")==0):
                    img_url = img.attrs[key]
                    break
        #img_url = img.attrs['src'] if img.attrs['src'].find("http") == 1 else img.attrs['data-original']
        print(img_url)
        if(len(img_url)==0):
                print("========")
        try:
            img_response = requests.get(img_url)
        except BaseException:
            print("Error: 获取图片{chapter_name}_{i}.jpg失败")
            img_response = requests.get(yiren_url)
            filename = f'{chapter_path}/fail_{img_url}_{i}.jpg'
            with open(filename, 'wb') as f:
                f.write(img_response.content)
            i=i+1
            continue

        filename = f'{chapter_path}/{chapter_name}_{i}.jpg'
        with open(filename, 'wb') as f:
            f.write(img_response.content)
        i=i+1
        #time.sleep(1)
    

