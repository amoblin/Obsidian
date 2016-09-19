#!/usr/bin/env python
# coding=utf-8
# File Name: myspider.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 五  8/ 5 18:12:46 2016

from Obsidian.ddspider import DDSpider
from Obsidian.ddsourcejsonconfig import DDSourceJsonConfig

class JsonSpider(DDSpider):
    config = DDSourceJsonConfig("config.json")

#    name = config.name
    name = "jsonspider"
    allowed_domains= config.allowed_domains
    start_urls = config.start_urls
    prefix = config.prefix
    link_array_pipline = config.link_array_pipline
    main_content_pipline = config.main_content_pipline
    item_pipline = config.item_pipline

