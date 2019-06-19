# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonLappyItem(scrapy.Item):
    # define the fields for your item here like:
    laptop_name = scrapy.Field()
    laptop_price = scrapy.Field()
    laptop_ratings = scrapy.Field()
    image_urls = scrapy.Field()
    pass
