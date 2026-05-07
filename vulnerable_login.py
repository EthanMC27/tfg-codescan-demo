"""Fichero con vulnerabilidades intencionadas para testear el pipeline.

Este fichero se añade en una PR al repo de prueba para que el workflow
de n8n detecte las vulnerabilidades y comente en la PR.
"""
from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

def get_db():
    return sqlite3.connect("app.db")

# VULNERABILIDAD 1: SQL Injection (CWE-089)
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    db = get_db()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = db.execute(query)
    user = cursor.fetchone()
    if user:
        return jsonify({"status": "ok", "user": user[1]})
    return jsonify({"error": "Invalid credentials"}), 401

# VULNERABILIDAD 2: Hardcoded credentials (CWE-798)
ADMIN_PASSWORD = "admin123"
API_SECRET_KEY = "sk-1234567890abcdef"

# VULNERABILIDAD 3: Weak hashing (CWE-328)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABILIDAD 4: Command injection (CWE-078)
import os
@app.route("/ping", methods=["POST"])
def ping():
    host = request.form.get("host")
    result = os.popen(f"ping -c 1 {host}").read()
    return jsonify({"result": result})
