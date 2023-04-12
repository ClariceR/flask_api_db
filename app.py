from flask import Flask, jsonify
from db_utils import get_all_records

app = Flask(__name__)


@app.route('/')
def welcome():
    return {'message': 'Welcome to the wishlist app'}


@app.route('/items')
def get_items():
    items_data = get_all_records()
    items = {}
    for item in items_data:
        items[item[1]] = item[2]
    return items


@app.route('/items/<int:id>')
def get_item_by_id(id):
    items = get_all_records()
    for item in items:
        if item[0] == id:
            return item[1]


if __name__ == '__main__':
    app.run(debug=True)