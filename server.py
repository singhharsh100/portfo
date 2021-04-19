from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def homepage(page_name):
    return render_template(page_name)

def database(data):
    with open('database.csv', mode="a", newline="") as databasee:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        csv_writer = csv.writer(databasee, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        database(data)
        return redirect('thankyou.html')
    else:
        return "Something went wrong!!"

