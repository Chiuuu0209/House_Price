import scrapy
import re
from bs4 import BeautifulSoup
# from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.request as req

class HousepriceSpider(scrapy.Spider):
    name = 'HousePrice'
    # allowed_domains = ['https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E6%9D%B1%E5%8D%80_zip/']
    # start_urls = ['https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E6%9D%B1%E5%8D%80_zip/']

    def __init__(self, city="台南市" ,region = "東區" , *args, **kwargs):
        super(HousepriceSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"https://community.houseprice.tw/list/{city}_city/{region}_zip/?p="]
        self.remain_urls = ["https://community.houseprice.tw/list",f"https://community.houseprice.tw/list/{city}_city/{region}_zip/",f"https://community.houseprice.tw/list/{city}_city/{region}_zip/?p=1"]

    def parse(self, response):
        print("parse : ")
        headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36",
            "cookie": "_gcl_au=1.1.189772085.1622176283; _ga=GA1.3.232522926.1622176283; __lt__cid=e55e78cd-8f95-4df6-b244-f183d017fe03; _fbp=fb.1.1622176282851.1106976163; TRID_G=a185a6e7-3e68-4821-86e5-fbc00a5f7162; _gid=GA1.3.1607873672.1623392310; __ltm_https_flag=true; __ltmwga=utmcsr=(direct)|utmcmd=(none); __lt__sid=4391ae19-21c7fa02; _pk_ses.28.9e80=*; userid=3c6ad7c7-2307-4fa8-b31f-5c1c0301d02f; _pk_id.28.9e80=a1cdc0678c5ab2e1.1622176283.12.1623395132.1623392310.; hpwebmobile=0; TS01fcc96e=01aebff41477b3fcfe8c2b104072713f2d4e0359aa525fd6d6cea21c058019321f5ba077ea473c429fd357340611ca76708b8442a6d4b26f00c07e18829d6a068af2b594f1b6f19aa9737a7ec3bfb8fb0b243eb97d",
            "authority":"s.houseprice.tw",
            "origin": "https://community.houseprice.tw",
            }
        res = BeautifulSoup(response.body,features="lxml")
        # for u in res.find_all(href=re.compile("https://community.houseprice.tw/list")):
        #     if u['href'] not in self.remain_urls:
        #         self.remain_urls.append(u['href'])
        #         yield scrapy.Request(u['href'],self.parse,headers={
        #             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        #             "referer":u['href']
        #         })
        # url=""
        # print(res.select('div section ul a')['href'])
        # print()
        # for house in res.select('li a'):
            # print("house:",house['href'])
        houses = re.findall('https://community.houseprice.tw/building......',str(res.select('div section ul a')))
        # yield scrapy.Request(houses[0],self.parse_house_page,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"})
        # yield self.parse_house_page(str(houses[0]))
        for house in houses:
            # print("house",house)
            yield response.follow(house, callback=self.parse_house_page)
            # yield self.parse_house_page(str(house),headers=headers)

            # yield scrapy.Request(house,self.parse_house_page,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"})
        # for house in res.select('div section ul a'):
            
        #     print("house",house['href'])
        
    def parse_house_page(self,response):
        # print("This is parse_house:",url)
    # #     yield scrapy.Request(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"},callback=self.aaa)
    #     # res = req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"})
    #     # with req.urlopen(res) as response:
    #     #     data = response.read()
    #     # soup = BeautifulSoup(res.body,features="lxml")
    #     # print(soup)
    #     # print(soup.find_all("div"))
        
        opts = ChromeOptions()
        opts.add_argument("--headless")
        prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        opts.add_experimental_option("prefs", prefs)  # 禁止加载图片和CSS
        # opts.add_argument(headers)
        driver = webdriver.Chrome(executable_path=".\\Webdriver\\chromedriver.exe",options=opts)
        # driver = webdriver.Firefox(executable_path=".\\Webdriver\\geckodriver.exe",options=opts)
        driver.get(response.url)
        # try:
        #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "div")))
        #     print("wait")
        #     soup = BeautifulSoup(driver.page_source,"html.parser")
        # finally:
        #     driver.quit()
        # print("e: ",soup)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        # print("soup: ",soup.find_all("div",class_="detail_footer"))
        driver.close()
        # print("s1:",soup.find_all(class_="item")[0])
        li = soup.find_all("li")
        if soup.find(class_='b-tag'):
            # print("btag: ",soup.find("b-tag"))
            yield{
                "建案名稱":soup.find('title').text.split('-')[0],
                # "地址":soup.find_all("address")[0].text,
                "屋齡":li[4].get_text()[2:],
                "樓高":li[5].get_text()[2:],
                "公設比":li[6].get_text()[3:],
                "建設公司":li[12].get_text()[4:],
                "總戶數":li[2].get_text()[3:]
            }
        else:
            yield{
                "建案名稱":soup.find('title').text.split('-')[0],
                # "地址":soup.find_all("address")[0].text,
                "屋齡":li[3].get_text()[2:],
                "樓高":li[4].get_text()[2:],
                "公設比":li[5].get_text()[3:],
                "建設公司":li[11].get_text()[4:],
                "總戶數":li[1].get_text()[3:]
            }


        # try:
        #     print("標題: ",soup.find_all('h1',class_="flex_item title_big")[0].get_text(strip=True))
        # except:
        #     print("標題: ",soup.find_all('h1'))
        # try:
        #     print("地址: ",soup.find_all(class_="item")[0].find_all("li")[0].get_text(strip=True))
        #     print("類型: ",soup.find_all(class_="item")[0].find_all("li")[1].get_text(strip=True))
        #     print("土地: ",soup.find_all(class_="item")[0].find_all("li")[2].get_text(strip=True))
        #     print("國小: ",soup.find_all(class_="item")[0].find_all("li")[3].get_text(strip=True))
        #     print("國中: ",soup.find_all(class_="item")[0].find_all("li")[4].get_text(strip=True))
        # except:
        #     print("none")

        # try:
        #     print("屋齡: ",soup.find_all(class_="item")[1].find_all("li")[0].get_text(strip=True))
        #     print("樓高: ",soup.find_all(class_="item")[1].find_all("li")[1].get_text(strip=True))
        #     print("坪數: ",soup.find_all(class_="item")[1].find_all("li")[2].get_text(strip=True))
        #     print("公設: ",soup.find_all(class_="item")[1].find_all("li")[3].get_text(strip=True))
        # except:
        #     print("none")
        # try:
        #     print("結構: ",soup.find_all(class_="item")[2].find_all("li")[0].get_text(strip=True))
        #     print("建設: ",soup.find_all(class_="item")[2].find_all("li")[1].get_text(strip=True))
        #     print("營造: ",soup.find_all(class_="item")[2].find_all("li")[2].get_text(strip=True))
        #     print("公共: ",soup.find_all(class_="item")[2].find_all("li")[3].get_text(strip=True))
        # except:
        #     print("none")
        # try:
        #     print("戶數: ",soup.find_all(class_="item")[3].find_all("li")[0].get_text(strip=True))
        #     print("管理: ",soup.find_all(class_="item")[3].find_all("li")[1].get_text(strip=True))
        #     print("車位: ",soup.find_all(class_="item")[3].find_all("li")[2].get_text(strip=True))
        #     print("垃圾: ",soup.find_all(class_="item")[3].find_all("li")[3].get_text(strip=True))
        # except:
        #     print("none")



        # for s in soup.find_all(class_="item"):
        #     print("i:", s.find_all("li"))
        #     for l in s.find_all("li"):
        #         print("s:",l.get_text(strip=True))
        #         print("re1:",re.findall('..',str(l.get_text(strip=True)))[0])
        #         print("re2:",re.findall('..(.*)',str(l.get_text(strip=True))))

    # def parse_house_page(self,response):
    #     soup = BeautifulSoup(response.body,features="lxml")
    #     print(soup.find_all("ul"))