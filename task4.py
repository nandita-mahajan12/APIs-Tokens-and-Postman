from flask import Flask, request, jsonify

app = Flask(__name__)
Token = "mysecrettoken123"

@app.route("/secure",methods=["GET"])
def secure():
    key = request.headers.get("Authorization")

    if key == f"Bearer {Token}":
        return jsonify({"send": "Access Granted"})
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True,port=5001)

