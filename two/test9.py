# author:  freelaeder
# ----
# date:  2022/4/14 21:03

# https://movie.douban.com/j/chart/top_list
# ?type=13&interval_id=100%3A90&action=&start=0&limit=1
import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}
params = {
    "type": 13,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 2,
}

response = requests.get(url, headers=headers, params=params)
data_list = response.content.decode('utf-8')
data_dict = json.loads(data_list)
print(data_dict)
# [{"rating":["9.6","50"],
# "rank":1,
# "cover_url":"https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2561716440.jpg",
# "is_playable":true,"id":"1291546","types":["剧情","爱情","同性"],
# "regions":["中国大陆","中国香港"],
# "title":"霸王别姬",
# "url":"https:\/\/movie.douban.com\/subject\/1291546\/",
# "release_date":"1993-07-26","actor_count":26,
# "vote_count":1928475,"score":"9.6",
# "actors":["张国荣","张丰毅","巩俐","葛优","英达","蒋雯丽","吴大维","吕齐","雷汉","尹治","马明威","费振翔","智一桐","李春","赵海龙","李丹","童弟","沈慧芬","黄斐","徐杰","黄磊","冯远征","杨立新","方征","周璞","隋永清"],"is_watched":false},
# {"rating":["9.6","50"],
# "rank":2,"cover_url":"https://img2.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2578474613.jpg","is_playable":true,"id":"1292063","types":["剧情","喜剧","爱情","战争"],"regions":["意大利"],"title":"美丽人生","url":"https:\/\/movie.douban.com\/subject\/1292063\/","release_date":"2020-01-03","actor_count":29,"vote_count":1198984,"score":"9.6","actors":["罗伯托·贝尼尼","尼可莱塔·布拉斯基","乔治·坎塔里尼","朱斯蒂诺·杜拉诺","赛尔乔·比尼·布斯特里克","玛丽萨·帕雷德斯","霍斯特·布赫霍尔茨","利迪娅·阿方西","朱利亚娜·洛约迪切","亚美利哥·丰塔尼","彼得·德·席尔瓦","弗朗西斯·古佐","拉法埃拉·莱博罗尼","克劳迪奥·阿方西","吉尔·巴罗尼","马西莫·比安奇","恩尼奥·孔萨尔维","吉安卡尔洛·科森蒂诺","阿伦·克雷格","汉尼斯·赫尔曼","弗兰科·梅斯科利尼","安东尼奥·普雷斯特","吉娜·诺维勒","理查德·塞梅尔","安德烈提多娜","迪尔克·范登贝格","奥梅罗·安东努蒂","沈晓谦","张欣"],"is_watched":false}]
