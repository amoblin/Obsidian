#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name = 'Obsidian',
    version = '1.0.1',
    packages = find_packages(),
    scripts = ['obsidian.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = [
        'scrapy',
    ],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md'],
    },

    # metadata for upload to PyPI
    author = "amoblin",
    author_email = "amoblin@gmail.com",
    description = "Obsidian make web crawl easier",
    license = "MIT",
    keywords = "web crawl json",
    url = "https://github.com/amoblin/Obsidian",

    # could also include long_description, download_url, classifiers, etc.
)
