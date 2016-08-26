#!/usr/bin/env python
# coding=utf-8
# File Name: ddsourcejsonconfig.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 五  8/26 14:01:27 2016

import json

from Obsidian.ddsourceconfig import DDSourceConfig

class DDSourceJsonConfig(DDSourceConfig):
    def __init__(self, filename=""):
        if len(filename) == 0:
            return
        with open(filename) as data_file:
            config = json.load(data_file)
            self.name = config["name"]
            self.allowed_domains= config["allowed_domains"]
            self.start_urls = config["start_urls"]
            self.prefix = config["prefix"]
            self.link_array_pipline = config["link_array_pipline"]
            self.main_content_pipline = config["main_content_pipline"]
            self.item_pipline = config["item_pipline"]
