from pymongo import MongoClient
import json, ast
client = MongoClient()

db = client['philips_gr']

aaa = db.users.find({"email": {"$exists": "true"}})
for user in aaa:
    print('openId: ' + user[u'openId'])
    print('email: ' + user[u'email'])
# print(aaa[0][u'openId'])
