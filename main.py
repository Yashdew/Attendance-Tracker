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

database = request.form
        new_ID = database['ID'] 
        new_name = database['Name'] 
        new_Username =  database['Username'] 
        new_email =  database['Email']  
        new_password = database['Password']  
    else:
        print(3)
        database = request.form
        """new_ID = database['ID'] 
        new_name = database['Name'] 
        new_Username =  database['Username'] 
        new_email =  database['Email']  
        new_password = database['Password']"""
         
    
    """mydict = { "_id": new_ID,
    "name": new_name, 
    "username": new_Username,
    "email": new_email,
    "password": new_password
    }"""
    """print(database['ID'])
    mycol.insert_one({ "_id": new_ID,
    "name": new_name, 
    "username": new_Username,
    "email": new_email,
    "password": new_password
    })"""




    """ if request.method == 'POST':
        print("3")
        record = {
            "_id": request.form['ID'],
            "name":  request.form['Name'], 
            "username": request.form['Username'],
            "email":  request.form['Email'],
            "password":  request.form['Password']

        }
    else:
        print("3")
        record = {
            "_id": request.form['ID'],
            "name":  request.form['Name'], 
            "username": request.form['Username'],
            "email":  request.form['Email'],
            "password":  request.form['Password']

        }

    mycol.insert_one(record)
    
    return render_template('index.html')"""