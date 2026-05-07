"""Simple Flask API — base segura para el repo de prueba."""
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("app.db")

@app.route("/users/<int:user_id>")
def get_user(user_id):
    db = get_db()
    cursor = db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify({"id": user[0], "name": user[1]})
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=False)
