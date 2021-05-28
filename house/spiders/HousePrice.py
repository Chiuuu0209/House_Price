import scrapy


class HousepriceSpider(scrapy.Spider):
    name = 'HousePrice'
    allowed_domains = ['https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E6%9D%B1%E5%8D%80_zip/']
    start_urls = ['http://https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E6%9D%B1%E5%8D%80_zip//']

    def parse(self, response):
        pass
