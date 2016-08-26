#!/usr/bin/env python
# coding=utf-8
# File Name: ddsourceconfig.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 五  8/26 13:53:17 2016

class DDSourceConfig(object):
    name = ""
    prefix = ""
    allowed_domains = []
    start_urls = []
    link_array_pipline = [{}]
    main_content_pipline = [{}]
    item_pipline = {}

    def __init__(self):
        pass
