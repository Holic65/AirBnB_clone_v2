#!/usr/bin/python3
''' a script thats sets up a flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_cities():
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('8-cities_by_states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
