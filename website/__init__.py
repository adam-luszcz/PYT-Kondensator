from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SECRET_KEY'] = 'Xo6h3HsJqPx40vkoBThH22hxy3u3jFDtm4UUHI39'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
