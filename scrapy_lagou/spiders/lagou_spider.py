# -*- coding: utf-8 -*-
import sys
import scrapy
import json
import re
import urllib
from scrapy_lagou.items import LagouPositionItem, LagouJobDescItem

reload(sys)
sys.setdefaultencoding('utf-8')

class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    # FIXME remove hard-coding
    keyword = 'Java'  # candicates: C, C++, Python, PHP
    city = u'武汉'
    pn = 1  # page no.
    cities = ['武汉', '深圳', '北京', '上海', '广州']
    current = 0  # 当前城市

    def start_requests(self):
        return [
            scrapy.FormRequest(
                url="http://www.lagou.com/jobs/positionAjax.json?city=武汉",
                headers={'Referer': 'http://www.lagou.com/jobs?px=default&city=武汉'},
                formdata={
                    'kd': self.keyword,
                    'first': 'false',
                    'pn': str(self.pn)
                },
                callback=self.parse
            ),
            scrapy.FormRequest(
                url="http://www.lagou.com/jobs/positionAjax.json?city=深圳",
                headers={'Referer': 'http://www.lagou.com/jobs?px=default&city=深圳'},
                formdata={
                    'kd': self.keyword,
                    'first': 'false',
                    'pn': str(self.pn)
                },
                callback=self.parse
            )
        ]

    def parse(self, resp):
        js = json.loads(resp.body_as_unicode())
        if not js['success']:
            self.logger.error('failed to get json')
        else:
            # print('#########################')
            # print '一共有%d页数据' % js['content']['pageSize']   # 一共有多少页
            # print('#########################')

            # f = open('../log.json', 'w')
            # f.write(str(js).encode('utf8', 'ignore'))
            # f.close()

            for i in range(js['content']['pageSize']):
                json_item = js['content']['positionResult']['result'][i]
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
                                     callback=self.parse_job_desc
                                     )

        self.pn = self.pn + 1
        if self.pn > js['content']['pageSize']:
            self.logger.info('Finished crawling %s pages of json feeds' %
                             js['content']['totalPageCount'])
            if self.current > 4:
                return
            else:
                self.current += 1
                self.pn = 1
                self.city = self.cities[self.current]

        # FIXME avoid duplicate
        yield scrapy.FormRequest(
            "http://www.lagou.com/jobs/positionAjax.json?city=" + urllib.quote(self.city.encode('utf8')),
            formdata={'kd': self.keyword, 'first': 'false', 'pn': str(self.pn)},
            callback=self.parse
        )

    # 解析职位描述html页面
    def parse_job_desc(self, resp):
        jd = LagouJobDescItem()
        p = re.compile('[^0-9]+([0-9]+)\.html')
        jd['position_id'] = int(p.sub(r'\1', resp.url))

        jd['dept'] = ''.join(
            resp.xpath('//*[@id="container"]/div[1]/dl[1]/dt/h1/div/text()').extract()
        ).strip().encode('utf8', 'ignore')

        subtree_root = resp.xpath('//*[@id="container"]/div[1]/dl[1]/dd[2]')[0]

        jd['job_desc'] = ''.join(
            [text.extract().strip() for text in subtree_root.xpath('.//text()')]
        ).strip().encode('utf8', 'ignore')
        jd['job_responsibility'] = ''
        jd['job_requirement'] = ''
        yield jd

    def closed(self, reason):
        self.logger.info(("Please run script `./scrapy_lagou/segmentation.py' "
                          "to do word segmentation and then calculate frequencies of every words"))
