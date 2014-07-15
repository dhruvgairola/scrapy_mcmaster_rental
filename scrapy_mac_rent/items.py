# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMacRentItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field()
    url = scrapy.Field()
    zone = scrapy.Field()
    lease = scrapy.Field()
    rooms_avail = scrapy.Field()
    rent_amt = scrapy.Field()
    contact = scrapy.Field()
    dist = scrapy.Field()
    dirn = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    contact_name = scrapy.Field()
    contact_ph = scrapy.Field()
    contact_sec_ph = scrapy.Field()
    num_bedrooms_for_rent = scrapy.Field()
    num_bedrooms = scrapy.Field()
    internet = scrapy.Field()
    utils = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
    female_keyword = scrapy.Field()
    pass

