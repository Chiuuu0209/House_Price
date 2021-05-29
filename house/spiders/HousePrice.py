import scrapy
import re
from bs4 import BeautifulSoup
# from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.request as req

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
        # yield scrapy.Request(houses[0],self.parse_house_page,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"})
        for house in houses:
            print("house",house)
            yield self.parse_house_page(str(house))
            # yield scrapy.Request(house,self.parse_house_page,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"})
        # for house in res.select('div section ul a'):
            
        #     print("house",house['href'])

    def parse_house_page(self,url):
    #     print("This is parse_house:",url)
    #     yield scrapy.Request(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"},callback=self.aaa)
        # res = req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"})
        # with req.urlopen(res) as response:
        #     data = response.read()
        # soup = BeautifulSoup(res.body,features="lxml")
        # print(soup)
        # print(soup.find_all("div"))
        
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=".\\Webdriver\\geckodriver.exe",options=opts)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        print("soup: ",soup.find_all("div",class_="detail_footer"))
        driver.close()
    # def parse_house_page(self,response):
    #     soup = BeautifulSoup(response.body,features="lxml")
    #     print(soup.find_all("ul"))