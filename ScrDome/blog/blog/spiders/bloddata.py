import json

from parsel import SelectorList
from scrapy import Request
from scrapy.http.response.html import HtmlResponse

import scrapy
from ..items import BlogItem


class BloddataSpider(scrapy.Spider):
    name = 'bloddata'
    allowed_domains = ['www.blog.cn']
    start_urls = ['http://bbs.hupu.com/hs']

    def parse(self, response):
        # with open('data.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # print('ok')
        data: SelectorList = response.xpath("//div[@class='bbs-sl-web-post']/ul/li/div")
        # print(type(data))
        # print(data)
        for i in data:
            item = BlogItem()
            item['name'] = i.xpath("./div[1]/a/text()").extract_first()
            item['auther'] = i.xpath("./div[3]/a/text()").extract_first()
            item['time'] = i.xpath('./div[4]/text()').extract_first()
            # item['url'] = 'https://bbs.hupu.com' + i.xpath("./div[1]/a/@href").extract_first()
            print(item)
            job_href = 'https://bbs.hupu.com' + i.xpath("./div[1]/a/@href").extract_first()
            detail_request = Request(job_href, callback=self.parse_datail, dont_filter=True, meta={'item': item})
            yield detail_request

    def parse_datail(self, response: HtmlResponse):
        item = response.meta['item']
        data = response.xpath("//p/text()").extract_first()
        item['content'] = data
        yield item
