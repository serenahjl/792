# -*- coding: utf-8 -*-
import scrapy
from qunarticket.items import QunarticketItem
from urllib.request import Request
from urllib import parse
from scrapy.http import Request



class TicketSpider(scrapy.Spider):
    name = 'ticket'
    allowed_domains = ['piao.qunar.com']
    start_urls = ['http://piao.qunar.com/ticket/list.htm?from=mpshouye_hotdest_more&keyword=%E5%B9%BF%E4%B8%9C']

    def parse(self, response):

        result_list = response.xpath("//div[@class='result_list']/div")
        item = QunarticketItem()

        for each_sight in result_list:

            sight_name = each_sight.xpath("div/div[@class='sight_item_about']/h3/a/text()").extract_first()

            tic_price =each_sight.xpath("div/div[@class='sight_item_pop']/table/tr/td/span/em/text()").extract_first()
            if not tic_price:
                tic_price = "null"

            sight_area = each_sight.xpath("div/div[@class='sight_item_about']/div[@class='sight_item_info']/div[@class='clrfix']/span[@class='area']/a/text()").extract_first()
            if not sight_area:
                sight_area = "null"

            sight_add = each_sight.xpath("div/div[@class='sight_item_about']/div[@class='sight_item_info']/p[@class='address color999']/span/text()").extract_first()
            if not sight_add:
                sight_add = "null"
            else:sight_add = sight_add.replace("地址：","")

            item['sight_name'] = sight_name
            item['tic_price'] = tic_price
            item['sight_area'] = sight_area
            item['sight_add'] = sight_add

            yield item

        next_url = response.xpath("//*[@id='pager-container']/div/a[@class='next']//@href").extract_first("")
        if next_url:
            next_url = parse.urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse)


