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
k=16
for i in range(3174, 3194):
    img_url = f'https://www.cangyuantu.cc/mhimg/yirenzx/a0/3194.jpg'
    try:
        img_response = requests.get(img_url, headers=headers)
        img_response.raise_for_status()  # 如果响应状态不是200，抛出HTTPError异常

        # 更稳健地获取章节名，例如从HTML中的特定元素或URL中提取
        chapter_name = '319宝姐生日快乐！'
        chapter_path = os.path.join(target_path, chapter_name)
        os.makedirs(chapter_path, exist_ok=True)
        # 使用章节编号和图片序号作为文件名
        filename = f"319_{k}.jpg"
        filepath = os.path.join(chapter_path, filename)

        with open(filepath, 'wb') as f:
            f.write(img_response.content)

        # 设置请求间隔，避免过于频繁请求
        time.sleep(random.uniform(0.1, 0.5))  # 示例：随机等待0.5秒到1.5秒之间

        print(chapter_name + filename)
        k+=1
    except requests.exceptions.RequestException as e:
        print(f"章节{chapter_name}:{img_url}下载失败: {e}")