# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ObsidianItem(scrapy.Item):
    # define the fields for your item here like:
    status = scrapy.Field()
    title = scrapy.Field()
    crawl_time = scrapy.Field()
    url = scrapy.Field()
