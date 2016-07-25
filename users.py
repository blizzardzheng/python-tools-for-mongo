#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-
from pymongo import MongoClient
import json, ast
client = MongoClient()

db = client['philips_gr']

aaa = db.users.find()
for user in aaa:
    # print(len(user[u'projects']))
    if (len(user[u'projects']) > 0 and len(user[u'projects'][0][u'feedbacks']) > 0):
        print(user[u'openId'])
# print(aaa[0][u'openId'])
