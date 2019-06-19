# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PepperfryItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_company = scrapy.Field()
    product_price = scrapy.Field()
    image_urls = scrapy.Field()


    pass
