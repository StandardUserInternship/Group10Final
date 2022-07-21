
#from app import app
from flask import app, Flask, render_template
from app import app


app=Flask(__name__)
@app.route('/')
def index():
    return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)