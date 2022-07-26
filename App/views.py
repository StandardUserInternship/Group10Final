import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show
from flask import render_template, jsonify
from app import app
import base64
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

@app.route('/testing')
def testing():
    return render_template("testing.html")

@app.route('/test2')
def test2():
    plot(1)  
    show(block=False)
    df = pd.read_csv("titanic.csv")
    df = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]
    cor = df.corr()
    sns.heatmap(cor, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
    plt.savefig('heatmap.png')

    data = {}
    with open('heatmap.png', mode='rb') as file:
        img = file.read()
    data['img'] = base64.encodebytes(img).decode()
    
    return jsonify(data['img'])

    

