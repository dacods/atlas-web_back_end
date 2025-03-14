#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, jsonify, request, abort, make_response
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
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """
    POST /sessions route for user login.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, "Missing email or password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(jsonify({"email": email,
                                      "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
