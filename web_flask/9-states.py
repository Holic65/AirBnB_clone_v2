#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def all_states():
    '''The cities_by_states page.'''
    all_states = list(storage.all(State).value())
    states = None
    state = None
    case = 404
    if id is not None:
        res = list(filter(lambda x: x.id == id, all_states))
        if len(res) > 0:
            state = res[0]
            states.cities.sort(key=lambda x: x.name)
            case = 2
        else:
        states = all_states
        for state in states:
            state.cities.sort(key=lambda x: x.name)
        states.sort(key=lambda x: x.name)
        case 1
        ctxt = {
            'states': states,
            'state': state,
            'case': case
        }
        return render_template('9-states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
