import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://yashdew:5kAa9bRquer0cRtq@cluster0.c6ung.mongodb.net/yashdew?retryWrites=true&w=majority")
                                                    
mydb = myclient["Yashdb"]
mycol = mydb["Yashdb"]
var = "jgdjkAHKJ@gmail.com"
for x in mycol.find():
    if x['email']==var:
           print(x['_id'])
           print(x['name'])
           print(x['username'])
           print(x['email'])

            
            from flask_restful import Resource
import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class UploadCSV(Resource):

    def post(self):
        files = request.files['file']
        files.save(os.path.join(ROOT_PATH,files.filename))
        data = pd.read_csv(os.path.join(ROOT_PATH,files.filename))
        print(data)

api.add_resource(UploadCSV, '/v1/upload')

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)




    ########################################################################

    filename=request.form['myfile']

    filename.save(os.path.join(ROOT_PATH,filename.filename))

    print(request.form['myfile'])

    df = pd.read_csv(os.path.join(ROOT_PATH,filename.filename))

    data = df.to_dict('records')
    mycol1.insert_many(data)
    return render_template('download.html')


    """Period5":{
                                            "Dept":none,
                                            "Subject":none,
                                            "Div":none

                            },
                            "Period6":{
                                            "Dept":none,
                                            "Subject":none,
                                            "Div":none

                            },
                            "Period7":{
                                            "Dept":none,
                                            "Subject":none,
                                            "Div":none

                            },
                            "Period8":{
                                            "Dept":none,
                                            "Subject":none,
                                            "Div":none

                            },
                            "Period9":{
                                            "Dept":none,
                                            "Subject":none,
                                            "Div":none

                            },
                            "Period10":{
                                            "Dept":none,
                                            "Subject":none,
                                            "Div":none

                            }"""