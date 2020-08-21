from flask import Flask, render_template, request, redirect, flash
import pymongo
from pymongo import MongoClient
import requests
import pandas as pd
import json
import time 

UPLOAD_FOLDER = './path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv'} 



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")

                                                 
mydb = myclient["Yashdb"]
mycol = mydb["Yashdb"]

mydb1 = myclient["app"]
mycol1 = mydb["users1"]

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/signup')
def register_page():
  return render_template('signup.html')
  

@app.route('/register', methods=['POST'])
def register():
    valid = True
    if request.form['Email'] == "":
        valid = False
        flash("Email cannot be empty")
        return redirect("/signup")
    if request.form['Password'] == "":
        valid = False
        flash("Password cannot be empty")
        return redirect("/signup")
    if request.form['Name'] == "":
        valid = False
        flash("Name cannot be empty")
        return redirect("/signup")
    if request.form['Password'] != request.form['CPassword']:
        valid = False
        flash("Your passwords need to match")
        return redirect("/signup")
    if not valid:
        return redirect("/signup")
    else:
        record = {
                "_id": request.form['ID'],
                "name":  request.form['Name'], 
                "username": request.form['Username'],
                "email":  request.form['Email'],
                "password":  request.form['Password']

            }
        mycol.insert_one(record)
        
        return render_template('check.html')  

@app.route('/login')
def check1():
    return render_template('check.html')

@app.route('/check', methods=['POST'])
def check():
    print(request.form['email'])
    for x in mycol.find():
       # print(x['email'])
        if x['email']==request.form['email'] and x['password']==request.form['Password']:
            #print(request.form['email'])
            name=x['name']
            username=x['username']
            email=x['email']
          
    return render_template('checkstatus.html',name=name,username=username,email=email)  

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 

@app.route('/upload', methods=['POST'])
def download():
    #filename=request.form['myfile']
    print(request.form)
    print(request.files.get('myfile'))
    df = pd.read_csv(request.files.get('myfile'))
    print(df)
    #mycol1.insert_many(data)
    return render_template('download.html')


app.run(debug=True)   



    
   