from flask import Flask, jsonify, render_template
from flask import app

app=Flask(__name__)
@app.route("/")
def index():
    print("index() was called")
    return render_template("index.html")
@app.route("/titanicGraph")
def test():
    return render_template("titanicGraph.html", title="Titanic Graph")

@app.route('/test2')
def test2():
    x = {'1': 'Zach'}
    return jsonify(x)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

#title="Home", user=user