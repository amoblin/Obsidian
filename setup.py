#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file name: setup.py
# description: TODO
# create date: 2016-09-19 13:37:41
# author: amoblin
# This file is created by Marboo<http://marboo.io> template file $MARBOO_HOME/.media/starts/default.py
# 本文件由 Marboo<http://marboo.io> 模板文件 $MARBOO_HOME/.media/starts/default.py 创建

from setuptools import setup, find_packages

setup(
    name = "Obsidian",
    version = "0.1",
    packages = find_packages(),
    scripts = ['obsidian.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
    },

    # metadata for upload to PyPI
    author = "amoblin",
    author_email = "amoblin@gmail.com",
    description = "Obsidian make web crawl easier",
    license = "MIT",
    keywords = "web crawl json",
    url = "https://github.com/amoblin/Obsidian",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
