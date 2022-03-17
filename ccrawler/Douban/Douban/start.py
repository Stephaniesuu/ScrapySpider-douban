from scrapy import cmdline
import os
#cmdline.execute('scrapy crawl douban'.split())

str=('scrapy crawl douban')   #运行cloud.py文件 
p=os.system(str)
print('爬虫生成结果：')  
print(p)  #打印执行结果 0表示 success ， 1表示 fail

# str=('python ./cloud.py')   #运行cloud.py文件 
# p=os.system(str)
# print('词云图生成结果：')  
# print(p)  #打印执行结果 0表示 success ， 1表示 fail