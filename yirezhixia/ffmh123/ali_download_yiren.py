import os
import requests
from bs4 import BeautifulSoup

# 创建保存图片的目录
os.makedirs('/Users/heoo0124/Desktop/AA/YIREN/comics', exist_ok=True)
# base地址
base_url = "https://www.ffmh123.com"

# 一人之下的URL
index_url = "https://www.ffmh123.com/book/3137"

# 发送GET请求并获取响应
response = requests.get(index_url)

# 解析HTML文档
index_soup = BeautifulSoup(response.text, 'html.parser')

# 获取所有话的链接
chapter_links = index_soup.select('ul.detail-list-select > li > a')
chapters = {}
for item in chapter_links:    #遍历列表元素
        key = item.string        #提取键
        value = item['href']       #提取值
        chapters[key] = value  #添加键值对到字典

# 遍历每话的链接
for i, chapter_link in enumerate(chapter_links, start=1):
    # 获取每话的页面
    chapter_response = requests.get(chapter_link)
    chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')
    
    # 获取每话中的图片链接
    image_links = chapter_soup.select('div.content img[src^="http"]')['src']
    
    # 下载每张图片
    for j, image_link in enumerate(image_links, start=1):
        response = requests.get(image_link)
        filename = f'/Users/heoo0124/Desktop/AA/YIREN/comics/{i}_{j}.jpg'
        print(filename)
        with open(filename, 'wb') as f:
            f.write(response.content)