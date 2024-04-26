import requests
import time
import random
from bs4 import BeautifulSoup
import os

target_path = "/Users/heoo0124/Desktop/AA/YIREN/bzmh/"
# 请求头模拟浏览器行为，降低被识别为爬虫的风险
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# 漫画网站的URL
for i in range(0, 800):  # 去掉无意义的循环，直接从248开始
    if(i<647):
        i+=1
        continue
    chapter_url = f"https://www.hbmanga.com/comic/chapter/yirenzhixia-dongmantang/0_{i}.html"
    try:
        chapter_response = requests.get(chapter_url, headers=headers)
    except requests.exceptions.RequestException as e:
        time.sleep(2)
        print(f"章节{i}下载失败重试！！！")
        chapter_response = requests.get(chapter_url, headers=headers)

    # 解析HTML文档
    chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')
    chapter_name = chapter_soup.select('title')[0].text.split(' - ')[0].replace("/", "-")
    chapter_path = target_path + chapter_name
    os.makedirs(chapter_path, exist_ok=True)
    print(chapter_name)
    imgpic_list = chapter_soup.find(name='ul',attrs={"class":"comic-contain"}).find_all('amp-img')
    for k,img in enumerate(imgpic_list):
        img_url = img['data-src']
        print(f'索引{i}_章节{chapter_name}_图{k+1}:{img_url}')
        # print(f'{chapter_path}/{chapter_name}_{k+1}.jpg')
        try:
            img_response = requests.get(img_url, headers=headers)
        except requests.exceptions.RequestException as e:
            time.sleep(2)
            print(f"章节{i}下载失败重试: {chapter_name}_{k+1}.jpg")
            img_response = requests.get(img_url, headers=headers)
        filename = f'{chapter_path}/{chapter_name}_{k+1}.jpg'
        with open(filename, 'wb') as f:
            f.write(img_response.content)
    # 随机等待0.5秒到1.5秒之间
    if(i%random.uniform(3, 7)==0):
        time.sleep(random.uniform(0.5, 1.5))  








