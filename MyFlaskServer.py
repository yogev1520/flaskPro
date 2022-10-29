from flask import Flask,redirect,url_for,render_template,request

app= Flask(__name__)#create instance of flask
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

""" video-src = https://www.youtube.com/watch?v=0meTbQQaosU """
@app.route("/result",methods = ["POST","GET"])
def result():
    output =request.form.to_dict()
    name =output['name']
    return render_template("result.html", name = name)





if __name__== "__main__":
    app.run(debug=True,port = 5000)