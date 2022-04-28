# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    num = scrapy.Field()
    detail_url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
