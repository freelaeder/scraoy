# author:  freelaeder
# ----
# date:  2022/4/12 11:06
import json

import requests

# 模拟post
url = 'http://www.haloncloud.top/login/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Accept': 'application/json'
}
# 请求信息
login_data = {'username': '18512344321', 'password': '11111111', 'remembered': True}
# json.dumps 把字典转化为json字符串
# json.loads 把json字符串转化为字典

# 生成session 类的对象
ss = requests.session()
response = requests.post(url, headers=headers, data=json.dumps(login_data))

print(response.content.decode('utf-8'))
print(response.cookies)

# 把requests.Cookies转为字典
cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)

# 获取个人数据再次请求
info_url = 'http://www.haloncloud.top/info/'
info_reponse = requests.get(info_url, cookies=cookie_dict)
print(info_reponse.content.decode('utf-8'))
