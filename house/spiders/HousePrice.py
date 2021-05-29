import scrapy
import re
from bs4 import BeautifulSoup
# from scrapy.selector import Selector

class HousepriceSpider(scrapy.Spider):
    name = 'HousePrice'
    # allowed_domains = ['https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E6%9D%B1%E5%8D%80_zip/']
    start_urls = ['https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E6%9D%B1%E5%8D%80_zip/']

    def parse(self, response):
        print("parse : ")
        res = BeautifulSoup(response.body,features="lxml")
        url=""
        # print(res.select('div section ul a')['href'])
        # print()
        # for house in res.select('li a'):
            # print("house:",house['href'])
        houses = re.findall('https://community.houseprice.tw/building......',str(res.select('div section ul a')))
        for house in houses:
            # print("house",house)
            # yield self.parse_house_page(str(house))
            yield scrapy.Request(house,self.parse_house_page)
        # for house in res.select('div section ul a'):
            
        #     print("house",house['href'])

    def parse_house_page(self,response):
        print("This is parse_house:",response)
        res = BeautifulSoup(response.body,features="lxml")
        print(res.select('div ul'))
