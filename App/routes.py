from flask import render_template


from app import app




@app.route('/')
@app.route('/index')


def index():
    user={'username': 'python'}
    return render_template('index.html, title="Home', user=user)
    






# from app.forms import LoginForm




















    
