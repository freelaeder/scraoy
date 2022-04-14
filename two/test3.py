# author:  freelaeder
# ----
# date:  2022/4/14 8:46

# https://36kr.com/

# - 1准备起始url 和请求头信息  定义好请求参数
# - 2 发送请求获取响应
# - 3 获取响应数据  提取数据
# - 4 保存数据
# - 5 开启爬虫
import json
import re
import traceback
from hashlib import md5

import requests


class Kr36:
    def __init__(self):
        #  1准备起始url 和请求头信息
        self.url = "https://www.36kr.com/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        }

    def get_data(self):
        # 发送请求获取响应
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode('utf-8')

    def parse_data(self, data):
        # 用正则提取数据
        result = re.findall('<script>window.initialState=(.*?)</script>', data)[0]
        # print(result)
        # 把数据转为字典
        data_dict = json.loads(result)
        data_list = data_dict['homeData']['data']['homeFlow']['data']['itemList']
        print(len(data_list))
        new_data_list = []
        for item in data_list:
            # itemType不同 新闻的类型不同  10 0 5000  数据为10的是最新新闻
            if item['itemType'] == 10:
                item = item['templateMaterial']
                temp = {}
                temp['title'] = item.get('widgetTitle')
                temp['time'] = item.get('publishTime')
                temp['authorName'] = item.get('authorName')
                temp['image'] = item.get('widgetImage')
                temp['summary'] = item.get('summary')
                new_data_list.append(temp)

        return new_data_list

    def save_data(self, data_list):
        with open('k36.json', 'w', encoding='utf-8') as f:
            for d in data_list:
                f.write(json.dumps(d, ensure_ascii=False) + ",\n")

    def start(self):
        data = self.get_data()
        data_list = self.parse_data(data)
        self.save_data(data_list)


if __name__ == '__main__':
    d = Kr36()
    d.start()
