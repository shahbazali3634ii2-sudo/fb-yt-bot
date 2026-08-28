#!/usr/bin/env python3
"""
Auto Code AI - Flask REST API Server
"""

from flask import Flask, jsonify, request
from functools import wraps
import datetime
import hashlib
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

# In-memory store
_store = {}

def require_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 415
        return f(*args, **kwargs)
    return wrapper

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "version": "1.0.0"
    })

@app.route("/items", methods=["GET"])
def list_items():
    return jsonify({"items": list(_store.values()), "count": len(_store)})

@app.route("/items", methods=["POST"])
@require_json
def create_item():
    data = request.get_json()
    item_id = hashlib.md5(str(data).encode()).hexdigest()[:8]
    _store[item_id] = {**data, "id": item_id, "created_at": datetime.datetime.utcnow().isoformat()}
    return jsonify(_store[item_id]), 201

@app.route("/items/<item_id>", methods=["GET"])
def get_item(item_id):
    item = _store.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
