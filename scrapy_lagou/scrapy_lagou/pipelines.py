# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy_lagou.items import LagouPositionItem, LagouJobDescItem
import mysql.connector


class LagouPositionPipeline(object):

    # FIXME move below to settings.py
    db = 'lagou'
    user = 'root'
    passwd = ''

    def __init__(self, user, passwd):
        #self.user = user
        #self.passwd = passwd
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls('TODO', 'TODO')

    def open_spider(self, spider):
        # TODO all instances of pipeline share one db conn.
        self.dbc = mysql.connector.connect(
                user = self.user,
                passwd = self.passwd,
                host = 'localhost',
                database = self.db
                )
        self.cursor = self.dbc.cursor()
        self.cursor.execute('set names utf8')

    def close_spider(self, spider):
        self.cursor.close()
        self.dbc.close()

    def process_item(self, item, spider):
        if not isinstance(item, LagouPositionItem):
            return item
        fmt = (
                "insert into position "
                "(search_keyword, company_id, company_short, company, company_size, "
                "finance_stage, industry, city, "
                "position_id, position_type, position_name, "
                "advantage, salary, work_year, education) "
                "values ("
                "%(search_keyword)s, %(company_id)s, %(company_short)s, %(company)s, %(company_size)s, "
                "%(finance_stage)s, %(industry)s, %(city)s, "
                "%(position_id)s, %(position_type)s, %(position_name)s, "
                "%(advantage)s, %(salary)s, %(work_year)s, %(education)s)"
                )
        data = {
                "search_keyword" : item["search_keyword"],
                "company_id" : item["company_id"],
                "company_short" : item["company_short"],
                "company" : item["company"],
                "company_size" : item["company_size"],
                "finance_stage" : item["finance_stage"],
                "industry" : item["industry"],
                "city" : item["city"],
                "position_id" : item["position_id"],
                "position_type" : item["position_type"],
                "position_name" : item["position_name"],
                "advantage" : item["advantage"],
                "salary" : item["salary"],
                "work_year" : item["work_year"],
                "education" : item["education"],
                }
        self.cursor.execute(fmt, data)
        raise DropItem()


class LagouJobDescPipeline(object):

    # FIXME move below to settings.py
    db = 'lagou'
    user = 'root'
    passwd = ''

    def __init__(self, user, passwd):
        #self.user = user
        #self.passwd = passwd
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls('TODO', 'TODO')

    def open_spider(self, spider):
        # TODO all instances of pipeline share one db conn.
        self.dbc = mysql.connector.connect(
                user = self.user,
                passwd = self.passwd,
                host = 'localhost',
                database = self.db
                )
        self.cursor = self.dbc.cursor()
        self.cursor.execute('set names utf8')

    def close_spider(self, spider):
        self.cursor.close()
        self.dbc.close()

    def process_item(self, item, spider):
        if not isinstance(item, LagouJobDescItem):
            return item
        fmt = (
                "insert into job_desc (position_id, dept, job_desc)"
                "values (%s, %s, %s)"
                )
        data = (item['position_id'], item['dept'], item['job_desc'])
        self.cursor.execute(fmt, data)
        raise DropItem
