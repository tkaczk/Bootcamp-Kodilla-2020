from flask import Flask
from flask import request, redirect
from flask import render_template


app = Flask(__name__)

@app.route('/hello')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'
@app.route('/blog', methods=['GET'])
def blog_main():
    return f'This is the main blog page.'
@app.route('/blog/<id>')
def blog(id):
    return f'This is blog entry #{id}.'
@app.route('/message', methods = ['GET', 'POST'])
def message():
    if request.method == 'GET':
        print('We received GET')
        return render_template("form.html")
    elif request.method == 'POST':
        print('We received POST')
        print(request.form)
        return redirect("/")
@app.route('/greetings')
def greetings():
    if request.method == 'GET':
        return render_template('greetings.html')
@app.route('/warehouse')
def warehouse():
    items = ['screwdriver', 'saw', 'hammer']
    error = 'Hammer is broken'    
    return render_template('warehouse.html', items = items, error = error)