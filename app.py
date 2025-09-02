from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Mock data storage (replace with MySQL later)
users = []
rotations = []
notes = []

@app.route('/api/health')
def health_check():
    return jsonify({"status": "OK", "message": "MedRotate backend is running"})

@app.route('/api/test')
def test_endpoint():
    return jsonify({"message": "Backend connection successful!"})

# Rotations endpoints
@app.route('/api/rotations', methods=['GET'])
def get_rotations():
    return jsonify(rotations)

@app.route('/api/rotations', methods=['POST'])
def create_rotation():
    new_rotation = request.get_json()
    rotations.append(new_rotation)
    return jsonify(new_rotation), 201

# Notes endpoints
@app.route('/api/notes', methods=['GET'])
def get_notes():
    rotation_id = request.args.get('rotation_id')
    if rotation_id:
        rotation_notes = [note for note in notes if note['rotation_id'] == rotation_id]
        return jsonify(rotation_notes)
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def create_note():
    new_note = request.get_json()
    notes.append(new_note)
    return jsonify(new_note), 201

# User endpoints (basic implementation)
@app.route('/api/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    users.append(user_data)
    return jsonify({"message": "User registered successfully", "user": user_data}), 201

@app.route('/api/login', methods=['POST'])
def login_user():
    login_data = request.get_json()
    # Simple authentication (replace with proper auth later)
    user = next((u for u in users if u['email'] == login_data['email']), None)
    if user:
        return jsonify({"message": "Login successful", "user": user})
    return jsonify({"error": "Invalid credentials"}), 401

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)