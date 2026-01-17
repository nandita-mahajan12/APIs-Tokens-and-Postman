from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    items[index] = request.json
    return jsonify(items[index])

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    deleted = items.pop(index)
    return jsonify(deleted)

if __name__ == "__main__":
    app.run(debug=True,port=5001)