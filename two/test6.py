# author:  freelaeder
# ----
# date:  2022/4/14 20:03

from urllib.request import urlopen

url = 'http://www.baidu.com'

resp = urlopen(url)

# print(resp.read().decode('utf-8'))

with open('mybaidu.html', 'w',encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))

print('over')
