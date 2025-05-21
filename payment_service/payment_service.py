from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    token = request.headers.get('Authorization')
    response = requests.post('http://auth-service/validate-token', json={'token': token})
    
    if response.status_code == 200:
        return jsonify({"status": "payment processed"}), 200
    return jsonify({"status": "unauthorized"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
