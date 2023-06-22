from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Topic, Thread, Post, User

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    topics = Topic.query.all()
    return render_template('home.html', user=current_user, topics=topics)


@views.route('/topic/<int:topic_id>')
@login_required
def topic_view(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    threads = Thread.query.filter_by(topic_id=topic_id).all()
    thread_list = []
    for thread in threads:
        user = User.query.get(thread.user_id)
        thread_dict = {
            'id': thread.id,
            'title': thread.title,
            'author_email': user.email,
            'created_at': thread.date
        }
        thread_list.append(thread_dict)
    return render_template('topic.html', user=current_user, threads=thread_list)


@views.route('/thread/<int:thread_id>')
@login_required
def thread_view(thread_id):
    thread = Thread.query.get_or_404(thread_id)
    posts = Post.query.filter_by(thread_id=thread_id).all()
    post_list = []
    for post in posts:
        user = User.query.get(post.user_id)
        post_dict = {
            'id': post.id,
            'content': post.content,
            'author_email': user.email,
            'created_at': post.date
        }
        post_list.append(post_dict)
    return render_template('thread.html', user=current_user, posts=post_list)
