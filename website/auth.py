from flask import Blueprint, render_template
from website.forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Form successfully submitted!'
    return render_template('login.html', form=form)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        return 'Form successfully submitted!'
    return render_template('signup.html', form=form)
