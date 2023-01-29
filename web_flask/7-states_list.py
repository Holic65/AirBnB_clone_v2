#!/usr/bin/python3
''' a script that starts a web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    states = sorted(list(storage.all('States').values()), key=lambda x: x.name)
    render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def app_teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
