import time

# redirect : To change the URL/Path Of Old wedsite to new website
# url_for : return URL which is pass inside the url_for
from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>Welcome To THe Home Page.</h1>"

@app.route("/pass")
def passed():
    return f"<h1> Congrat, You are Pass ! </h1>"


@app.route("/fail")
def failed():
    return f"<h1>Sorry, You are fail </h1>"


@app.route("/score/<name>/<int:num>")
def score(name,num):
    print(f"<h1>{name} </h1>")
    if num < 30:
        time.sleep(2)
        return redirect(url_for("passed"))
        # redirect user to page "fail"
        
    else:
        time.sleep(2)
        return redirect(url_for("failed"))
        # redirect user to page "fail"
        

if __name__ =="__main__":
    app.run(debug=True)