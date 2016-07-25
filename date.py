#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-

from pymongo import MongoClient
from datetime import datetime
import sys
import re
import csv
client = MongoClient()


start = datetime(2016, 04, 01, 0, 0, 0)
end = datetime(2016, 05, 01, 0, 0, 0)

db = client['philips_gr']
result = db.surveyanswers.find({"updateTimeStamp": {"$gte": start,"$lt": end}})

print('totally' + result.count())
for doc in result:
    print(doc[u'updateTimeStamp'])
