# -*- coding: utf-8 -*-
import scrapy
import requests
import os
from ..items import AmazonLappyItem
DIR='C:/Users/Pcv/Documents/GitHub/Web-Scraping-Summer_of_ML/amazon_lappy/amazon_lappy/images'


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    
    start_urls = ['https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2']
    page_no=2

    def parse(self, response):
    	items=AmazonLappyItem()
    	laptop_name=response.css('.a-color-base.a-text-normal').css('::text').extract()
    	laptop_price=response.css('.a-price-whole').css('::text').extract()
    	laptop_ratings=response.css('.a-icon-alt').css('::text').extract()
    	image_urls=response.css('.s-image::attr(src)').extract()
    	items['laptop_name']=laptop_name
    	items['laptop_price']=laptop_price
    	items['laptop_ratings']=laptop_ratings
    	items['image_urls']=image_urls
    	yield items
    	for i,img_url in enumerate(image_urls):
	    		r = requests.get(img_url)
	    		with open(os.path.join(DIR,"image_{}.jpg".format(i)),'wb') as f:
	    			f.write(r.content)

    	next_item='https://www.amazon.in/s?k=laptops&page='+str(AmazonSpider.page_no)+'&qid=1560951705&ref=sr_pg_'+str(AmazonSpider.page_no)
    
    	if(AmazonSpider.page_no<5):
    		AmazonSpider.page_no=AmazonSpider.page_no+1
    		yield response.follow(next_item,callback=self.parse)
    	pass
