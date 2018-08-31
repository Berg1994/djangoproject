# -*- coding: utf-8 -*-
from time import sleep

import scrapy

from tianyancha.spiders.cookies_to_dict import GetCookies


class TianyanSpider(scrapy.Spider):
    name = 'tianyan'
    # allowed_domains = ['www.tianyancha.com']
    start_urls = ['https://www.tianyancha.com/']
    # 获取cookie字典类型值
    cookie = GetCookies().string_to_dict()

    # 配置cookie
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], cookies=self.cookie, callback=self.parse)

    def parse(self, response):
        # 获取省链接
        provinces_urls = response.xpath('//*[@id="web-content"]/div/div[6]/div/div[2]/div/div/div[1]/a/@href').extract()
        # 获取省名称
        provinces_name = response.xpath(
            '//*[@id="web-content"]/div/div[6]/div/div[2]/div/div/div[1]/a/text()').extract()
        for province_url in provinces_urls:
            sleep(3)
            yield scrapy.Request(url=province_url, callback=self.parse_all_cities)

    def parse_all_cities(self, response):
        print(response)
