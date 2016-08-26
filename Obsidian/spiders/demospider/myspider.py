#!/usr/bin/env python
# coding=utf-8
# File Name: myspider.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 五  8/ 5 18:12:46 2016

import time
from Obsidian.ddspider import DDSpider
from Obsidian.spiders.demospider.items import RoadBicycleItem
from Obsidian.ddsourcejsonconfig import DDSourceJsonConfig

class MySpider(DDSpider):
    config = DDSourceJsonConfig("sourceconfig.json")

    name = config.name
    allowed_domains= config.allowed_domains
    start_urls = config.start_urls
    prefix = config.prefix
    link_array_pipline = config.link_array_pipline
    main_content_pipline = config.main_content_pipline
    item_pipline = config.item_pipline

    def parse(self, response):
        main_content_selector = self.juice(response, self.main_content_pipline, 0)
        item = RoadBicycleItem()
        item['status'] = 1
        item['url'] = response.url
        item['crawl_time'] = int(time.time())
        for key, value in self.item_pipline.iteritems():
            item[key] = self.juice(main_content_selector, value)
        return item
