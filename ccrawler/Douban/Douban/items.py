# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    
    author_adress = scrapy.Field() # 评论者个人主页地址
    author_name = scrapy.Field() # 评论者id
    author_like = scrapy.Field() # 评论获赞数
    review = scrapy.Field() # 评论内容
    time = scrapy.Field() # 评论时间
    pass
