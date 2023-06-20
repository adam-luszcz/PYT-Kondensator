from flask import Blueprint, render_template, request, redirect, flash
from website.forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')
            return redirect('/')
        elif form.errors:
            for message in form.errors.values():
                flash(message[0], category='error')
    return render_template('login.html', form=form)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')
            return redirect('/')
        elif form.errors:
            for message in form.errors.values():
                flash(message[0], category='error')
    return render_template('signup.html', form=form)
