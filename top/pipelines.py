# -*- coding: utf-8 -*-
# coding:utf-8
import MySQLdb
from top import settings
from datetime import datetime

def dbHandle():
    conn = MySQLdb.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        passwd=settings.MYSQL_PASSWD,
        charset="utf8",
        use_unicode=False
    )
    return conn

def one2two(x):
    return "{0:0=2d}".format(int(x))
def month2str(x):
    return one2two(datetime.strptime(x,'%b').month)

class TopPipeline(object):
    def process_item(self, item, spider):
        # add to mysql
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE " + settings.MYSQL_DBNAME)
        # only update deadline because that is editable
        # update all  REPLACE into table (id, name, age) values(1, "A", 19)
        date=str(item['deadline']).split()
        deadline=date[3]+month2str(date[2])+one2two(date[1])
        # Dec 11, 2017 - Dec 14, 2017
        date=str(item['dates']).replace(',','').split(' - ')
        date1=date[0].split()
        start_date=date1[2]+month2str(date1[0])+one2two(date1[1])
        date1=date[1].split()
        end_date=date1[2]+month2str(date1[0])+one2two(date1[1])
        sql = "INSERT INTO CONFERENCE (topic,deadline,start_date,end_date,url,address,img,h5index, info) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE deadline=%s"
        try:
            cursor.execute(sql, (item['topic'], deadline,start_date,end_date, item['url'],
                                 item['address'], item['img'], item['h5index'], item['info'],deadline))
            cursor.connection.commit()
        except Exception as e:
            print("error", e)
            dbObject.rollback()
        return item
