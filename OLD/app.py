import flask
from flask import request, jsonify
import os

app = flask.Flask(__name__)

# Load configuration from environment, with defaults
app.config['DEBUG'] = True if os.getenv('DEBUG') == 'True' else False
app.config['LISTEN_HOST'] = os.getenv('LISTEN_HOST', '0.0.0.0')
app.config['LISTEN_PORT'] = int(os.getenv('LISTEN_PORT', '5000'))
app.config['APP_URL'] = os.getenv('APP_URL', 'http://localhost:5000')  # must be https to avoid browser issues
app.config['APP_CLIENT_ID'] = os.getenv('APP_CLIENT_ID')
app.config['APP_CLIENT_SECRET'] = os.getenv('APP_CLIENT_SECRET')
app.config['SESSION_SECRET'] = os.getenv('SESSION_SECRET', os.urandom(64))


# Setup secure cookie secret
app.secret_key = app.config['SESSION_SECRET']


device = [
    {
        'id': 0,
        'pid': 1234,
        'product_name':'rotor1',
        'product_handbook': 'somebook',
        'product_items': 'item1, item 2',
        'product_maintenance_schedule': 'item1 - mondays at 08:00'
    },
    {
        'id': 1,
        'pid': 4321,
        'product_name':'rotor2',
        'product_handbook': 'somebook',
        'product_items': 'item1, item 2',
        'product_maintenance_schedule': 'item1 - mondays at 08:00'
    },       
]

@app.route('/', methods=['GET'])
def index():
    return "<p>This site is for demo purposes, API for Nyskopun 2020</p><br><a href='/api/v1/resources/products/all'>api link</a>"


@app.route('/api/v1/resources/products/all', methods=['GET'])
def api_all():
    return jsonify(device)

if __name__ == "__main__":
    app.run(app.config['LISTEN_HOST'], app.config['LISTEN_PORT'])
