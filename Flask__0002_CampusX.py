from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "<h1>Welcome To The Home Page</h1>"

@app.route("/welcome/tony")
def welcome_tony():
    return "<h1>Welcome Tony On The Home Page</h1>a"


@app.route("/welcome/sonu")
def welcome_sonu():
    return "<h1>Welcome Sonu On The Home s</h1>"
 
# This is Dynamical URL
@app.route("/welcome/<name>")
def welcome_name(name):
    return f"<h1>Welcome {name} On The Home s</h1>"
 


if __name__=="__main__":
    app.run(debug=True)