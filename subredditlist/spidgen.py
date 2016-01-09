import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from spiders.baseSpider import baseSpider

# Use this script to create a usable spider from the baseSpider class
# can add methods to use any lists of urls you want to start from

process = CrawlerProcess()
spide = baseSpider(['reddit.com'], ['https://www.reddit.com/r/gaming'])
process.crawl(baseSpider)
process.start()
