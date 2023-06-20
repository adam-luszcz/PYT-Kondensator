from flask import Blueprint, render_template
from website.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Form successfully submitted!'
    return render_template('login.html', form=form)
