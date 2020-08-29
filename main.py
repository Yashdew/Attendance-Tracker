import pymongo
from werkzeug.security import generate_password_hash,check_password_hash

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")

mydb = myclient["Yashdb1"]
mycol = mydb["Yashdb1"]
password="bhai"
password1="bhai"
password = generate_password_hash(password)
#storedpassword="pbkdf2:sha256:150000$YI0uJO9I$91735684df0066aea02bb504cefee9fe1cff872fec79ab1a454b9061681e99b9"
record = {
            "Email": "yashdewangan123456@gmail.com",
            "Name":  'yash', 
            "Password":  password,
            "CPassword":  password,
            "SID": "0000",
}
mycol.insert_one(record)
for x in mycol.find():
    result = check_password_hash(x['Password'],password1)
print(result)
