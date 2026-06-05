# Simple Flask app — proves your container is running
from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "healthy",
        "message": "Fargate lab is running!",
        "hostname": socket.gethostname(),
        "env": os.environ.get("APP_ENV", "dev")
    })

@app.route('/health')
def health():
    # ALB will call this endpoint to check if the task is healthy
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
