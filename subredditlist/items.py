# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class redditItems(scrapy.Item):
	postTitle = scrapy.Field()
	postLink = scrapy.Field()
	postUpvote = scrapy.Field()
	commentLink = scrapy.Field()
	rankingPosition = scrapy.Field()
	lastUpdate = scrapy.Field()
	subcategory = scrapy.Field()
	postOrigin = scrapy.Field()
