import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from subredditlist.items import redditItems
from scrapy.spiders import CrawlSpider


class baseSpider(CrawlSpider):
    name = "redditSpider"

    def __init__(self, allowed_domains=[], start_urls=[]):
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls
        print "Crawling..."
        print self.allowed_domains
        print self.start_urls

    def parse(self, response):
        print "Processing data..."
        print response
        redditPosts = Selector(response).xpath('//div[@id="siteTable"]')
        items = []
        for post in redditPosts:
            item = redditItems()
            item['postTitle'] = post.xpath('div/div[2]/p[1]/a/text()').extract()
            item['postLink'] = post.xpath('div/div[2]/p[1]/a/@href').extract()
            item['postUpvote'] = post.xpath('div/div[1]/div[3]/text()').extract()
            item['commentLink'] = post.xpath('div/div[2]//ul/li[1]/a/@href').extract()
            item['rankingPosition'] = str(0)
            item['lastUpdate'] = post.xpath('div/div[2]/p[2]/time/@datetime').extract()
            item['postOrigin'] = post.xpath('div/div[2]/p[2]/a/text()').extract()
            items.append(item)
        print items
        return items
