#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime
import sys
import re
import csv
client = MongoClient()

db = client['urlshorten']
data_day_results_PV= []

events = sys.argv[1]
days = sys.argv[2]

data_day_results_PV.append(['date', 'pv', 'uv'])
for i in range(0, int(days) - 1):
    tmp = datetime.date.today() - datetime.timedelta(days = i)
    end = datetime.datetime.combine(tmp, datetime.time.max)
    start = datetime.datetime.combine(tmp, datetime.time.min)

    pv = db.visits.find({"$and": [{"created": {"$gte": start,"$lt": end}}, {"_shortId": events}]})
    uv = db.visits.distinct("ip", {"$and": [{"created": {"$gte": start,"$lt": end}}, {"_shortId": events}]})
    data_day_results_PV.append([tmp.strftime('%m/%d/%Y'), pv.count(), len(uv)])

def matrixReverse(data):
    li = []
    for col, col_data in enumerate(data):
        for row, row_data in enumerate(col_data):
            if len(li) < row + 1:
                li.append([])
            li[row].append(row_data)
    return li

fileName = 'urlShortenData_' + events + '.csv'
with open(fileName, 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for row in matrixReverse(data_day_results_PV):
        writer.writerow(row)
