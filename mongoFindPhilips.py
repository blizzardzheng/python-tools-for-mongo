# coding=gbk


#-*- coding: UTF-8 -*-


from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import sys
import csv
data_results = []

client = MongoClient()

db = client['philip-test']
result = db.asserts.find({})

for element in result:

    products = element[u'data']
    for tmp in products:
        print(tmp['Model'])
