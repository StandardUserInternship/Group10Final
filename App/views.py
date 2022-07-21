
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
#It is using this here instead of in the __innit__.py!
def index():
    
    return render_template('index.html')

@app.route('/content')
def content():
    return render_template('content.html')






    

