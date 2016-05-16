import sys
import pymysql.cursors
import json

# reload(sys)
# sys.setdefaultencoding('utf-8')


def default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(
            calendar.timegm(obj.timetuple()) * 1000 +
            obj.microsecond / 1000
        )
        return millis
    raise TypeError('Not sure how to serialize %s' % (obj,))


db = 'lagou'
user = 'root'
passwd = ''

dbc = pymysql.connect(
    user=user,
    passwd=passwd,
    host='localhost',
    database=db,
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = dbc.cursor()


# sql = 'select * from lagou.position'
# count = cursor.execute(sql)
# t = cursor.fetchone()['time']
# print(cursor.fetchone())

sql = 'select * from lagou.position'
result = cursor.execute(sql)
f = open('./lagou_json/position.json', 'w')
for item in cursor.fetchall():
    f.write(json.dumps(item, default=default, ensure_ascii=False))
f.close()

sql = 'select * from lagou.job_desc'
result = cursor.execute(sql)
f = open('./lagou_json/job_desc.json', 'w')
for item in cursor.fetchall():
    f.write(json.dumps(item, default=default, ensure_ascii=False))
f.close()

sql = 'select * from lagou.ignored_word'
result = cursor.execute(sql)
f = open('./lagou_json/ignored_word.json', 'w')
for item in cursor.fetchall():
    f.write(json.dumps(item, ensure_ascii=False))
f.close()

sql = 'select * from lagou.word_frequency'
result = cursor.execute(sql)
f = open('./lagou_json/word_frequency.json', 'w')
for item in cursor.fetchall():
    f.write(json.dumps(item, ensure_ascii=False))
f.close()

dbc.close()