from flask import Flask
from flask import render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/warehouse2')
def warehouse():
    items = ['screwdriver', 'saw', 'hammer']

    return render_template('warehouse2.html', items = items)
