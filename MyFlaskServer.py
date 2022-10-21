from flask import Flask,redirect,url_for,render_template

app= Flask(__name__)#create instance of flask

@app.route("/")
def main():
    #return render_template("home.html") #using html mthod to display page

    return "Main Page"# main page or index page >>>  http://127.0.0.1:5000 <<<

    """here you can put content for main page
    you can use flask function (or) html file  to use html file make in project dir new folder calld {{templates}}
    and >>> import form flask render_template >>> and >>> call the render_template("your_file.html")
    in your app.route() function
    """

@app.route('/hello')# hello page >>> http://127.0.0.1:5000\hello <
def hello_name():
    return "hello.world!"
    """ here you can put content to the page"""





if __name__== "__main__":
    app.run()