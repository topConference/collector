#coding:utf-8
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from top.items import topItem

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Connection': 'keep-alive'
}
class topSpider(CrawlSpider):
    name ='topspider'
    url = "http://www.guide2research.com"

    # get all pages http://www.guide2research.com/conferences/page-2
    def start_requests(self):
        url=self.url+'/conferences'
        yield Request(url, callback=self.parse)
        # for i in range(1,10):
        #     yield Request(url+'/page-'+str(i), callback=self.parse)

    #get every conference page url
    def parse(self,response):
        urls = response.xpath('//*[@id="ajax_content"]/div/table/tr[1]/td[2]/h4/a/@href')
        for url in urls:
            page_url = self.url + url.extract()
            print(page_url)
            yield Request(url=page_url, callback=self.parse_detail)

    #get detail information
    def parse_detail(self,response):
        item = topItem()
        detail = response.xpath('//table[1]/tr/td[2]')
        item['topic'] = response.xpath('//article[1]//header[1]/h1/text()').extract_first().strip()
        item['deadline'] = detail[0].xpath('text()').extract_first().strip()
        item['link'] = detail[1].xpath('a/@href').extract_first().strip()
        item['dates'] = detail[2].xpath('text()').extract_first().strip()
        item['address'] = detail[3].xpath('text()').extract_first().strip()\
                          +detail[3].xpath('a/text()').extract_first().strip()
        item['proceed'] = self.url+detail[4].xpath('a/img/@src').extract_first().strip()
        yield item
