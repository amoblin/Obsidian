# Obsidian - WebPage Crawler by json config

<!--
create time: 2016-08-26 14:43:58
Author: amoblin

This file is created by Marboo<http://marboo.io> template file $MARBOO_HOME/.media/starts/default.md
本文件由 Marboo<http://marboo.io> 模板文件 $MARBOO_HOME/.media/starts/default.md 创建
-->

base on scrapy and just write json config like this:

```json
{
    "name": "myspider",
    "prefix": "https://www.specialized.com/",
    "allowed_domains": ["specialized.com"],
    "start_urls": ["https://www.specialized.com/cn/zh/115443"],
    "link_array_pipline": [],
    "main_content_pipline": [{"type": "css", "value": ".js-body"}],
    "item_pipline": {
        "image": [{
            "type": "css", "value": ".carousel-hero__slide-image.js-lazy-slide-image::attr(data-src)"
        }]
    }
}
```

不需要开发，只需要会在浏览器中“审查元素”，然后书写json配置文件，就可以抓取网页上的特定数据。
