# author:  freelaeder
# ----
# date:  2022/4/14 20:35

import requests

# 目标地址
url = 'https://www.sogou.com/web?query=周杰伦'

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',

}

response = requests.get(url, headers=headers)

print(response.content.decode('utf-8'))
