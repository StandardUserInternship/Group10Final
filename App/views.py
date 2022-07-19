from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app



# app = Flask(__name__)
# change to name of your database; add path if necessary
db_name = 'sockmarket.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'squlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
# the varaibl, db will be used for all SQLALchemy commands
db=SQLAlchemy(app)

@app.route('/')
def testdb():


    try:


        db.session.query(text('1')).from_statement(text('SELECT 1')).all
    except Exception as e:

        error_text= "<p>The error:<br>" + str(e) + "</p>"
        hed= '<h1>Something is broken.</h1>'
        return hed + error_text
if __name__ == "__main__":
    app.run(debug=True)

