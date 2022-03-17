import scrapy

import requests
from bs4 import BeautifulSoup

import sys
import os
from items import DoubanItem
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ffpath = os.path.abspath(os.path.join(fpath, ".."))
sys.path.append(ffpath)



# 爬取豆瓣网页对于电影《小偷家族》的评论

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/27622447/comments?start=0&limit=20&sort=new_score&status=P']

    def parse(self, response):
        # r = requests.get('https://movie.douban.com/subject/27622447/comments?start=0&limit=20&sort=new_score&status=P',headers = ua)
        # html = BeautifulSoup(r.text,'html.parser')
        # review_list = html.select('div.comment-item')
        review_list = response.xpath('//*[@id="comments"]/div[position()<21]')
        for review in review_list:
            movie_item = DoubanItem()

            # review_url = review.xpath('./div[2]/h3/span[2]/a/')
            movie_item['author_name'] = review.xpath('./div[2]/h3/span[2]/a//text()').get()
            movie_item['author_adress'] = review.xpath('./div[2]/h3/span[2]/a/@href').get()

            # vote_information = review.select('div.comment>h3>span.comment-vote>span.votes')
            movie_item['author_like'] = review.xpath('./div[2]/h3/span[1]/span//text()').get()  

            # comment_time = review.select('div.comment>h3>span.comment-info>span.comment-time')
            # movie_item['time'] = comment_time[0]['title']
            movie_item['time'] = review.xpath('./div[2]/h3/span[2]/span[3]//text()').get()


            # comment_information = review.select('div.comment>p>span.short')
            # movie_item['review'] = comment_information[0].text.strip()
            movie_item['review'] = review.xpath('./div[2]/p/span/text()').get()
            # print(movie_item)
            yield movie_item
        # next_page = html.find('a', attrs={'class': 'next'}, href = True).attrs['href']
        next_page = response.xpath('//*[@class="next"]/@href').get()
        
        if next_page != None:
            
            
            url = 'https://movie.douban.com/subject/27622447/comments'+next_page
            yield scrapy.Request(url, callback=self.parse)
            # print(next_page)
            # 获得了正确的网址 https://movie.douban.com/subject/27622447/comments?start=20&limit=20&sort=new_score&status=P&percent_type=
            # 却出现了第二页显示的问题  
            #原因：未使用scrapy里自带模块