# author:  freelaeder
# ----
# date:  2022/4/12 10:45


import requests
# 获取gitee
url = 'https://gitee.com/freeslaeder'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Cookie': 'user_locale=zh-CN; oschina_new_user=false; Serve_State=true; yp_riddler_id=fc4e6fd3-117e-44bd-bb3a-76a495872000; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; visit-gitee--2022-03-22%2010%3A27%3A42%20%2B0800=1; remote_way=ssh; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%229014269%22%2C%22first_id%22%3A%2217c4f7e7bef3fd-041759a1cc93c1-b7a1a38-786432-17c4f7e7bf08a9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22repo2public%22%7D%2C%22%24device_id%22%3A%2217c4f7e7bef3fd-041759a1cc93c1-b7a1a38-786432-17c4f7e7bf08a9%22%7D; tz=Asia%2FShanghai; Hm_lvt_24f17767262929947cc3631f99bfd274=1649291339,1649292233,1649644277,1649732229; Hm_lpvt_24f17767262929947cc3631f99bfd274=1649732229; gitee-session-n=ZzBQdEltbGw0eFg3QWFQSEVqRDY1MW1uTTRMOUlsUDZZejlJenhEQWJ1UjhWMUZPajcvYk9sQUtqWjVlQlV4YTVlZXVrOGYvTUZBc1pQMlNaWjQ4OUxDd0dGclJEais4a2NyRHpLaFhIOFFGR2N2M2hEbVk0Ly9QL3JzSTdhUHRkcUovR04xcHhPY1l1bjlzQUxWWDlMbmk5NE9hZEpwNlZqR0dXcitETHh3SXFzbUdkcWpzbWsrR2xZTjRjOU9uLS1oV3RqUDFUNDRBbFFKc2VDbzZYUURBPT0%3D--e74f479bf38997ee62b1205e362ada0e93aa09f7'
}
response = requests.get(url, headers=headers)

with open('freelaeder.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))

print('保存成功')
