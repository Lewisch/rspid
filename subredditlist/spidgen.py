#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Use this script to create a usable spider from the baseSpider class, can add methods to use any lists of urls you want to start from

import scrapy
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from spiders.baseSpider import baseSpider
from scrapy.utils.project import get_project_settings

#Adjust start_urls and allowed_domains as desired

process = CrawlerProcess(get_project_settings())
process.crawl(baseSpider, start_urls=["https://www.reddit.com/r/gaming"], allowed_domains=["reddit.com"])
process.start()
