#!/usr/bin/env python
# coding=utf-8
# File Name: road_bicycle_item.py
# Author: amoblin <amoblin@gmail.com>
# Created Time: 四  8/25 23:08:40 2016

import scrapy
from Obsidian.items import ObsidianItem

class RoadBicycleItem(ObsidianItem):
    image = scrapy.Field()
