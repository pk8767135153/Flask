import time

from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>Welcome To THe Home Page.</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Name is {sname} and mark is {marks} Congrat, You are Pass ! </h1>"


@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Name is {sname} and mark is {marks} Sorry, You are Fail ! </h1>"


@app.route("/score/<name>/<int:num>")
def score(name,num):
    print(f"<h1>{name} </h1>")
    if num < 30:
        time.sleep(2)
        return redirect(url_for("passed",sname = name,marks=num))
        # redirect user to page "fail"
        
    else:
        time.sleep(2)
        return redirect(url_for("failed",sname = name,marks=num))
        # redirect user to page "fail"
        

if __name__ =="__main__":
    app.run(debug=True)

# url_for()