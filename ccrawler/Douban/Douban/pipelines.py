# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class DoubanPipeline(object):
    def __init__(self):
        f = open('moviewreview.csv', 'w', encoding='utf-8-sig',newline='')
        fieldnames = [
            'author_name', 'time','author_like', 'review','author_adress'

            
        ]

        self.writer = csv.DictWriter(f, fieldnames=fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item