import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import NewsItem


class NewdataSpider(CrawlSpider):
    name = 'newdata'
    allowed_domains = ['news.e23.cn']
    start_urls = ['https://news.e23.cn/content/jinan/index.html']

    rules = (
        # 分页
        # https://news.e23.cn/content/jinan/2.html
        # https://news.e23.cn/content/jinan/2.html
        Rule(LinkExtractor(allow=r'content/jinan/\d+\.html'), follow=True),
        # 详情页
        # http://news.e23.cn/jnnews/2022-04-27/2022042700013.html
        # http://news.e23.cn/jnyc/2022-04-25/2022042500489.html
        # http://news.e23.cn/jnnews/2022-04-27/2022042700013.html
        # http://news.e23.cn/jnnews/2022-04-27/2022042700035.html
        # http://news.e23.cn/jnnews/2022-04-26/2022042600022.html
        Rule(LinkExtractor(allow=r'\w/2022-04-\d+/\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = NewsItem()
        item['title'] = response.xpath("//div[@class='post_content_main']/h1/text()").extract_first()
        item['time'] = response.xpath("//div[@class='post_time']/p[1]/text()").extract_first()
        item['src'] = response.xpath("//div[@class='post_time']/p[2]/a/text()").extract_first()
        item['content'] = response.xpath('//*[@id="zhw"]/p/text()').extract_first()

        yield item
