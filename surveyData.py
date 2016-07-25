#coding=gbk

#coding=gb2312

#-*- coding: UTF-8 -*-
from pymongo import MongoClient
import datetime
import sys
import re
import csv
client = MongoClient()

db = client['philips_gr']
data_results = []
data_day_results= []

day = 27
regex = re.compile(r"....Apr %s.*"%day)


listName = {
    'displayName': [
        'category',
        'Pregnancy',
        'Breastfeeding',
        'Confinement',
        'Toddler',
        'Recovery'
    ],
    'propties': [
        'pregnancy',
        'breastfeeding',
        'confinement',
        'toddler',
        'recorvery'
    ]
}

rowName = ['Optimizer', 'Seeker', 'Aware',
            'Concerned', 'Foodie', 'Family', 'Pratical', 'Safety', 'Learner']
rowKey = [
    ['A', 'Healthy_Points'],
    ['B', 'Healthy_Points'],
    ['C', 'Healthy_Points'],
    ['D', 'Healthy_Points'],
    ['A', 'Diet_Type'],
    ['B', 'Diet_Type'],
    ['C', 'Diet_Type'],
    ['D', 'Diet_Type'],
    ['E', 'Diet_Type']
]

healthLevels = {
        'Optimizer' : ['A', 'Healthy_Points'],
        'Seeker': ['B', 'Healthy_Points'],
        'Aware': ['C', 'Healthy_Points'],
        'Concerned': ['D', 'Healthy_Points'],
        'Foodie': ['A', 'Diet_Type'],
        'Family': ['B', 'Diet_Type'],
        'Pratical': ['C', 'Diet_Type'],
        'Safety' :['D', 'Diet_Type'],
        'Learner': ['E', 'Diet_Type']
}


data_results.append(listName['displayName'])
data_day_results.append(listName['displayName'])


for key, value in zip(rowName, rowKey):
    values = [key, 0, 0, 0, 0, 0]
    values2 = [key, 0, 0, 0, 0, 0]
    for propty in listName['propties']:
        data = db.surveyanswers.find({"$and":[{ "result":
                                               {"$elemMatch":
                                                {"resultGroup":
                                                 value[1],
                                                 "content": value[0]}}},
                                              {"surveyName": propty}]})
        data2 = db.surveyanswers.find({"$and":[{ "result":
                                               {"$elemMatch":
                                                {"resultGroup":
                                                 value[1],
                                                 "content": value[0]}}},
                                              {"surveyName": propty},{
                                                  "updateTimeStamp":
                                                  {'$regex': regex}
                                              }]})
        values[listName['propties'].index(propty) + 1] = data.count()
        values2[listName['propties'].index(propty) + 1] = data2.count()
    data_results.append(values)
    data_day_results.append(values2)
    print(data_day_results)


def matrixReverse(data):
    li = []
    for col, col_data in enumerate(data):
        for row, row_data in enumerate(col_data):
            if len(li) < row + 1:
                li.append([])
            li[row].append(row_data)
    return li


with open('out.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for row in matrixReverse(data_results):
        writer.writerow(row)
    writer.writerow(['Daily Report'])
    for row in matrixReverse(data_day_results):
        writer.writerow(row)
    writer.writerow([''])
