import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")
                                                    
mydb = myclient["Yashdb"]
mycol = mydb["Yashdb"]
var = "jgdjkAHKJ@gmail.com"
for x in mycol.find():
    if x['email']==var:
           print(x['_id'])
           print(x['name'])
           print(x['username'])
           print(x['email'])

            