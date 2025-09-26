from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevSecOps Pipeline Demo",
        "version": "1.0.0",
        "environment": os.getenv("ENV", "development")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/users/<user_id>')
def get_user(user_id):
    # Intentional vulnerability for DAST testing (will fix later)
    return jsonify({
        "id": user_id,
        "name": f"User {user_id}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)