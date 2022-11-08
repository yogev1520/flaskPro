from flask import Flask,redirect,url_for,render_template,request
import json
from flask_sqlalchemy import SQLAlchemy,model,session
from datetime import datetime
#pip install -U Flask-SQLAlchemy
#https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation
#https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#define-models

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


""" create server or app Flask"""

base_link = "http://127.0.0.1:5000"
@app.route("/")
@app.route("/home")
def main():

    return render_template("result.html") #using html mthod to display page

    #return "Main Page"# main page or index page >>>  http://127.0.0.1:5000 <<<

    """here you can put content for main page
    you can use flask function (or) html file  to use html file make in project dir new folder calld {{templates}}
    and >>> import form flask render_template >>> and >>> call the render_template("your_file.html")
    in your app.route() function
    """

@app.route('/login')
def login():
    return render_template("Login.html")

@app.route("/sign_up")
def sign_up():
    return render_template("signUp.html")

@app.route('/hello')# hello page >>> http://127.0.0.1:5000\hello <
def hello_name():
    return "hello.world!"
    """ here you can put content to the page"""



""" for thet return page i add request from flask lib 
and add method post and get 

on the html i use {% if name %}
btw you heve to close the if statment with {% andif %}

<h2> create heder with hello {{name}},how are you ?  </h2>
{% if name %}

<h3 style="color: chocolate;">hello {{name}}, how are you ? </h3>

{% endif %}
and render name in render_templets to return it 
"""

"""
video sorce 
video-src = https://www.youtube.com/watch?v=0meTbQQaosU
video_src using data-base=https://www.youtube.com/watch?v=Z1RJmh_OqeA
"""
@app.route("/result",methods = ["POST","GET"])
def result():

    output =request.form.to_dict()#get the form from the html and extract list of valuse
    name =output['name']#the name of the input id
    password = output['password']#the name of the input id
    email=output['email']#the name of the input id

    #open file name storg.txt and save content from name,email,password input_fiald in html file
    
    mystorg= open("storg.txt",'a')#append to file
    mystorg.write ("{name=" +"," + name + "," + "}" )#write to file
    mystorg.write( "{email="+"," + email + ","+ "email}" )
    mystorg.write("{password="+"," + password + "," + "password}")
    mystorg.write("{id="+","+"="+","+"id}")
    
    mystorg.close()

    """send data to json
    "name" : name = key : value
    "email" : email = key : value
    "password":password = key : value
    """
    #object to send to json file 
    toStorg ={
    "name":name
    ,"email":email
    ,"password":password}
 
    #Character  Meaning
    #'r' = open for reading (default)
    #'w' = open for writing, truncating the file first
    #'x' = open for exclusive creation, failing if the file already exists
    #'a' = open for writing, appending to the end of file if it exists
    #'b' = binary mode
    #'t' = text mode (default)
    #'+' open for updating (reading and writing)
    file_location ="templates\storg.json"#the location or path to the file 
    with open(file_location,"a")as file:#open the file(storg.json) as file
        FileTell =file.tell()
        file.seek(FileTell)
        json.dump(toStorg,file)
        file.close()
    
    """ DataBase """
   
    
    
    return render_template("result.html", name = name,email=email,password=password)#render the values here !!! 


if __name__== "__main__":
    app.run(debug=True,port = 5000)