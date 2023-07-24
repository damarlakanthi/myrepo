from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient
import sqlalchemy

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['lab07']
collection = db['userdetails']
@app.route("/")
def hello_world():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submitsignup",methods = ['POST'])
def submitsignup():
    first = request.form['firstName']
    last = request.form['lastName']
    email = request.form['email']
    password = request.form['password']

    email_exist = collection.find_one({"email": email})
    if(email_exist):
        return render_template('signup.html',error='email is already exists...')
    collection.insert_one({'firstName': first,'lastName':last,'email': email, 'password': password})

    return render_template('thankyou.html')

@app.route("/loginsubmission", methods=['POST'])
def loginsubmission():

    email = request.form['email']
    password = request.form['password']
    loginTrue  = collection.find_one({"email": email,"password":password})

    if(loginTrue):
        return render_template('secret.html')
    return render_template('login.html',error='Wrong Details....!!!')
    




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)