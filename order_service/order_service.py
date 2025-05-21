from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/create-order', methods=['POST'])
def create_order():
    token = request.headers.get('Authorization')
    response = requests.post('http://payment-service/process-payment', headers={'Authorization': token})
    
    if response.status_code == 200:
        return jsonify({"status": "order created"}), 200
    return jsonify({"status": "payment failed"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
