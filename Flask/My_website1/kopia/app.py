from flask import Flask
from flask import render_template, request, redirect


app = Flask(__name__)

@app.route("/me")
def me():
    return render_template("me.html")


@app.route("/contact", methods = ["GET", "POST"])
def contact():
    contact_info = ['e-mail: tkaczk@yahoo.co.uk', 'Tel. +48 123 456 789']
    if request.method == 'GET':
        print('We have a get!')
        return render_template("contact.html", contact_info = contact_info)
    elif request.method == 'POST':
        print(request.form)
        return redirect("/me")
