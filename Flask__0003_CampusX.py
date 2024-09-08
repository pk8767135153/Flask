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