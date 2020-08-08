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
  return render_template('check.html')  


    
   