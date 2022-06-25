from app import app, db
from flask import request

from app.data import User

@app.route('/user')
def get_users():
    return "working"

@app.route('/user', methods=["put"])
def create_user():
    email = request.args.get("email")
    new = User(email)
    db.session.add(new)
    db.session.commit()
    return "User created."
