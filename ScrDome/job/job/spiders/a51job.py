import json
import re

from scrapy.http.response.html import HtmlResponse

from scrapy import Request

import scrapy
from job.items import JobItem


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['www.51.com']
    start_urls = [
        'https://search.51job.com/list/010000%252C020000%252C030200%252C040000%252C200200,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']
    cookies = '_uab_collina=165052994618029085324269; guid=bac3e13e03e7d476674552436bd94fe1; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60010000%2C020000%2C030200%2C040000%2C200200%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60010000%2C020000%2C030200%2C040000%2C200200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=76b20ffa16505299470755853e74852580225113aa2e1999181878de1c450c; acw_sc__v3=6261169d2477a837d1c4e0046d11d4d0f323d31e; ssxmod_itna=YqfxnDu7G=qGuDeq0dq=UYD7YqitzeerKqTrqdvDlPrQxA5D8D6DQeGTTnKt8TqnWiwqDyj8q+Teij7pwPK82nOrbLnGZneDHxY=DUh0mwoD445GwD0eG+DD4DWDme7DnxAQDjxGpycuTXBDi3Dbg=Df4DmDGAybqDgDYQDGTKXD7QDIM=KZ4bl0nte7Q+YzqDMneGXY7a=zwbF1aqV7mWTdCpnDB=zxBQZ0MN00eDHmq0Z3eYEK0Go/ghoYAPe+0xNQiwIG9+t38Gvoip5lBOq38x5W++sC5DA+iq3QEYxD; ssxmod_itna2=YqfxnDu7G=qGuDeq0dq=UYD7YqitzeerKqTrqdD6EK=40vhy403KwnDyiGlKPrqa0PXCeCi0C/AhYgLIKK/bq=mrlQpKaQOxSfLTXtyttAWRrWbc3rnfLSWbcCQuEQh=S3vruTnXrAxaz7c1KhH8/Gri=h0NXDidrxOGZPErit0FZDO=iShWi9mmtpo=IIYp8Pmqr+nFeroiVPk8SW8eKaoHm9WfYgkjYZykkZF0d6LbDryHbfxbWIu0tDrmrBBEqnjbWt0Ame34X+kWK5oA0Ic8eGcqnxOtz=/D/BOWelb3vFweXDfAj2VtaWW4l8bL0WT04li+bf2Gz2xcheHaG3RfY+r+7pAbL4vanGNlP=Y4YE25r4bbE=iENDIdHex+o1IOLDP4Zxa+R=Xc5x4ASoA0b=fhbiRQ24a8byC2EiiYA2KR5aF8mF0sGbmYi=ebLGeNSwpzFiAbyiD1KfLAT=/SDi+rXFWFgcWoPwvOtdlILxeEm+KARvA0e9CEAlmTVSBta+1PDkCID4pROIIWB0+n7Q1EmpxRHvozVSmfxIwFraxDKk8wTvxrepWqPlkcM5UzIdY9pcqD7=DYIYcG1RrN+ZWY2RFiN/h1Wn4eD==='

    def start_requests(self):
        self.cookies_dict = {}
        for item in self.cookies.split("; "):
            kv = item.split("=")
            self.cookies_dict[kv[0]] = kv[1]

        for url in self.start_urls:
            yield Request(url, dont_filter=True, cookies=self.cookies_dict)

    def parse(self, response):
        # with open('job.html', 'w') as f:
        #     f.write(response.text)
        # print('ko')
        # <class 'scrapy.selector.unified.SelectorList'>
        # print(type(li_list))
        results = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]
        print(results)
        data_dict = json.loads(results)
        # 获取职位列表
        data_list = data_dict.get('engine_jds')
        for data in data_list:
            item = JobItem()
            item['name'] = data.get('job_name')
            item['company_name'] = data.get('company_name')
            item['provides_name'] = data.get('providesalary_text')

            # 详情页的地址
            job_href = data.get('job_href')
            datail_request = Request(job_href, callback=self.parse_datail, dont_filter=True, cookies=self.cookies_dict,
                                     meta={'item': item})
            yield datail_request

    def parse_datail(self, response: HtmlResponse):
        data = response.xpath('.//div[@class="bmsg job_msg inbox"]/p/text()').extract()
        item = response.meta['item']
        item['require'] = data
        print('data------------', data)
        yield item
