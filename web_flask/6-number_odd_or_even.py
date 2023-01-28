#!/usr/bin/python3
''' a script that runs a flask application '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    new_text = 'C ' + text.replace('_', ' ')
    return new_text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text=''):
    if text:
        new_text = 'Python ' + text.replace('_', ' ')
        return new_text
    else:
        return 'Python is cool'


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    new_text = '{:d} is a number'.format(n)
    return new_text


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template_route(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_template(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
