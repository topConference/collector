# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class topItem(Item):
    # /page-?
    #pp_url=Field()
    # .../?p=7232
    pageurl=Field()

    #conference data
    #topic name
    topic=Field()
    # submission_deadline
    deadline=Field()
    # conference_submission_link
    link=Field()
    # conference_dates
    dates=Field()
    # conference_address
    address=Field()
    # proceedings_indexed_by
    proceed=Field()
    # conference_call_for_papers
    call=Field()

    # extra info
    #is_top_conference
    top=Field()
    #GoogleScholarH5index
    h5index=Field()
    #CORE 2017 Rating
    c17_rate=Field()
    #Guide2Research Overall  Ranking
    g2r_rank=Field()
    #Category Rankings
    cate_rank=Field()
    #extra
    extra=Field()
    # #Image  Processing & Computer    Vision
    # ipcv=Field()
    # #Machine Learning & Arti.Intelligence
    # mlai=Field()
    # #Signal  Processing
    # sp=Field()
