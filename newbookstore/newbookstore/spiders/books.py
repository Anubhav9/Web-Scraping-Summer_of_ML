# -*- coding: utf-8 -*-
import scrapy
import requests
import os
import sys
sys.path.append("..")
from .. items import NewbookstoreItem



class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']
    page_no=2
    def parse(self, response):
    	items=NewbookstoreItem()
    	product_name=response.css('.product_pod a::text').extract()
    	product_price=response.css('.price_color::text').extract()
    	product_image=response.css('.thumbnail::attr(src)').extract()
    	for items in zip(product_name,product_price,product_image):
    		scrapped_info={
    		'product_image':items[0],
    		'product_name' :items[1],
    		'product_price':items[2]
    		}
    	#items['product_name']=product_name
    	#items['product_price']=product_price
    	#items['product_image']=product_image
    		yield scrapped_info
    	next_result='http://books.toscrape.com/catalogue/page-'+str(BooksSpider.page_no)+'.html'
    	if(BooksSpider.page_no<51):
    		BooksSpider.page_no=BooksSpider.page_no+1
    		yield response.follow(next_result,callback=self.parse)

    	