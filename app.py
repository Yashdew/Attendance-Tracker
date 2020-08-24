from flask import Flask, render_template, request, redirect, flash
import pymongo
from pymongo import MongoClient
import requests
import pandas as pd
import json
import time 
import datetime
import math
import gspread as gs
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

UPLOAD_FOLDER = './path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv'} 
spreadsheetid = "1l4edR5UL8Ayg9AYtLjlMspdHdMjCeQ8P8RvKBMbEcH0"


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
<<<<<<< refs/remotes/origin/kulkarni
    df = pd.read_csv(request.files.get('myfile'))
=======
    print(pd.__version__)
    try:
        df = pd.read_csv(request.files.get('myfile'),encoding='utf-16',sep='\t')
    except:
        df=pd.DataFrame()
        df = pd.read_csv(request.files.get('myfile'),sep=',')   
>>>>>>> local
    print(df)
    date = str(df['Timestamp'][0]).split()[0][:-1]
    df1 = df.sort_values(['Full Name','Timestamp'])
    XD = df1[(df1['Full Name']=='useradmin' ) | (df1['Full Name']=='Ravindra Apare')]
    x = XD['Timestamp']
    y = str(x)[15:23]
    y.split(':')
    mh,mm,ms = y.split(':')
    basetime = int(datetime.timedelta(hours=int(mh),minutes=int(mm),seconds=int(ms)).total_seconds())
    endtime = basetime + 3900
    df1.reset_index(inplace=True)
    df1.drop('index',inplace=True,axis=1)
    i=0
    a=0
    b=0
    j=0
    jo=0
    seconds1 = 0
    seconds2 = 0
    b1 = 0
    grandtotal = []
    while a < len(df1['Full Name'].unique()):
        if df1['Full Name'].value_counts().sort_index()[a]==1:
            jo = df1.iloc[i]['Timestamp'][10:18]
            h,m,s = jo.split(':')
            seconds = int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
            seconds1 = endtime - seconds
            i = i + 1
        elif df1['Full Name'].value_counts().sort_index()[a]%2 != 0:
            while b1 < math.trunc(df1['Full Name'].value_counts().sort_index()[a]/2):
                j = df1.iloc[i]['Timestamp'][10:18]
                l = df1.iloc[i+1]['Timestamp'][10:18]
                h,m,s = j.split(':')
                h1,m1,s1 = l.split(':')
                seconds = int(datetime.timedelta(hours=int(h1)-int(h),minutes=int(m1)-int(m),seconds=int(s1)-int(s)).total_seconds())
                seconds1 = seconds1 + seconds
                b1 = b1 + 1 
                i = i + 2
            b1 = 0    
            jo = df1.iloc[i]['Timestamp'][10:17]
            h,m,s = jo.split(':')
            seconds = int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()) 
            seconds2 = seconds1 + (endtime - seconds)
            seconds1 = seconds2
            i = i + 1
        elif df1['Full Name'].value_counts().sort_index()[a]%2 == 0:    
            while b < df1['Full Name'].value_counts().sort_index()[a]/2:
                j = df1.iloc[i]['Timestamp'][10:17]
                l = df1.iloc[i+1]['Timestamp'][10:17]
                h,m,s = j.split(':')
                h1,m1,s1 = l.split(':')
                seconds = int(datetime.timedelta(hours=int(h1)-int(h),minutes=int(m1)-int(m),seconds=int(s1)-int(s)).total_seconds())
                seconds1 = seconds1 + seconds
                b = b + 1
                i = i + 2
        b = 0
        grandtotal.append(seconds1)
        seconds = 0
        seconds1 = 0
        a=a+1
    new = pd.DataFrame()
    grandtotal1 = []
    Attendance = []
    for i in grandtotal:
        grandtotal1.append(str(datetime.timedelta(seconds=abs(i))))
        if(abs(i) >= 1800):
            Attendance.append('P')
        else:
            Attendance.append('A')
    new['Full Name'] = df1['Full Name'].unique()
    #new['Total Attendance Time'] = grandtotal1
    new[date] = Attendance
    print(new)
    print(date)  #Date required for final csv
    #mycol1.insert_many(data)"""
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('skn-hackclub-153a8f198669.json', scope)
    gc = gs.authorize(credentials)
    sheet = gc.open_by_key(spreadsheetid)
    wks0 = sheet.get_worksheet(0)
    Name = input("Enter Your Given UserName :")
    Password = input("Enter Your Given Password :")
    try:
        if wks0.find(Name).value:
            if wks0.find(Password).value:
                print("Logging in")
    except:
        print("Sorry you are not a authorised user")
    newName = input("Enter Your New UserName :")
    newPassword = input("Enter Your New Password :")
    subName = input("Subject name :")
    email = input("Enter your email which can access Google Sheets:")
    x = wks0.find(Name)
    wks0.update_acell(wks0.find(Name).address,newName)
    wks0.update_acell(wks0.find(Password).address,newPassword)
    wks0.update_acell("C"+str(x.row),subName)
    wks0.update_acell("D"+str(x.row),email)
    newEmail = wks0.get("D"+str(wks0.find(newName).row))[0][0]
    currentSubject = wks0.get("C"+str(wks0.find(newName).row))[0][0]
    newsheet = gs.oauth()
    s1 = newsheet.create(currentSubject)
    newsheet.insert_permission(s1.id ,'attendance@skn-hackclub.iam.gserviceaccount.com',perm_type='user',role='writer')
    newsheet.insert_permission(s1.id ,newEmail,perm_type='user',role='writer') 
       
    return render_template('download.html')


app.run(debug=True)   



    
   