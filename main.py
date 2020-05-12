from flask import Flask, render_template, request, redirect
import requests
from app import app

app = Flask(__name__)

@app.route('/')
def red():
    return redirect('/index')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        ingr = request.form['sostojki']
        if not ingr:
            return render_template('index.html', ingredients = "")
        url = 'http://www.recipepuppy.com/api/?i={sostojki}'.format(sostojki = ingr)
        try:
            response = requests.get(url)
            response = response.json()
        except Exception:
            return render_template('index.html', notfound = "Couldn't find any recepie")
    return render_template('index.html', ingredients = response['results'])

if __name__ == "__name__":
    app.run()
