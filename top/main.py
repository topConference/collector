#coding:utf-8
from scrapy import cmdline
# import pipelines
# from datetime import datetime,timedelta

# def remove_old():
#     dbObject=dbHandle()
#     cursor=dbObject.cursor()
#     print('del if deadline before'+ (datetime.today()-timedelta(days=10)).strftime('%Y%m%d'))
#     cursor.excute("delete from CONFERENCE where deadline<=%s",((datetime.today()-timedelta(days=10)).strftime('%Y%m%d'),))
#     cursor.connection.commit()
# update info
cmdline.execute("scrapy crawl topspider".split())
#del if deadline past 10 days
#remove_old()

