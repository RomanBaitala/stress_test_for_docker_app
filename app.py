from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = Flask(__name__)
TARGET_URL = os.environ.get('target-url')

@app.route('/request/<int:num_requests>', methods=['GET'])
def test_back(num_requests):
    for _ in range(num_requests):
        requests.get(TARGET_URL)
    return jsonify({'message': f'Successfully sent {num_requests} requests to endpoint GOAL.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
