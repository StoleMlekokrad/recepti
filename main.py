from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def red():
    return redirect('/index')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingr = request.form['sostojki']
        #print(ingr)
        if not ingr:
            return render_template('index.html', ingredients = "", notfound = "EMPTY")
        url = 'http://www.recipepuppy.com/api/?i={sostojki}'.format(sostojki = ingr)
        try:
            response = requests.get(url)
            response = response.json()
        except Exception:
            return render_template('index.html', notfound = "Couldn't find any recepie")
        return render_template('index.html', sostojki = response["results"])
    return render_template('index.html', sostojki = "", notfound = "HELLO1")

if __name__ == "__name__":
    app.run()
