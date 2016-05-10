# -*- coding: utf-8 -*-

import scrapy
import json
import re
import urllib
from scrapy_lagou.items import LagouPositionItem, LagouJobDescItem

class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    # FIXME remove hard-coding
    keyword = 'C' # candicates: C, C++, Python, PHP
    city = u'深圳'
    pn = 1      # page no.

    def start_requests(self):
        return [
                scrapy.FormRequest(
                    "http://www.lagou.com/jobs/positionAjax.json?city=" + urllib.quote(self.city.encode('utf8')),
                    formdata = {'kd' : self.keyword, 'first' : 'false', 'pn' : str(self.pn)},
                    callback = self.parse
                    ),
                ]

    def parse(self, resp):
        js = json.loads(resp.body_as_unicode())
        if not js['success']:
            self.logger.error('failed to get json')
        else:
            for i in range(js['content']['pageSize']):
                json_item = js['content']['result'][i]
                position = LagouPositionItem()
                position['search_keyword'] = self.keyword
                position['company_short'] = json_item['companyName']
                position['company'] = json_item['companyShortName']
                position['company_id'] = json_item['companyId']
                position['company_size'] = json_item['companySize']
                position['education'] = json_item['education']
                position['finance_stage'] = json_item['financeStage']
                position['industry'] = json_item['industryField']
                position['city'] = self.city
                position['position_type'] = json_item['positionType']
                position['position_name'] = json_item['positionName']
                position['position_id'] = json_item['positionId']
                position['advantage'] = json_item['positionAdvantage']
                position['salary'] = json_item['salary']
                position['work_year'] = json_item['workYear']
                yield position

                yield scrapy.Request('http://www.lagou.com/jobs/' + str(json_item['positionId']) + '.html',
                        callback = self.parse_job_desc
                        )

        self.pn = self.pn + 1
        if self.pn > js['content']['totalPageCount']:
            self.logger.info('Finished crawling %s pages of json feeds' %
                    js['content']['totalPageCount'])
            return
        # FIXME avoid duplicate
        yield scrapy.FormRequest(
                    "http://www.lagou.com/jobs/positionAjax.json?city=" + urllib.quote(self.city.encode('utf8')),
                    formdata = {'kd' : self.keyword, 'first' : 'false', 'pn' : str(self.pn)},
                    callback = self.parse
                    )


    # 解析职位描述html页面
    def parse_job_desc(self, resp):
        jd = LagouJobDescItem()
        p = re.compile('[^0-9]+([0-9]+)\.html')
        jd['position_id'] = int(p.sub(r'\1', resp.url))

        jd['dept'] = ''.join(
                resp.xpath('//*[@id="container"]/div[1]/dl[1]/dt/h1/div/text()').extract()
                ).strip()

        subtree_root = resp.xpath('//*[@id="container"]/div[1]/dl[1]/dd[2]')[0]
        jd['job_desc'] = ''.join(
                [text.extract().strip() for text in subtree_root.xpath('.//text()')]
                ).strip()
        jd['job_responsibility'] = ''
        jd['job_requirement'] = ''
        yield jd

    def closed(self, reason):
        self.logger.info(("Please run script `./scrapy_lagou/segmentation.py' "
            "to do word segmentation and then calculate frequencies of every words"))
