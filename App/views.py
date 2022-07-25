from flask import app
from flask import render_template#, redirect, url_for 
from forms import LoginForm
#from flask_login import logout_user


@app.route('/')
@app.route('/index')
# @app.route("/content")
# @app.route("/login")
def index():
    user = {'username' : ''}    
    return render_template('index.html', title='Home', user=user)
 
@app.route("/content")
def content():
    content = content()
    # if content.validate_on_submit():
    #     return redirect(url_for("content"))
    return render_template("content.html", title="Content", content=content)

@app.route("/login")#, methods=["GET", "POST"])
def login():

    form = LoginForm()
    return render_template("Login.html", title="Sign In", form=form)
@app.route("titanicGraph")
def test():
    return render_template("titanicGraph.html", title="Titanic Graph")

# @app.route("/logout")
# def logout():
#     form = LogoutForm()
#     return render_template("index.html", title="Sign Out", form=form)




    

