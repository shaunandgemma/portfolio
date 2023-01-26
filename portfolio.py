from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def file_to_databasetxt(data):
    with open("database.txt", mode="a") as databasetxt:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = databasetxt.write(f"\n{name}: {email}: {message}")

def file_to_databasecsv(data):
    with open('database.csv', newline='', mode='a') as databasecsv:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(databasecsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            file_to_databasetxt(data)
            file_to_databasecsv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to databese"
    else:
        return "something went wrong, try again!"

