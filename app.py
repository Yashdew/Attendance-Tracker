from flask import Flask, render_template, request, redirect, flash, url_for, session, g, Response
import os 
import pymongo
from pymongo import MongoClient
import requests
import pandas as pd
import json
import time 
import datetime
import math
import gspread as gs
from werkzeug.security import generate_password_hash,check_password_hash
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


spreadsheetid = "1l4edR5UL8Ayg9AYtLjlMspdHdMjCeQ8P8RvKBMbEcH0"

spreadsheetid = "1l4edR5UL8Ayg9AYtLjlMspdHdMjCeQ8P8RvKBMbEcH0"


app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config.from_pyfile('config.cfg')
mail = Mail(app)
s = URLSafeTimedSerializer('Thisisasecret!')

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")

                                                 
mydb = myclient["Yashdb1"]
mycol = mydb["Yashdb1"]

mydb1 = myclient["app"]
mycol1 = mydb["users1"]

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/signup',methods=['GET'])
def register_page():
    ishwar_tu_chutiya_hain1='i$hw@rW@D@rch0d'
    return render_template('signup.html' ,ishwar_tu_chutiya_hain1=ishwar_tu_chutiya_hain1)
  

@app.route('/mainlogin', methods=['POST'])
def register():
    password=generate_password_hash(request.form['Password'])
    ishwar_tu_chutiya_hain1='i$hw@rW@D@rch0d'

    none="none"
    
    try:
        if(request.form['Email']!='' or request.form['Name']!='' or request.form['Password']!='' or request.form['CPassword']!=''):
            if(request.form['Password']==request.form['CPassword']):
                if(request.form['SID']==ishwar_tu_chutiya_hain1):
                    
                    record = {
                                "Email": request.form['Email'],
                                "Name":  request.form['Name'], 
                                "Password":  password,
                                "SID": request.form['SID'],
                                "Period1":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period2":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period3":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period4":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period5":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period6":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period7":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period8":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period9":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                },
                                "Period10":{
                                                "College":none,
                                                "Dept":none,
                                                "Year":none,
                                                "Subject":none,
                                                "Div":none

                                }
                                

                    }
                    
                    mycol.insert_one(record)
                    
                    return render_template('mainlogin.html')  
    except:
        print("Something went wrong") 


@app.route('/login')
def check1():
    return render_template('check.html')

@app.route('/check', methods=['POST'])
def check():
    password=generate_password_hash(request.form['Password'])
    newpassword=generate_password_hash(request.form['NPassword'])
    print(request.form['Email'])
    for x in mycol.find():
        
        if x['Email']==request.form['Email'] and check_password_hash(x['Password'],request.form['Password']):
            record=x
           
            if(request.form['MName']!='' or request.form['NPassword']!='' or request.form['NEmail']!=''):
                
                newrecord={"$set":{"Email":request.form['NEmail'],
                                   "Name":request.form['MName'],
                                   "Password":newpassword,
                                   
                                   "Period1":{
                                                "College":request.form['College'],
                                                "Dept":request.form['Department'],
                                                "Year":request.form['Year'],
                                                "Subject":request.form['Subject'],
                                                "Div":request.form['Div'],
                            
                                    },
                                    "Period2":{
                                                "College":request.form['College1'],
                                                "Dept":request.form['Department1'],
                                                "Year":request.form['Year1'],
                                                "Subject":request.form['Subject1'],
                                                "Div":request.form['DivA'],
                            
                                    },
                                    "Period3":{
                                                "College":request.form['College2'],
                                                "Dept":request.form['Department2'],
                                                "Year":request.form['Year2'],
                                                "Subject":request.form['Subject2'],
                                                "Div":request.form['DivB'],
                            
                                    },
                                    "Period4":{
                                                "College":request.form['College3'],
                                                "Dept":request.form['Department3'],
                                                "Year":request.form['Year3'],
                                                "Subject":request.form['Subject3'],
                                                "Div":request.form['DivC'],
                            
                                    }
                            }
                }
               
               
                mycol.update_many({"_id":record['_id']},newrecord)
                return render_template('mainlogin.html')
    Response.flash = 'Wrong Password'
    return render_template('check.html')       
      
      
######## Main Login
@app.route('/mainlogin')
def register_page_main():
  return render_template('mainlogin.html')

@app.route('/maincheck', methods=['GET','POST'])  ###Kuch bhasad hi hain yaha yaad rakhna
def checkmain():
    if request.method == 'POST':
        session.pop('user',None)
        password=generate_password_hash(request.form['Password'])
        for x in mycol.find():
            if x['Email']==request.form['Email'] and check_password_hash(x['Password'],request.form['Password']):
                name=x['Name']
                email=x['Email']
                session['user']=x['Name']
                return redirect(url_for('protected'))
                """return render_template('checkstatus.html',name=name,email=email)"""
    
    return render_template('mainlogin.html')

@app.route('/protected', methods=['GET','POST'])
def protected():
    if g.user:
        return render_template('checkstatus.html',user=session['user'])
    return redirect(url_for('mainlogin'))

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']

@app.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return render_template('mainlogin.html')
#############   

##################### Forget Password
@app.route('/forgetpassword')
def forget():
    return render_template('forget.html')

@app.route('/OTPforpassword',methods=['GET','POST'])
def forgetpassword():
    """for x in mycol.find():
        if x['Email']==request.form['Email']:"""
    email='yashdewangan123456@gmail.com'
    
    token = s.dumps(email, salt='email-confirm')
    msg = Message('Confirm Email', sender='sknhackclub@gmail.com', recipients=[email])

    link = url_for('updatepassword',token=token, _external=True)

    msg.body = "Your Link is {}".format(link)

    mail.send(msg)

    return render_template('OTP.html',email=email,token=token) 
        

@app.route('/updatepassword/<token>')
def updatepassword(token):
    try:
        email = s.loads(token,salt='email-confirm',max_age=10)
        print(email)
    except SignatureExpired:
        return 'The Token is expired'
    return 'The token works'
###################

@app.route('/upload',methods=['GET','POST'])
def dashboard():
    
    return render_template('upload.html') 

@app.route('/uploadfile', methods=['POST'])
def download():
    #filename=request.form['myfile']
    print(request.form)
    print(request.files.get('myfile'))
    df = pd.read_csv(request.files.get('myfile'),encoding='utf-16',delimiter='\t')

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


if __name__ == '__main__':
    app.run(debug=True)   



    
   