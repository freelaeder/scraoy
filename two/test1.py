# author:  freelaeder
# ----
# date:  2022/4/13 9:09


# 豆瓣电影
import json

import requests

url = 'https://movie.douban.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Accept': 'application/json'
}
# https://movie.douban.com/j/search_subjects?
# type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0

# https://movie.douban.com/j/search_subjects?
# type=movie&  类别电影
# tag=%E5%8F%AF%E6%92%AD%E6%94%BE  分类
# &sort=recommend  排序
# &page_limit=20 多少条数据
# &page_start=0  起始页

class Douban:
    def __init__(self, tag='青春', start=0, limit=20):
        self.url = 'https://movie.douban.com/j/search_subjects'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'Accept': 'application/json'
        }
        self.params = {
            'type': 'movie',
            'tag': tag,
            'sort': 'recommend',
            'page_limit': limit,
            'page_start': start,
        }

    def get_data(self):
        # 获取数据
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.content.decode('utf-8')

    def parse_data(self, data):
        print(f'data-------------{data}')
        # 解析数据
        #
        data_dict = json.loads(data)
        data_list = data_dict.get('subjects')
        print(f'data_dict---------------{data_list}')
        # 保存提取后的数据
        data_list_new = []
        for i in data_list:
            temp_dict = {}
            temp_dict['rate'] = i.get('rate')
            temp_dict['title'] = i.get('title')
            temp_dict['url'] = i.get('url')
            # 追加数据
            data_list_new.append(temp_dict)
        print(f'data_list_new{data_list_new}')
        return data_list_new

    def save_data(self, data):
        # 保存数据
        with open('hotmovie.json', 'w', encoding='utf-8') as f:
            for d in data:
                f.write(json.dumps(d, ensure_ascii=False) + ",\n")

    def start(self):
        # 获取数据
        data = self.get_data()
        # 提取数据
        data_list = self.parse_data(data)
        # 保存数据
        self.save_data(data_list)
        print(f'保存成功')


if __name__ == '__main__':
    s = Douban('青春', 0, 2000)
    s.start()

