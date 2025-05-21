from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate-token', methods=['POST'])
def validate_token():
    token = request.json.get('token')
    if token == "valid-token":
        return jsonify({"status": "valid"}), 200
    return jsonify({"status": "invalid"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
