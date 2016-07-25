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
result = db.asserts.find({"name": "listProduct"})

sliderShowData = []


def getSliderShow(li):
    if (li['code'] == 'SC5370_10' and li['extension'] == 'tif'):
        print(li)
# for assets
# for element in result:
#     asset = element['data']['assets']['asset']
#     for tmp in asset:
#         getSliderShow({
#             'code': tmp['code'],
#             'extension': tmp['extension'],
#             'types': tmp['type'],
#             'asset': tmp['asset']
#         })
#         sliderShowData.append({
#             tmp['code'],
#             tmp['extension'],
#             tmp['type'],
#             tmp['asset']
#         })


# for title
for element in result:
    products = element['data']['products']
    for tmp in products:
        # print(tmp['ctn'], tmp['productTitle'].encode('gbk'))
        stra = tmp['ctn'].encode('utf-8') + '  '+ tmp['productTitle'].encode('utf-8')
        print(stra)






        # print(tmp['code'], tmp['extension'], tmp['type'], tmp['asset'])

# for line in sliderShowData:
#     print(line)
