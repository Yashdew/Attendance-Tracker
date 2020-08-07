from flask import Flask, render_template
from user.models import User
app = Flask(__name__)


### Routes
#from user import routes
@app.route('/users/signup', methods=['POST'])   ### rounding to this directory for GET data

def signup():
    return User().signup()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')