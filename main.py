import pymongo

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")

mydb = myclient["Yashdb1"]
mycol = mydb["Yashdb1"]

for x in mycol.find():
    if x['Email']=='kul@gmail.com' and x['Password']=='bhaibhai':
        record=x
        y=record['_id']
        print(record['_id'])
        """newrecord = {
                    "$set",{
                        "Email":request.form['NEmail'],
                        "Name":request.form['MName'],
                        "Password":request.form['NPassword'],
                        "CPassword":request.form['NPassword'],
                        "Period1":{
                            "Dept":request.form['Department'],
                            "Year":request.form['Year'],
                            "Subject":request.form['Subject'],
                            "Div":request.form['Div'],
                            
                        }
                    }
        }"""
        newrecord={"$set":{"Email":'kul@gmail.com',"Name":"bhaibhai","Password":"bhaibhai","CPassword":"bhaibhai","Period1":{
                            "Dept":"IT",
                            "Year":"FE",
                            "Subject":"DBMS",
                            "Div":"Div2",
                            
                        }}}
                
mycol.update_many({"_id":record['_id']},newrecord)
            