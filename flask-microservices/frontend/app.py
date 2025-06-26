from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)

SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")

@app.route('/')
def index():
    headers = {"Authorization": f"Bearer {SECRET_TOKEN}"}
    resp = requests.get('http://backend:5001/api/message', headers=headers)
    data = resp.json()
    return render_template_string("""
        <h1>Frontend Microservice</h1>
        <p>Message du backend : {{ msg }}</p>
    """, msg=data['message'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)