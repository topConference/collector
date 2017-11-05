# -*- coding: utf-8 -*-
# coding:utf-8
import MySQLdb
import logging
from scrapy.conf import settings
from pymongo import MongoClient
from datetime import datetime
from scrapy.exceptions import DropItem


def one2two(x):
    return "{0:0=2d}".format(int(x))


def month2str(x):
    return one2two(datetime.strptime(x, '%b').month)


class MysqlPipeline(object):
    num = 0

    def __init__(self):
        conn = MySQLdb.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset="utf8mb4",
            use_unicode=True
        )
        self.cursor = conn.cursor()
        self.cursor.execute("USE " + settings.MYSQL_DBNAME)

    def process_item(self, item, spider):
        # only update deadline because that is editable
        # update all  REPLACE into table (id, name, age) values(1, "A", 19)
        date = str(item['deadline']).split()
        deadline = date[3] + month2str(date[2]) + one2two(date[1])
        # Dec 11, 2017 - Dec 14, 2017
        date = str(item['dates']).replace(',', '').split(' - ')
        date1 = date[0].split()
        start_date = date1[2] + month2str(date1[0]) + one2two(date1[1])
        date1 = date[1].split()
        end_date = date1[2] + month2str(date1[0]) + one2two(date1[1])
        sql = "INSERT INTO CONFERENCE (topic,deadline,start_date,end_date,url,address,img,h5index, info) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE deadline=%s"
        logging.info(str(self.num) + ' ' + item['topic'])
        self.num += 1
        try:
            self.cursor.execute(sql, (item['topic'], deadline, start_date, end_date, item['url'],
                                      item['address'], item['img'], item['h5index'], item['info'], deadline))
            self.cursor.connection.commit()
        except Exception as e:
            logging.error(e)
        finally:
            return item


class MongoPipeline(object):
    def __init__(self):
        self.num = 0
        self.update_num = 0
        connection = MongoClient()
        if settings['MONGODB_URL']!='':
            connection = MongoClient(
                settings['MONGODB_URL']
            )
        else:
            connection = MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT']
            )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            date = str(item['deadline']).split()
            deadline = date[3] + month2str(date[2]) + one2two(date[1])
            date = str(item['dates']).replace(',', '').split(' - ')
            date1 = date[0].split()
            start_date = date1[2] + month2str(date1[0]) + one2two(date1[1])
            date1 = date[1].split()
            end_date = date1[2] + month2str(date1[0]) + one2two(date1[1])
            i = dict(item)
            i['start_date'] = start_date
            i['end_date'] = end_date
            i['deadline'] = deadline
            # i.pop('dates',None)
            result = self.collection.replace_one({'topic': i['topic']}, i, True)
            self.update_num += result.matched_count
            logging.info(str(self.num) + ' ' + str(self.update_num)+ ' '+ i['topic'])
            self.num += 1
        return item

    def close_spider(self, spider):
        logging.info('update_num: {0} num: {1}'.format(self.update_num, self.num))