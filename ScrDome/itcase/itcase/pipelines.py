# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class ItcasePipeline:
    def open_spider(self, spider):
        self.file = open('myitca.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # print('myitcase process', item)
        json_item = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_item + "\n")
        return item
