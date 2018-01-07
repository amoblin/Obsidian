#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# file name: cmdline.py
# description: TODO
# create date: 2016-09-19 14:43:48
# author: amoblin
# This file is created by Marboo<http://marboo.io> template file $MARBOO_HOME/.media/starts/default.py
# 本文件由 Marboo<http://marboo.io> 模板文件 $MARBOO_HOME/.media/starts/default.py 创建

import os
import sys
import scrapy.cmdline

base = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))

def execute():
    if len(sys.argv) <= 1:
        print("usage: %s [config file]" % sys.argv[0])
        sys.exit(0)
    filename = sys.argv[1]

    output = os.path.join(os.getcwd(), "obsidian_output.json")
    if len(sys.argv) > 2:
        output = sys.argv[2]

    if not output.startswith('/'):
        output = os.path.join(os.getcwd(), output)

    if not filename.startswith('/'):
        filename = os.path.join(os.getcwd(), filename)

    if not os.path.isfile(filename):
        print("file not exist: %s" % sys.argv[1])
        sys.exit(0)

    os.chdir(os.path.join(base, "spiders"))
    init_settings()
    scrapy.cmdline.execute(("scrapy crawl jsonspider -a path=%s -o %s" % (filename, output)).split())

def init_settings():
    content = """
[settings]
default = Obsidian.settings

[deploy]
#url = http://localhost:6800/
project = Obsidian
"""
    cfg_file = os.path.join(os.path.dirname(base), "scrapy.cfg")
    if not os.path.isfile(cfg_file):
        f = open(cfg_file, 'w')
        f.write(content)

if __name__ == "__main__":
    execute()
