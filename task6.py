from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods= ['POST'])
def square():
    data = request.get_json()
    number = data.get('number')

    result = number * number

    return jsonify({
    'number': number,
    'Square': result
})

if __name__ == "__main__":
    app.run(debug=True)

    
