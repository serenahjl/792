# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import pymongo
from scrapy.conf import settings

class QunarticketPipeline(object):

    wb = Workbook()
    ws = wb.active
    ws.append(['景点名称', '门票最低价', '所在地区', '具体地址'])  # 设置表头

    def process_item(self, item, spider):

        line = [item['sight_name'], item['tic_price'], item['sight_area'], item['sight_add']] # 把数据中每一项整理出来
        self.ws.append(line) # 将数据以行的形式添加到xlsx中
        self.wb.save('/home/baicai/PycharmProjects/gd_qunar_ticket.xlsx') # 保存xlsx文件
        return item


