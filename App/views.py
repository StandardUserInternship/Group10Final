
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

@app.route('/htmlTesting')
def htmlTesting():
    return render_template('htmlTesting.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/titanicGraph')
def titanicGraph():
    return render_template("titanicGraph.html")

@app.route('/monthGraph')
def monthGraph():
    return render_template("monthGraph.html")


    

