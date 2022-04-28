import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ZuhaoItem


class ZudataSpider(CrawlSpider):
    name = 'zudata'
    allowed_domains = ['list.xubei.org']
    start_urls = ['http://list.xubei.org/?gameId=302']

    rules = (
        # http://list.xubei.org/?gameId=302&pageIndex=3
        Rule(LinkExtractor(allow=r'gameId=302&pageIndex=\d+'), callback='parse_detail', follow=True),
        # http://list.xubei.org/goods_details?goodsId=3363255
        Rule(LinkExtractor(allow=r'goods_details\?goodsId=\d+'), callback='parse_item', follow=False),
    )

    def parse_detail(self, response):
        tr_list = response.xpath('//*/div/div/div/div//tr')
        print(tr_list)

    def parse_item(self, response):
        item = ZuhaoItem()
        # item['name'] = response.xpath(
        #     '//*[@id="__next"]/div/div[3]/div[2]/div[2]/div[1]/div[1]/span/text()').extract_first()
        item['name'] = response.xpath("//span[@class='dhcr_goods_title']/text()").extract_first()
        item['detail_url'] = response.url
        # item['num'] = response.xpath(
        #     '//*[@id="__next"]/div/div[3]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/span[2]/text()').extract_first()
        #
        item['num'] = response.xpath(
            "/html/body/div[1]/div/div[3]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/span[2]/text()").extract_first()
        # item['description'] = response.xpath(
        #     '//*[@id="__next"]/div/div[4]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/span/text()').extract_first()
        item['description'] = response.xpath("/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div").extract_first()
        # print(item)
        yield item
