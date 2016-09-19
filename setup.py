from setuptools import setup, find_packages

setup(
    name = "Obsidian",
    version = "1.0",
    packages = find_packages(),
    scripts = ['obsidian'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = [
        'docutils>=0.3',
        'scrapy'
    ],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
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
