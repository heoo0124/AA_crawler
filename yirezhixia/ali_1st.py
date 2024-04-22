import os
import requests
from bs4 import BeautifulSoup

# 漫画网站的URL
chapter_url = "https://www.ffmh123.com"
url = "https://www.ffmh123.com/book/3137"

# 发送GET请求并获取响应
response = requests.get(url)

# 解析HTML文档
soup = BeautifulSoup(response.text, 'html.parser')

detailList = soup.select('ul.detail-list-select > li > a')
# print(detailList)

# 获取所有话的链接
# chapter_links = list_to_map(detailList)
chapters = {}
for item in detailList:    #遍历列表元素
        key = item.string        #提取键
        value= item['href']       #提取值
        chapters[key] = value  #添加键值对到字典

# print(chapters)

# 打印每一话的URL
for name in chapters:
    print(name + ",下载地址：" + chapter_url + chapters[name])
print(chapter_url + chapters["529"])
response = requests.get(chapter_url + chapters["529"])
soup = BeautifulSoup(response.text, 'html.parser')















def list_to_map(detailList):
    result= {}              #创建空字典
    for item in detailList:    #遍历列表元素
        key = item.string        #提取键
        value= item['href']       #提取值
        result[key] = value  #添加键值对到字典
    return result           #返回转换后的字典