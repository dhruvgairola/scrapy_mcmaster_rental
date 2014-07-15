# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_mac_rent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_mac_rent'

SPIDER_MODULES = ['scrapy_mac_rent.spiders']
NEWSPIDER_MODULE = 'scrapy_mac_rent.spiders'

ITEM_PIPELINES = { 'scrapy_mac_rent.pipelines.ScrapyMacRentPipeline': 800,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_mac_rent (+http://www.yourdomain.com)'
