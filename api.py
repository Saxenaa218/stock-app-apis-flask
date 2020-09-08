from flask import Flask, jsonify, request
from test import get_data
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-datasets', methods=['GET'])
def get_dataset():
    return jsonify({"datasets": os.listdir(f'{os.getcwd()}/files')})

@app.route('/get-data', methods=['POST'])
def post_tasks():
    name = request.json['name']
    return jsonify(get_data(name))

if __name__ == '__main__':
    app.run(debug=True)