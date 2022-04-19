# author:  freelaeder
# ----
# date:  2022/4/18 20:48

# https://fanyi.youdao.com/

# 有道翻译
import json
import random
import time
from hashlib import md5

import requests


class Youdao:
    def __init__(self, kw):
        self.url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            "Accept": "application / json, text / javascript, * / *; q = 0.01", \
            "Connection": "keep - alive"
        }
        # 关键字
        self.kw = kw
        # 时间戳
        self.lts = str(int(time.time() * 1000))
        # 盐
        self.salt = self.lts + str(random.randint(0, 10))
        # sign
        self.last = 'Ygy_4c=r#e#4EX^NUGUc5'
        self.content = 'fanyideskweb' + self.salt + self.last
        # MD5加密
        self.sign = md5(self.content.encode('utf-8')).hexdigest()
        self.data = {
            "i": self.kw,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": self.salt,
            "sign": self.sign,
            "lts": self.lts,
            "bv": "ac3968199d18b7367b2479d1f4938ac2",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content.decode('utf-8')

    def start(self):
        data = self.get_data()
        # {"type":"EN2ZH_CN",
        # "errorCode":0,"elapsedTime":1,
        # "translateResult":[[{"src":"gold","tgt":"黄金"}]]}
        data_dict = json.loads(data)
        result = data_dict.get('translateResult')
        tgt = result[0][0].get('tgt')
        print(f'tft----{self.kw} ----{tgt}')


if __name__ == '__main__':
    s = Youdao('热')
    s.start()
