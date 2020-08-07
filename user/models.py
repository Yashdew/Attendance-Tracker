from flask import Flask, jsonify 

class User:                          ### Creating a Signup feature
    def signup(self):

        user = {
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }                           ### getting these information

        return jsonify(user), 200   ### returing in JSON Format
