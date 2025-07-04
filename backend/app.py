# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) to allow the frontend
# to make requests to this backend.
CORS(app)

@app.route('/api/greet', methods=['GET'])
def greet():
    """
    A simple API endpoint that returns a greeting.
    It takes a 'name' query parameter.
    Example: /api/greet?name=Alice
    """
    # Get the 'name' parameter from the query string. Default to 'World' if not provided.
    name = request.args.get('name', 'World')

    # Create the greeting message
    greeting_message = f"Hello, {name}! This message came from the backend."

    # Return the message as a JSON response
    return jsonify({"greeting": greeting_message})

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible from outside the container.
    # The default port is 5000.
    app.run(host='0.0.0.0', port=5000)
