from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({
        "message": "Data received successfully",
        "data": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
