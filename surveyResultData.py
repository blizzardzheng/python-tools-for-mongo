#coding=gbk

#coding=gb2312

#-*- coding: UTF-8 -*-
# export mongodb surveyanswers
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pymongo import MongoClient

import csv

data_results = []
client = MongoClient()
db = client['philips_gr']

surveyNames = [
    'breastfeeding',
    'pregnancy',
    'recovery',
    'toddler',
    'confinement'
]

for key in surveyNames:
    data_results.append(["surveyName", key])
    data = db.surveyanswers.find({"surveyName" : key})
    for re in data:
        data_results.append(["new survey", re['updateTimeStamp']])
        data_results.append(['categoryFrom', re[u'categoryFrom']])
        for answer in re[u'answers']:
            data_results.append([
                                 'questionName', answer[u'questionName'],
                                 'group', answer[u'group'],
                                 'input', answer[u'input']
                                 ])
print data_results

with open('surveyResultOut.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Survey Report'])
    for row in data_results:
        writer.writerow(row)
