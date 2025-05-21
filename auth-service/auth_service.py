from flask import Flask, request, jsonify
import jwt
import datetime

from jaeger_client import Config
from flask_opentracing import FlaskTracing

# Setup Jaeger Tracer
def init_tracer(service_name='auth-service'):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
            'reporter_batch_size': 1
        },
        service_name=service_name,
        validate=True
    )
    return config.initialize_tracer()

app = Flask(__name__)

# Attach tracer to Flask
tracer = init_tracer(service_name='auth-service')
tracing = FlaskTracing(tracer, True, app)

SECRET_KEY = 'mysecretkey'

@app.route('/get-token', methods=['POST'])
def get_token():
    username = request.json.get('username')
    if username:
        token = jwt.encode(
            {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({"token": token}), 200
    return jsonify({"error": "Username required"}), 400

@app.route('/validate-token', methods=['POST'])
def validate_token():
    token = request.json.get('token')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"status": "valid"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "invalid"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
