from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def home():
    return render_template('login.html')
