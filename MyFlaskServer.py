from flask import Flask,redirect,url_for

app= Flask(__name__)#create instance of flask

@app.route("/")
def main():
    return "Index Page"# main page or index page >>>  http://127.0.0.1:5000 <<<
    """here you can put content for main page """

@app.route('/hello')# hello page >>> http://127.0.0.1:5000\hello <
def hello_name():
    return "hello.world!"
    """ here you can put content to the page"""