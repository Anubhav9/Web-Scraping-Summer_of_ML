# -*- coding: utf-8 -*-
import scrapy
import requests
import os
DIR='C:/Coding Blocks-Assignments/images'
from ..items import PepperfryItem


class PepperfrySpider(scrapy.Spider):
    name = 'pepperFry'
    start_urls = ['https://www.pepperfry.com/site_product/search?q=book+shelf&as=1&src=os']

    def parse(self, response):
    	items=PepperfryItem()
    	product_name=response.css('.xs-12 a').css('::text').extract()
    	product_company=response.css('.clip-dtl-brand-name').css('::text').extract()
    	product_price=response.css('.clip-offr-price').css('::text').extract()
    	image_urls=response.css('.vip-product-img::attr(src)').extract()
    	items['product_name']=product_name
    	items['product_company']=product_company
    	items['product_price']=product_price
    	items['image_urls']=image_urls

    	yield items
    	for i,img_url in enumerate(image_urls):
	    		r = requests.get(img_url)
	    		with open(os.path.join(DIR,"image_{}.gif".format(i)),'wb') as f:
	    			f.write(r.content)
    
    	pass

