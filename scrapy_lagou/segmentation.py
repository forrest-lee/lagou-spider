# -*- coding: utf-8 -*-
import sys
import jieba
import pymongo

client = pymongo.MongoClient("localhost", 27017)
jieba.load_userdict("../userdict.txt")

reload(sys)
sys.setdefaultencoding('utf-8')


class WordSeg(object):
    def __init__(self):
        self.ignored_words = []
        self.db = client.lagou
        self.load_ignoring()

    # XXX this class should not hold other objects,
    # or else it will not be called.
    # see this link for details:
    # http://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python
    def __del__(self):
        self.db.close()

    def load_ignoring(self):
        ignores = self.db.ignored_word.find({})
        for item in ignores:
            print item
            # self.ignored_words = ignores

    def segment(self):
        results = self.db.position.distinct('search_keyword')
        keywords = [item.search_keyword for item in results]
        for kw in keywords:
            self.segment_one(kw)

    def segment_one(self, keyword):
        # print 'process keyword "%s"' % keyword
        results = self.db.job_desc.find({}, {'job_desc': 1})

        all_jd = ''
        for jd in results:
            all_jd = all_jd + jd[0]

        counter = {}
        for seg in jieba.cut(all_jd):
            seg = seg.lower()
            if seg in self.ignored_words:
                continue
            if seg not in counter:
                counter[seg] = 0
            else:
                counter[seg] += 1

        for (word, cnt) in counter.iteritems():
            self.db.word_frequency.insert_one({
                'search_keyword': keyword,
                'word': word.encode('utf8', 'ignore'),
                'cnt': cnt
            })


if '__main__' == __name__:
    ws = WordSeg()
    ws.segment()
