#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-


from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
import re

client = MongoClient()

surveyName = sys.argv[1]

db = client['philips_gr']
result = db.users.find({ "$and":[{"email": {"$exists": "true"}},
                        {"projects":{"$elemMatch":{
                            "project": ObjectId("56fb6ca846e5a97b054ef051"),
                            "feedbackType": "survey"}}}]})

for element in result:
    for feedback in element[u'projects'][0][u'feedbacks']:
        result2 = db.surveyanswers.find({"_id": feedback})
        for element2 in result2:
            if (element2[u'surveyName'] == surveyName):
                print(element[u'email'])
