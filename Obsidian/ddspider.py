#!/usr/bin/env python
# coding=utf-8
# File Name: dd_spider.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 一  8/ 8 13:51:08 2016

import time
import scrapy
from Obsidian.items import ObsidianItem

from scrapy import Spider
from scrapy.http import Request

class DDSpider(Spider):

    def juice(self, s, pipline, should_extract=1):
        selector = s
        command = "selector"
        for pip in pipline:
            if not 'type' in pip:
                continue
            if pip["type"] != "re":
                command = "%s.%s('%s')" % (command, pip["type"], pip["value"])
            else:
                command = "%s.re(%s)" % (command, pip["value"])

        print("*"*20)
        print(command)
        print("*"*20)
        selector = self.eval(selector, command)

        if len(pipline) > 0 and pipline[-1]["type"] != "re" and should_extract:
            selector = selector.extract()

            if not 'should_join' in pipline[-1] or pipline[-1]['should_join'] != 0:
                return "".join(selector).strip()
        return selector

    def drink(self, content, regex='', index=1):
        return "".join(content).strip()

    def eval(self, selector, code):
#        print "********** will execute: %s" % code
        return eval(code)


    def parse(self, response):
        if len(self.link_array_pipline) == 0:
            yield self.parse_page(response)
        elif isinstance(self.link_array_pipline[0], list):
            for item in self.parse_step_generator()(response):
                yield item
        else:
            for item in map(lambda x: self.prefix + x, self.juice(response, self.link_array_pipline)):
                yield Request(url = item, callback=self.parse_page)

    def parse_step_generator(self, i=0):
        def fun(response):
            if i >= len(self.link_array_pipline):
                yield self.parse_page(response)
            else:
                pipline = self.link_array_pipline[i]
                for item in map(lambda x: self.prefix + x, self.juice(response, pipline)):
                    yield Request(url = item, callback=self.parse_step_generator(i+1))
        return fun

    def parse_page(self, response):
        main_content_selector = self.juice(response, self.main_content_pipline, 0)
        item = ObsidianItem()
        for key, value in self.item_pipline.items():
            if key not in ObsidianItem.fields:
                ObsidianItem.fields[key] = scrapy.Field()
            item[key] = self.juice(main_content_selector, value)
        item['url'] = response.url
        item['crawl_time'] = int(time.time())
        item['status'] = 1
        return item
