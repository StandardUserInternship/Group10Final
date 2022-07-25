from flask import Flask

# from flask import Loginform
#from flask_login import LoginManager,login_required,render_template
from app import app


app= Flask(__name__)




app.config.from_object('config')






# @app.route('/')
# @app.route('/index')
# @login_required
# def index():
    
#     return render_template("index.html")


# app = Flask(__name__)
# login=LoginManager(app)
# login.login_view='login'





# app= Flask(__name__ )
from app import routes



if  __name__ =="__main__":
    app.run(debug=True)