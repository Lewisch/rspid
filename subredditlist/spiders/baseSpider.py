import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from items import redditItems
from scrapy.spiders import CrawlSpider

class baseSpider(CrawlSpider):
    name = "redditSpider"

    def __init__(self, **kw):
        super(baseSpider, self).__init__(**kw)
        start_urls = kw.get('start_urls')
        allowed_domains = kw.get('allowed_domains')
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls

    print "Crawling..."

    def parse(self, response):
        print "Processing data..."
        redditPosts = Selector(response).xpath('//div[@id="siteTable"]')
        items = []
        for post in redditPosts:
            item = redditItems()
            item['postTitle'] = post.xpath('div/div[2]/p[1]/a/text()').extract()
            item['postLink'] = post.xpath('div/div[2]/p[1]/a/@href').extract()
            item['postUpvote'] = post.xpath('div/div[1]/div[3]/text()').extract()
            item['commentLink'] = post.xpath('div/div[2]//ul/li[1]/a/@href').extract()
            item['postOrigin'] = response.xpath('//body/div[1]/div[2]/span/a/text()').extract()
            items.append(item)

        return items
