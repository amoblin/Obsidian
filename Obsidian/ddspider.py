#!/usr/bin/env python
# coding=utf-8
# File Name: dd_spider.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 一  8/ 8 13:51:08 2016

import time

from Obsidian.items import ObsidianItem

from scrapy import Spider
from scrapy.http import Request


class DDSpider(Spider):

    def juice(self, s, pipline, should_extract=1):
        selector = s
        command = "selector"
        for pip in pipline:
            if pip["type"] != "re":
                command = "%s.%s('%s')" % (command, pip["type"], pip["value"])
            else:
                command = "%s.re(%s)" % (command, pip["value"])
        print "*"*20
        print command
        print "*"*20
        selector = self.eval(selector, command)

        if pipline[-1]["type"] != "re" and should_extract:
            selector = selector.extract()
        return selector

    def drink(self, content, regex='', index=1):
        return "".join(content).strip()

    def eval(self, selector, code):
#        print "********** will execute: %s" % code
        return eval(code)

    def parse(self, response):
        for item in map(lambda x: self.prefix + x, self.juice(response, self.link_array_pipline)):
            yield Request(url = item, callback=self.parse_page)

    def parse_page(self, response):
        main_content_selector = self.juice(response, self.main_content_pipline, 0)
        item = ObsidianItem()
        item['status'] = 1
        item['url'] = response.url
        item['crawl_time'] = int(time.time())
        return item
