#!/usr/bin/env python
# coding=utf-8
# File Name: myspider.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 五  8/ 5 18:12:46 2016

from Obsidian.ddspider import DDSpider
from Obsidian.ddsourcejsonconfig import DDSourceJsonConfig

class JsonSpider(DDSpider):
    name = "jsonspider"
    def __init__(self, path='config.json', **kwargs):
        super().__init__(**kwargs)
        config = DDSourceJsonConfig(path)
        #name = config.name
        self.allowed_domains= config.allowed_domains
        self.start_urls = config.start_urls
        self.prefix = config.prefix
        self.link_array_pipline = config.link_array_pipline
        self.main_content_pipline = config.main_content_pipline
        self.item_pipline = config.item_pipline
