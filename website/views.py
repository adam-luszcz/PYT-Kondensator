from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Topic, Thread

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    topics = Topic.query.all()
    return render_template('home.html', user=current_user, topics=topics)


@views.route('/topic/<int:topic_id>')
@login_required
def topic_view(topic_id):
    threads = Thread.query.filter_by(topic_id=topic_id).all()
    return render_template('topic.html', user=current_user, threads=threads)
