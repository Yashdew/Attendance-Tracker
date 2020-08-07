import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")
                                                    
mydb = myclient["Yashdb"]
mycol = mydb["Yashdb"]

num=2
name="YashDewangan"
add1="RHE"
mydict = { "_id": num,
 "name": name, 
 "address": add1
 }
def insertEntry():
    x = mycol.insert_one(mydict)
print(x.inserted_id)