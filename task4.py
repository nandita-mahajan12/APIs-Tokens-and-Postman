from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

SECRET_TOKEN = "mysecrettoken123"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token missing"}), 401

        if token != f"Bearer {SECRET_TOKEN}":
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return decorated


@app.route('/secure-items', methods=['GET'])
@token_required
def secure_items():
    return jsonify({
        "message": "Access granted using Bearer Token"
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)
