#!/usr/bin/python3
"""
<<<<<<< HEAD
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
=======
A simple flask server running on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Prints html document with a list of states"""
    states = storage.all(State).values()
>>>>>>> d364182adf6b6aebc07fd37d00692d0bd7608f44
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
def remove_current_session(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> d364182adf6b6aebc07fd37d00692d0bd7608f44
