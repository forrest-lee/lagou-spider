# lagou_spider

## 环境配置 setting envirioment
```
virtualenv venv
source venv/bin/activate
pip install -r package.txt
```

## 启动爬虫 start spider
`scrapy crawl lagou`


## 计算词频 calculate word frequency
python ./scrapy_lagou/segmentation.py


# 相关说明 Instructions
`mysql2json.py` 是用来将mysql数据库导出成json格式以便导入mongodb的脚本
```shell
mkdir lagou_json
python mysql2json.py
```