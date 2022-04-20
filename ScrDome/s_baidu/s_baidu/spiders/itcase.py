import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse



class ItcaseSpider(scrapy.Spider):
    name = 'itcase'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response: HtmlResponse):
        # print(type(response))
        # print(response.body)
        # 保存
        li_list = response.xpath('/html/body//div[@class="tea_txt tea_txt_cur "]/ul//li')
        print('li_list', type(li_list))
        li: Selector
        for li in li_list:
            print(li)
        # li_list <class 'scrapy.selector.unified.SelectorList'>
        pass
