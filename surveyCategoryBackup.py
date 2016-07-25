#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime
import sys
import re
import csv
client = MongoClient()

db = client['philips_gr']
data_results = []

start = 25;
end = 29;


keys = [
    'time',
    'regularBaby',
    'sensitiveBaby',
    'sum',
    'regularChild',
    'fussyEater',
    'allergy',
    'sum',
    'regularPregnancy',
    'highRiskPregnancy',
    'sum',
    'confinementDiet',
    'sum',
    'healthBack',
    'bodyBack'
]

data_results.append(keys)

for i in range(start, end):
    day = str(i)
    if i < 10:
        day = '0' + str(i)
    regex = re.compile(r"....Apr %s.*"%day)
    result = db.surveyanswers.find({"updateTimeStamp": {'$regex': regex}})

    values = [0  for i in keys]
    for surveyAnswer in result:
        key = surveyAnswer[u'categoryFrom']
        # key = surveyAnswer[u'surveyName']
        values[keys.index('time')] = surveyAnswer[u'updateTimeStamp'][:10]
        if (key in keys):
            # print(keys[u'updateTimeStamp'])
            values[keys.index(key)] += 1
    data_results.append(values)

li = []
for col, col_data in enumerate(data_results):
    for row, row_data in enumerate(col_data):
        if len(li) < row + 1:
            li.append([])
        li[row].append(row_data)

with open('surveyOut.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['weekly survey category'])
    for row in li:
        writer.writerow(row)
