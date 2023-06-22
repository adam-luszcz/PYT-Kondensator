from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Topic, Thread, Post

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


@views.route('/thread/<int:thread_id>')
@login_required
def thread_view(thread_id):
    posts = Post.query.filter_by(thread_id=thread_id).all()
    return render_template('thread.html', user=current_user, posts=posts)
