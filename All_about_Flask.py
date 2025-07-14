# --------------------------------------------------------------------------------------------------------------
# Import the Flask Libary
from flask import Flask

# Create the Object Of Flask
# Here Just call __name__ is Dounder Method
app = Flask(__name__) 

# Assign the Name of this application.
# To Create a Decorater
# This Forward slash "/" 'that means this is home page
@app.route("/") 
def home():
    return "<h1>Welcome To The Home Page(Flask__0001) </h1>"

# @app.route("/about")
# def about():
#     return "<h1>Welcome To The About Page </h1>"

# @app.route("/Home")
# def about():
    # return "<h1>Welcome To The home Page </h1>"

# @app.route("/Welcome/<name>")
# def name(name):
#     return f"<h2> Hi {name}, You're welcome to this page</h2>"

@app.route("/addition/<num>")
def addition(num):
    return f"<h1> Input is {num}, Output is {num+10}</h1>"

@app.route("/addition/int:<num1>/int:<num2>")
def addition1(num1,num2):
    return f"<h1> Input is {num1} ,{num2} , Output is {num1+num2}</h1>"


# There are variuse application to run the flask application 
# In python when you import module it will execute if we don't want executed the this app when any module is imported 
# __main__ refer current file only

# Below code explain we can cheack __name__ == Flask_0001_CampusX.py it will increase security.
if __name__ =="__main__":
    app.run(debug=True)

app.run(debug=True)


# --------------------------------------------------------------------------------------------------------------

import Flask__0001_CampusX

print(f"Running Mod 1 
({__name__})")

# --------------------------------------------------------------------------------------------------------------

import Flask__0001_Mod1
print(f"Running Mod 2 ({__name__})")

# --------------------------------------------------------------------------------------------------------------

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

# --------------------------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------------------------
#  When we Create a Template by using HTML that stored in one floder that floder name is "templates" Name is fixed.

# render_template : it will render the templates and show html web page

# Jinja about Layout

from flask import Flask,  render_template,url_for

from Flask__0003_DataSet_CampusX import employees_data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title = "Home")

@app.route("/place_holder")
def place_holder():
    return render_template("place_holder.html",title = " Place Holder ")

# Take User Input in URL for filling Place Holder
# @app.route("/about/<title1>")
# def about(title1):
#     return render_template("about.html",title = title1)



@app.route("/about")
def about():
    return render_template("about.html",title = "About")


@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",title = "Evaluate",number=num)

@app.route("/employees")
def employees():
    return render_template("employees.html",title = "Employees",employees = employees_data)

@app.route("/manager")
def managers():
    return render_template("manager.html",title = "Manager",employees = employees_data)

if __name__ == "__main__":
    app.run(debug=True)


# AssertionError: View function mapping is overwriting an existing endpoint function: home :: --> If multiple method/function having same name

# --------------------------------------------------------------------------------------------------------------

employees_data = {
    1:{
        "name":"Pravin" ,
        "age": 22,
        "Position": "Manager"     
       },
    2:{
        "name":"Dev" ,
        "age": 24,
        "Position":"manager"     
       },
    3:{
        "name":"Ajay" ,
        "age": 25,
        "Position":"Receptionist"     
       },
    4:{
        "name": "Josh",
        "age": 34,
        "Position":"Founder"     
       },
    5:{
        "name": "Joshi",
        "age": 34,
        "Position":"Co-Founder"     
       }
}

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
