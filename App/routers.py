from market import app
from flask_login import current_user, login_required, login_user, render_template,forms, redirect,url_for,LoginForm,flash
from app.models import User





@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

from flask_login import logout_user

@app.route('/')
@app.route('/logout')

def logout():
    logout_user()
    return redirect (url_for('index'))