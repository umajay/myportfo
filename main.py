import csv

from flask import Flask, render_template, request, redirect,copy_current_request_context

app = Flask(__name__)
print(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello,World UMA!"


@app.route('/')
def about():
    return render_template("index.html")


# @app.route('/HappyHomeMaker')
# def happy_homemaker():
#     return render_template("HappyHomeMaker.html")

@app.route('/<string:page_name>')
def happy_homemaker(page_name):
    return render_template(page_name)

#
# @app.route('/PythonDeveloper')
# def python_developer():
#     return render_template("PythonDeveloper.html")
#
#
# @app.route('/Yoga')
# def yoga():
#     return render_template("Yoga.html")
#
#
# @app.route('/Education')
# def my_education():
#     return render_template("Education.html")
#
#
# @app.route('/WorkExperience')
# def work_experience():
#     return render_template("WorkExperience.html")
#
#
# @app.route('/CoursesandCertification')
# def my_courses():
#     return render_template("CoursesandCertification.html")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        writ_to_csv(data)
        return redirect("/#contact")
    else:
        return "something went wrong, please try again"


def writ_to_text(data):
    with open("C:\\Users\\Uma\\PycharmProjects\\SampleWebServer\\database.txt", mode="a") as database:
        name = data["name"]
        email = data["email"]
        comment = data["comment"]
        file = database.write("{}, {} ,{}\n".format(name, email, comment))


def writ_to_csv(data):
    with open("database2.csv", newline="",  mode="a") as database2:
        name = data["name"]
        email = data["email"]
        comment = data["comment"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,comment])
