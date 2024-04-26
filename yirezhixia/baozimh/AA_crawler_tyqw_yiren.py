import os
import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin

# 目标路径
target_path = "/Users/heoo0124/Desktop/AA/YIREN/bzmh/"

# 请求头模拟浏览器行为，降低被识别为爬虫的风险
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 遍历章节
for i in range(248, 700):  # 去掉无意义的循环，直接从248开始
    chapter_url = f"https://www.hbmanga.com/comic/chapter/yirenzhixia-dongmantang/0_{i}.html"
    try:
        chapter_response = requests.get(chapter_url, headers=headers)
        chapter_response.raise_for_status()  # 如果响应状态不是200，抛出HTTPError异常

        # 解析HTML文档
        chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')

        # 更稳健地获取章节名，例如从HTML中的特定元素或URL中提取
        chapter_name = chapter_name = chapter_soup.select('title')[0]
        
        # 为章节名做清理，确保符合文件路径要求
        cleaned_chapter_name = chapter_soup.select('title')[0].text.split(' - ')[0]  # 示例清理操作，根据实际需要调整
        chapter_path = os.path.join(target_path, cleaned_chapter_name)
        os.makedirs(chapter_path, exist_ok=True)

        print(chapter_name)

        # 获取图片列表
        imgpic_list = chapter_soup.find(name='ul', attrs={"class": "comic-contain"}).find_all('amp-img')

        for k, img in enumerate(imgpic_list):
            img_url = urljoin(chapter_url, img['data-src'])  # 绝对化图片URL，防止相对路径问题
            print(f"索引{i}_章节{chapter_name}_图{i}:{img_url}")

            img_response = requests.get(img_url, headers=headers)
            img_response.raise_for_status()

            # 使用章节编号和图片序号作为文件名
            filename = f"{i}_{k+1}.jpg"
            filepath = os.path.join(chapter_path, filename)

            with open(filepath, 'wb') as f:
                f.write(img_response.content)

            # 设置请求间隔，避免过于频繁请求
            time.sleep(random.uniform(0.1, 0.5))  # 示例：随机等待0.5秒到1.5秒之间

    except requests.exceptions.RequestException as e:
        print(f"章节{i}下载失败: {e}")
        continue  # 跳过当前章节，继续下一个