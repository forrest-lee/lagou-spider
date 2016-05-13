# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouPositionItem(scrapy.Item):
    search_keyword = scrapy.Field()     # 搜索关键字，记点击首页左侧时的关键字
    company_short = scrapy.Field()      # 公司简称
    company = scrapy.Field()            # company name
    company_id = scrapy.Field()         # 公司ID
    company_size = scrapy.Field()       # 公司规模
    education = scrapy.Field()          # 学历要求
    finance_stage = scrapy.Field()      # 融资规模
    industry = scrapy.Field()           # 行业
    city = scrapy.Field()               # 城市
    position_type = scrapy.Field()      # 职位类型
    position_name = scrapy.Field()      # 职位名称
    position_id = scrapy.Field()        # 职位id
    advantage = scrapy.Field()          # 职位诱惑
    salary = scrapy.Field()             # 薪水
    work_year = scrapy.Field()          # 工作年限


class LagouJobDescItem(scrapy.Item):
    position_id = scrapy.Field()        # 职位ID
    dept = scrapy.Field()               # 部门名称
    job_desc = scrapy.Field()           # 职位描述，包括职责与要求
    job_responsibility = scrapy.Field() # 工作职责
    job_requirement = scrapy.Field()    # 任职要求
