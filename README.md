House_Price_Crawler
===
Crawl house price by scrapy.

Target site
---
```
https://community.houseprice.tw/list/
```
You can chose the region you want to crawl.

Run code
---
Just run
```
scrapy crawl HousePrice
```

The default region is `台南/東區`.
And you need to pass argument to change region, for example:

```
scrapy crawl HousePrice -a region=北區
```
or
```
scrapy crawl HousePrice -a city=台北市 -a region=北投區
```

Output csv file
```
scrapy crawl HousePrice -O house_price.csv
```

Scrapy tutorial
```
https://hackmd.io/frV3RgNFRyiQAgFnd_gBOA
```