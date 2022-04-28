from parsel import SelectorList, Selector

import scrapy
# from scrapy.ScrDome.itcase.itcase.items import ItcaseItem
# 被注释的会报错，找不到该模块
from itcase.items import ItcaseItem


class MyitcaseSpider(scrapy.Spider):
    name = 'myitcase'
    allowed_domains = ['www.itcase.com']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        # print(response.text)
        li_list: SelectorList = response.xpath("//div[@class='tea_txt tea_txt_cur ']/ul/li")
        # print(type(li_list))
        print(li_list)
        # <class 'scrapy.selector.unified.SelectorList'>
        li: Selector
        for li in li_list:
            #     # print(type(li))
            item = ItcaseItem()
            item['name'] = li.xpath('.//h3/text()').extract_first()
            item['job'] = li.xpath('.//h4/text()').extract_first()
            item['desc'] = li.xpath('.//p/text()').extract_first()
            yield item
