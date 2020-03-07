import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
def home():
    return "This site is for demo purposes, API for Nyskopun 2020"


@app.route('/api/v1/resources/products/all', methods=['GET'])
def api_all():
    return jsonify(device)

app.run()