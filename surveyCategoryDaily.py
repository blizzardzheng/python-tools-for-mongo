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


days = sys.argv[1]

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


for i in range(0, days - 1):

    tmp = datetime.date.today() - datetime.timedelta(days = i)
    end = datetime.datetime.combine(tmp, datetime.time.max)
    start = datetime.datetime.combine(tmp, datetime.time.min)

    result = db.surveyanswers.find({"updateTimeStamp": {"$gte": start,"$lt": end}})

    values = [0  for i in keys]
    values[keys.index('time')] = start.strftime('%d/%m/%y')
    for surveyAnswer in result:
        key = surveyAnswer[u'categoryFrom']
        # key = surveyAnswer[u'surveyName']
        if (key in keys):
            # print(keys[u'updateTimeStamp'])
            values[keys.index(key)] += 1
    lastSum = 1;

    for index, summ in enumerate(keys):
        if (summ == 'sum'):
            for i in range(lastSum, index):
                values[index] += values[i]
                lastSum = index + 1

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
