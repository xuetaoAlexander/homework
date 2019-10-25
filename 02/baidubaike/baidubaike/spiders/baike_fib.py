# -*- coding: utf-8 -*-
import scrapy

class BaikeFibSpider(scrapy.Spider):
    name = 'baike_fib'
    base_url = 'https://baike.baidu.com'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145?fr=aladdin']
    filename = "output"

    def __init__(self):
        self.fout = open(self.filename, "wb+")

    def start_requests(self):
        yield scrapy.Request(url = self.start_urls[0], meta = {"count" : 1, "title" : ""}, callback = self.parse)
    
    def parse(self, response):
        print(response.request.headers['User-Agent'], '\n')
        h1_name = response.xpath('//h1/text()')[0].extract()
        #print(h1_name)
        title = response.meta["title"] + h1_name
        self.fout.write(title.encode('UTF-8'))
        self.fout.write(b'\n')
        title += ' -> '
        if response.meta["count"] <  5:
            baike_list = response.xpath('//div[@class="lemma-summary"]/div[@class="para"]/a/@href')
            for i in baike_list:
                url = self.base_url + i.extract()
                #print(url)
                yield scrapy.Request(url = url, meta = {"count" : response.meta["count"] + 1, "title" : title}, callback = self.parse)
