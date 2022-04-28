import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HudataSpider(CrawlSpider):
    name = 'hudata'
    allowed_domains = ['zuhaowan.com']
    start_urls = ['https://www.zuhaowan.com/zuhao/']

    rules = (
        # 分页
        # https://www.zuhaowan.com/zuhao/p2.html
        Rule(LinkExtractor(allow=r'zuhao/p\d+\.html'), follow=True),
        # 详情页
        # https://www.zuhaowan.com/zuhao/10702393.html
        # https://www.zuhaowan.com/zuhao/9649887.html
        Rule(LinkExtractor(allow=r'zuhao/\d+'+'.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        print(1212)
        item['title'] = response.xpath("//div[@class='key_msg2']/ul/li[1]/text()").extract_first()
        print(item)
