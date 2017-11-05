# from pymongo import MongoClient
# import pprint
# client = MongoClient('localhost', 27017)
# db = client['top_conference']
# post={'topic':'topvic'}
# collection = db['CONFERENCE']
# print(collection.insert_one(post).inserted_id)
# pprint.pprint(collection.find_one())
# posts.update_one({'topic': item['topic']}, {"topic": item['topic'], "deadline": deadline, "start_date": start_date
#     , "end_date": end_date, "url": item['url'], 'address': item['address'], 'img': item['img'],
#                                             'h5index': item['h5index']
#     , 'info': item['info']}, {upsert: true})
# self.num += 1
from scrapy import Item,Field

class top(Item):
    c=Field()
    b=Field()
a=top()
a.pop('b',None)
# print(dict(a))
print("""{0}
    {1}""".format(1,2))