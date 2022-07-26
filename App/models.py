from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import app, db
from flask import request

#...
#@app.route("/register", methods=("Get", "POST")) 
# def register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         db = get_db()
#         error = None

#         if not username:
#             error = "Username is required."
#         elif not password:
#             error = "Password is required."
#         if error is None:
#             try:
#                 db.execute(
#                     "INSERT INTO user (username, password) Values (?, ?)",
#                     (username, generate_password_hash(password)),
#                 )
#                 db.commit()
#             except db.IntegrityError:
#                 error = f"User {username} is already registered."
#             else:
#                 return redirect(url_for("auth.login"))
class User(UserMixin, db.Model):
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)