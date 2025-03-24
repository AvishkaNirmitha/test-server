from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask server!"

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello from Flask API!"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
