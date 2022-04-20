import scrapy


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['www.51.com']
    start_urls = [
        'https://search.51job.com/list/010000%252C020000%252C030200%252C040000%252C200200,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    def parse(self, response):
        with open('job.html', 'w') as f:
            f.write(response.text)
        print('ko')