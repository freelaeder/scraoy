# author:  freelaeder
# ----
# date:  2022/4/26 15:52

# coding=utf-8
import json
import pymysql
import requests
import hashlib

# def md5(string):
#     """
#     计算字符串md5
#     :param string: 字符串
#     :return: 字符串的md5值
#     """
#     return hashlib.md5(string.encode('utf8')).hexdigest()


# 配置连接数据库的信息
# connect = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='root',
#     db='news_crawler',
#     charset='utf8mb4'
# )
# 获取插入的游标
# cursor = connect.cursor()

url = "https://www.hao123.com/feedData/data?type=%s&app_from=pc_tuijian&rn=10&pn=1"

# 定义插入语句
# sqlTemplate = "insert ignore into data_rec(rid, url, title, `desc`, `time`, `source`) " \
#               "values ('%s', '%s', '%s', '%s', FROM_UNIXTIME(%d), '%s')"

# # 循环计数器
# i = 0
# while i < 10086:
#     data = json.loads(requests.get(url).content.decode("utf8"))
#     # 遍历新闻列表json中的每篇新闻
#     for news in data['data']:
#         # 如果新闻描述为空，则跳过
#         if news['desc'] is None:
#             continue
#         # 给插入语句赋值
#         title = connect.escape_string(news['title'])
#         description = connect.escape_string(news['desc'])
#         insertSql = sqlTemplate % (
#             md5(news['title']), news['url'], title, description, news['time'], news['source']
#         )
#         # 执行插入语句
#         cursor.execute(insertSql)
#     i = i + 1


data = json.loads(requests.get(url).content.decode('utf-8'))
print(data)

with open('new.txt', 'w', encoding='utf-8') as f:
    for new in data['data']:
        f.write(json.dumps(new, ensure_ascii=False) + ",\n")
