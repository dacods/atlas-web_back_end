#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)


AUTH = Auth()


@app.route("/", methods=['GET'])
def home() -> str:
    """
    GET route for the root URL, returns a JSON response
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    """
    POST /users route for registering a new user.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400
    
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
