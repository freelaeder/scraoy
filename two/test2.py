# author:  freelaeder
# ----
# date:  2022/4/13 10:27

# 爱词霸
# http://ifanyi.iciba.com/index.php?
# c=trans
# &m=fy
# &client=6
# &auth_user=key_ciba
# &sign=0020c1fc11e96d3a

import json
from hashlib import md5

import requests


class AiChi:
    def __init__(self, kw):
        # 目标url
        self.url = 'http://ifanyi.iciba.com/index.php?'
        # 要搜索的单词
        self.kws = kw
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }
        # 参数
        self.params = {
            'c': 'trans',
            'm': 'fy',
            'client': '6',
            'auth_user': 'key_ciba',
            'sign': '0020c1fc11e96d3a',
        }
        # 表单
        self.data = {
            'from': 'zh',
            'to': 'en',
            'q': kw
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data)
        return response.content.decode('utf-8')

    def start(self):
        data = self.get_data()
        data_dict = json.loads(data)
        # {'status': 1,
        # 'content': {
        # 'from': 'zh', 'to': 'en', 'vendor': 'ciba', 'out': 'hello',
        # 'reqid': '723e8252-263c-43a8-bb3a-fb903faaf65a', 'version': 'v2.19.220221.1',
        # 'ciba_use': '以上结果来自词霸AI实验室。', 'ciba_out': '', 'err_no': 0,
        # 'ttsLan': 1, 'ttsLanFrom': 8}
        # }
        result = data_dict.get('content')
        out = result.get('out')
        print(f'-{self.kws}->>翻译结果>>>-{out}')


if __name__ == '__main__':
    s = AiChi('你好')
    s.start()
