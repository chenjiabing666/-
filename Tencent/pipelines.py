# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,codecs
class TencentPipeline(object):
    def __init__(self):
        self.file=codecs.open('duty_file.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def close_file(self,spider):
        self.file.close()

