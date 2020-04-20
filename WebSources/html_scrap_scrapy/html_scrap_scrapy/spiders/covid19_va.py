# -*- coding: utf-8 -*-
import scrapy

class Covid19VaSpider(scrapy.Spider):
    name = 'covid19_va'
    allowed_domains = ['covid19.healthdata.org']
    start_urls = ['http://https://covid19.healthdata.org/united-states-of-america/virginia/']

    def parse(self, response):
        mes = response.selector.xpath('//*[@id="root"]/div/main/div[3]/div[1]/div[2]/div[1]/div[1]/text()').get()
        print ("Mes :", mes)
