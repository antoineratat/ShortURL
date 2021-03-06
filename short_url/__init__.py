from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from short_url.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.test_request_context():
        from short_url.models import Links
        db.create_all()

    from short_url.urls.routes import urls
    from short_url.errors.handlers import errors
    app.register_blueprint(urls)
    app.register_blueprint(errors)

    return app
