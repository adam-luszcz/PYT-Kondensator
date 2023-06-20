from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Xo6h3HsJqPx40vkoBThH22hxy3u3jFDtm4UUHI39'

    return app
