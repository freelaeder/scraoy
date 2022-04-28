import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# from sundata.items import SunItem
# 报错 ，但可以正常运行，不美观
# 大致原理就是：在一个package中，同级使用 . 在父级使用 ..
from ..items import SunItem


class Sun0769Spider(CrawlSpider):
    name = 'sun0769'
    allowed_domains = ['sun0769.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    rules = (
        # 列表页，列表页面中没有需要提取的数据，可以不同指定解析函数，链接需要跟进
        # https://wz.sun0769.com/political/index/politicsNewest?id=1&page=6
        Rule(LinkExtractor(allow=r'index/politicsNewest\?id=1&page=\d+'), follow=True),
        # 详情页
        # http://wz.sun0769.com/political/politics/index?id=475825
        Rule(LinkExtractor(allow=r'politics/index\?id=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # 实例化item，使用xpath提取数据
        item = SunItem()
        # 编号
        item['num'] = response.xpath('//div[@class="mr-three"]/div[1]/span[4]/text()').extract_first()
        # 详情页面的请求地址
        item['detail_url'] = response.url
        # 标题
        item['title'] = response.xpath('//div[@class="mr-three"]/p/text()').extract_first()
        # 具体内容
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract_first()
        # print('item=', item)
        yield item
