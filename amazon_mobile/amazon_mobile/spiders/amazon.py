# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonMobileItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/s?k=4g+mobile+phones&rh=n%3A1389401031&ref=nb_sb_noss']

    def parse(self, response):
    	items=AmazonMobileItem()
    	product_name=response.css('.a-color-base.a-text-normal').css('::text').extract()
    	product_price=response.css('.a-price-whole').css('::text').extract()
    	product_img=response.css('.s-image::attr(src)').extract()
    	items['product_name']=product_name
    	items['product_price']=product_price
    	items['product_img']=product_img
    	yield items
    	pass
