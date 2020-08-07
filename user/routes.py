from flask import Flask
from app import app          ### importing app function from app.py
from user.models import User ### calling User Class from user/model.py dir

@app.route('/users/signup', methods=['POST'])   ### rounding to this directory for GET data

def signup():
    
    return User().signup()
