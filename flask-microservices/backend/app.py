from flask import Flask, jsonify, request, abort
import os

app = Flask(__name__)

SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")

@app.route('/api/message')
def get_message():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {SECRET_TOKEN}":
        abort(401)
    return jsonify({"message": "Hello from the backend microservice!!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)