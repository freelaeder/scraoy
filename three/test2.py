# author:  freelaeder
# ----
# date:  2022/4/15 8:36


# https://tieba.baidu.com/f/search
# /res?qw=freelaeder&sm=2&cf=1&ie=utf-8
import requests


class GetTie:
    def __init__(self, name):
        # 初始化数据
        self.name = name
        self.url = f'https://tieba.baidu.com/f?kw={self.name}'
        # 定义请求头
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
            'Cookie': 'BIDUPSID=92EFA278A1789E4E859A0E54B2E5DBE4; PSTM=1632566244; __yjs_duid=1_ad08f1db388f2e635d3440ad35fe1bed1632575354481; H_WISE_SIDS=110085_127969_177370_178384_178629_179350_179452_181133_181485_181588_182231_182531_183035_183328_183981_184011_184321_184440_184560_184655_184737_184794_184826_184893_185224_185268_185517_185879_186318_186597_186635_186716_186831_186844_186897_187022_187067_187090_187184_187188_187205_187292_187356_187433_187449_187669_187726_187912_187929_187960_188031_188181_188296_188332_188352_188427_188463_188615_188720_188731_188846_188900_189058_189325_189390_189418_189431_189468_189679_189716_189755_190113_190153_190157; bdshare_firstime=1635383302480; BDUSS=xpbUNNalY5d05XaEhzcmN6aFN4RHItZVdqdUtmOXRJU3dTYk5aU2gwNjAwTjloSVFBQUFBJCQAAAAAAAAAAAEAAADSfjqEz6e7qNa7zqrs8gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALRDuGG0Q7hhZU; BDUSS_BFESS=xpbUNNalY5d05XaEhzcmN6aFN4RHItZVdqdUtmOXRJU3dTYk5aU2gwNjAwTjloSVFBQUFBJCQAAAAAAAAAAAEAAADSfjqEz6e7qNa7zqrs8gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALRDuGG0Q7hhZU; BAIDUID=6B534E672C05F9F85A5E1061E3C79346:FG=1; STOKEN=e85b829e0348b0676760ad1a29bf743bd9bd7cbfb37dd986dfec7cf8dbd894cf; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1647964397; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31254_35910_36167_34584_36140_36126_36234_26350_35867_36100_36061; delPer=0; PSINO=3; BA_HECTOR=80042l24a420alaglf1h5aajh0q; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1647964395,1649748596; st_key_id=17; BAIDU_WISE_UID=wapp_1649748600649_379; USER_JUMP=-1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1649749251; ab_sr=1.0.1_ODY1NjgxOThkYmRkY2MzMTdmYjdlYjlkOGM3NDBkNGQzZGVlZDAyYTU1ZDU4NWU4OTU0YmIxMWY1YjVlMmM2NGU2ZThkYzE2MTg1MzZjMDA4YzNlZGZmNjYwMjVkNTQ1MTYyYTY0YzljMDAwOTJkMzhiY2FlM2U1MGY2MGEwYWEyNDEzMmMxOTllZDA1NGEzNzYwYTg5OWUzMTc0ZGE1Y2MyZTFhMzAxNmViNTc2ZDJlMmQ0ODNjNTlhYTFjYzE2; st_data=3d8a48ae0252ca028cf8010314c902c4e3e9424518afa28656aeef8e8b31ec8d418db0f3bed0df9a55c2c102d73e7bca9ea9ecef9cbdefd5842d6e2a4c62f19561f74a09f26533b81b6b3f4359d40f6cdd548b0be5005ad680aedaf55885f508; st_sign=c09b9d2b'

        }

    def get_data(self):
        # 获取数据
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode('utf-8')

    def params_data(self, data):
        # 保存数据 注意encoding（编码）是为了正常显示文字
        with open('Get_{}.html'.format(self.name), 'w', encoding='utf-8') as f:
            f.write(data)

    def start(self):
        data = self.get_data()
        self.params_data(data)
        print('{}---保存成功'.format(self.name))


if __name__ == '__main__':
    s = GetTie('赵丽颖')
    s.start()
