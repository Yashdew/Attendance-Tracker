from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient
import requests


app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")
                                                    
mydb = myclient["Yashdb"]
mycol = mydb["Yashdb"]

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        new_ID = request.form.get('ID')
        new_name = request.form.get('Name')
        new_Username = request.form.get('Username')
        new_email = request.form.get('Email')
        new_password = request.form.get('Password')

    mydict = { "_id": new_ID,
    "name": new_name, 
    "username": new_Username,
    "email": new_email,
    "password": new_password
    }
    mycol.insert_one(mydict)
    return render_template('index.html')