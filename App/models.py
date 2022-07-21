from flask_login import UserMixin
from app import login
from app import app


@app.user_loader
def load_user():
    return load_user.query.get(int())

