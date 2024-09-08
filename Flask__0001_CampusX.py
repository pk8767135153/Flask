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