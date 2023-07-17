from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient;
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['pwdchecker']
collection = db['pwdcollection']
# global count
# count =0


@app.route("/")
def hello_world():
    return render_template("base.html")

@app.route("/password")
def password():
    return render_template("index.html")


# def counterCall():
    
#     count=count+1
#     print(count)
#     if count >= 3:
#         return render_template('report.html',counter='You have entered 3 times a wrong password')

@app.route("/validations", methods = ['POST'] )
def validations():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        uc=0
        lc=0
        num=0
        char=0
        if len(password) >= 8 :
            char=1
        for x in password:
            
            if(x.isupper()):
                uc=1
               
            if(x.islower()):
                lc=1
                
        
        if(password[len(password)-1].isnumeric()):
            num=1
        
            
        if(lc==1 and uc==1 and num==1 and char==1):
            collection.insert_one({'username': username, 'password': password})
            return render_template('report.html',success='your password passed all three requirements....!!!!')
            
        if(lc==1 and uc==1 and num==1 and char!=1):
            
            return render_template('report.html',charerror='There should be one upper case....')
        if(lc==1 and uc==1 and num!=1 and char!=1):
            
            return render_template('report.html',charerror='There should be one upper case....',numerror='Password should end with a number....!!!')
        if(lc!=1 and uc!=1 and num==1 and char==1):
            
            return render_template('report.html',lowerror='There should have atleast  one lower case....',uperror='Password should have atleast one Uppercase....!!!')
        if(uc!=1):
            
            return render_template('report.html',uperror='There should be one upper case....')
        if(num!=1):
            
            return render_template('report.html',lowerror='There should be one number....')
        if(char!=1):
            
            return render_template('report.html',charerror='length should be 8 characters....')
        
        return render_template('report.html',success='your password passed all three requirements....!!!!')
if __name__ == '__main__':
    app.run(host='0.0.0.0')