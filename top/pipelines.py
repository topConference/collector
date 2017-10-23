# -*- coding: utf-8 -*-
#coding:utf-8
import MySQLdb
from top import settings
def dbHandle():
    conn = MySQLdb.connect(
        host = settings.MYSQL_HOST,
        port = settings.MYSQL_PORT,
        user = settings.MYSQL_USER,
        passwd = settings.MYSQL_PASSWD,
        charset = "utf8",
        use_unicode = False
    )
    return conn

class TopPipeline(object):
    def process_item(self, item, spider):
        print('process_item'+item['topic'])
        return

        #add to mysql
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE "+settings.MYSQL_DBNAME)
        sql = "INSERT INTO %s VALUES(%s,%s,%s,%s,%s)" % settings.MYSQL_TABLE
        try:
            cursor.execute(sql, (item['topic'], item['deadline'], item['link']
                                 ,item['datas'],item['address'], item['info']))
            cursor.connection.commit()
        except BaseException as e:
            print("error", e)
            dbObject.rollback()
        return item
