# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from scrapy.exceptions import DropItem
from scrapy_lagou.items import LagouPositionItem, LagouJobDescItem

import pymongo
client = pymongo.MongoClient("localhost", 27017)


reload(sys)
sys.setdefaultencoding('utf-8')


class LagouPipeline(object):
    # FIXME move below to settings.py

    def __init__(self, user, passwd):
        self.db = ''
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls('TODO', 'TODO')

    def open_spider(self, spider):
        # TODO all instances of pipeline share one db conn.
        self.db = client.lagou

    def close_spider(self, spider):
        self.db.close()



class LagouPositionPipeline(LagouPipeline):
    def process_item(self, item, spider):
        if not isinstance(item, LagouPositionItem):
            return item

        self.db.position.insert_one({
            'search_keyword': item['search_keyword'],
            'company_id': item['company_id'],
            'company_short': item['company_short'],
            'company': item['company'],
            'company_size': item['company_size'],
            'finance_stage': item['finance_stage'],
            'industry': item['industry'],
            'city': item['city'],
            'position_id': item['position_id'],
            'position_type': item['position_type'],
            'position_name': item['position_name'],
            'advantage': item['advantage'],
            'salary': item['salary'],
            'work_year': item['work_year'],
            'education': item['education'],
        })

        raise DropItem()


class LagouJobDescPipeline(object):
    def process_item(self, item, spider):
        if not isinstance(item, LagouJobDescItem):
            return item

        self.db.job_desc.insert_one({
            'position_id': item['position_id'],
            'dept': item['dept'],
            'job_desc': item['job_desc']
        })
        raise DropItem
