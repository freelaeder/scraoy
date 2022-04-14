# author:  freelaeder
# ----
# date:  2022/4/14 20:48
import requests

url = ' https://fanyi.baidu.com/sug'

data = {
    'kw': 'free'
}

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',

}
# post 请求，发送的数据必须放在字典中，通过data参数进行传递
response = requests.post(url, data=data, headers=headers)
# 将服务器返回的内容直接处理成json() => dict
print(response.json())
# {'errno': 0,
# 'data': [
# {'k': 'free', 'v': 'adj. 免费的; 自由的; 免税的; 空闲的 adv. 免费地; 自由地，无拘束地; 一帆风顺地 '},
# {'k': 'Free', 'v': '[人名] [英格兰人姓氏] 弗里绰号，或身份名称，来源于古英语，含义是“自由的”(free)，即不是'},
# {'k': 'FREE', 'v': 'abbr. Florida Resources in Education Exchange 佛罗里达'},
# {'k': 'freed', 'v': 'v. 免除，释放( free的过去式和过去分词 ); 使…免除，使…释放，使…。。摆脱'},
# {'k': 'Freed', 'v': '[人名] [英格兰人、苏格兰人、威尔士人姓氏] 弗里德 Firth的变体'}]}

data_dict = response.json()
result_list = data_dict.get('data')
print(result_list)

for i in result_list:
    print(i['k'], i['v'])

