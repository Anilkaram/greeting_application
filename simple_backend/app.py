from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/greet')
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'greeting': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
