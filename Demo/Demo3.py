# author:  freelaeder
# ----
# date:  2022/4/27 10:28


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from zuhao.items import ZuhaoItem


class Zuhao00Spider(CrawlSpider):
    name = 'zuhao00'
    allowed_domains = ['list.xubei.org']
    start_urls = ['http://list.xubei.org/?gameId=302']

    rules = (
        # http://list.xubei.org/?gameId=302&pageIndex=3  分页
        Rule(LinkExtractor(allow=r'\?gameId=1494&pageIndex=\d+'), callback='parse_detail', follow=True),
        # 详情页
        # http://list.xubei.org/goods_details?goodsId=3534843
        Rule(LinkExtractor(allow=r'goods_details\?goodsId=\d+'), callback='parse_item', follow=False),
    )

    def parse_detail(self, response):
        # print(response.url)
        tr_list = response.xpath('//*/div/div/div/div//tr')
        print(tr_list)

    def parse_item(self, response):
        # print(response)
        item = ZuhaoItem()
        item['name'] = response.xpath(
            '//*[@id="__next"]/div/div[3]/div[2]/div[2]/div[1]/div[1]/span/text()').extract_first()
        item['detail_url'] = response.url
        item['num'] = response.xpath(
            '//*[@id="__next"]/div/div[3]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/span[2]/text()').extract_first()
        item['description'] = response.xpath(
            '//*[@id="__next"]/div/div[4]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/span/text()').extract_first()
        # print(item)
        yield item
