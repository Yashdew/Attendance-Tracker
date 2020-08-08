from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient
import requests


app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")
                                                    
mydb = myclient["Yashdb"]
mycol = mydb["Yashdb"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def register_page():
  return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    record = {
            "_id": request.form['ID'],
            "name":  request.form['Name'], 
            "username": request.form['Username'],
            "email":  request.form['Email'],
            "password":  request.form['Password']

        }
    mycol.insert_one(record)
        
    return render_template('check.html')  

@app.route('/check', methods=['POST'])
def check():
    return render_template('checkstatus.html')   
app.run(debug=True)    


    
   