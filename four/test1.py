# author:  freelaeder
# ----
# date:  2022/4/18 8:48

# - 1准备起始url 和请求头信息  定义好请求参数
# - 2 发送请求获取响应
# - 3 获取响应数据  提取数据
# - 4 保存数据
# - 5 开启爬虫
import json
import os
import re
import traceback
from hashlib import md5

import requests
from lxml import etree


# 下载bili视频

class Bili:
    def __init__(self):
        #  1准备起始url 和请求头信息
        self.url = 'https://www.bilibili.com/video/BV11q4y1i7Eu?spm_id_from=333.1007.partition_recommend.content.click'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'referer': self.url
        }

    def get_data(self):
        # 发送请求获取响应
        response = requests.get(self.url, headers=self.headers)
        # print(response.content.decode('utf-8'))
        return response.content.decode('utf-8')

    def download(self, video_url, audio_url, title):
        print('开始下载')
        video = requests.get(video_url, headers=self.headers).content
        audio = requests.get(audio_url, headers=self.headers).content
        print('开始保存')
        title = title.replace("/", "").replace(" ", "")
        video_name: str = title + '_temp.mp4'
        audio_name: str = title + '_temp.mp3'
        # 保存文件
        # with open(video_name, 'wb') as f:
        #     f.write(video)
        # with open(audio_name, 'wb') as f:
        #     f.write(audio)
        print('开始合成')
        self.hecheng(video_name, audio_name, title + '.mp4')

    def hecheng(self, video_name, audio_name, new_name):
        os.system(f'ffmpeg -i {video_name} -i {audio_name} -c copy {new_name}')

    def parse_data(self, data):
        # 转化
        html = etree.HTML(data)
        # print(html)
        # 提取script 获取视频地址
        # //h1[@class='video-title tit']/@title
        # //h1[@class='video-title tit']
        # //h1[@class='video-title tit']/@title
        title = html.xpath('//h1[@id="video-title"]/span/text()')[0]
        text = html.xpath('/html/head/script[4]/text()')[0]
        print(title)
        # print(text)
        # 正则 获取视频，音频
        # 视频地址提取
        video_url = re.findall(r'"video":.*?,"baseUrl":"(.*?)",', text)[0]
        # 音频地址提取
        audio_url = re.findall(r'"audio":.*?,"baseUrl":"(.*?)",', text)[0]
        print(f'video_url{video_url}')
        print(f'audio_url{audio_url}')
        # 下载
        self.download(video_url, audio_url, title)

    def save_data(self, data_list):
        pass

    def start(self):
        data = self.get_data()
        data_list = self.parse_data(data)
        self.save_data(data_list)


if __name__ == '__main__':
    d = Bili()
    d.start()
