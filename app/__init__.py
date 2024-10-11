"""
Application factory and initialization.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class or 'app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app.main import models  # Import models to register them
        db.create_all()

    from app.main.controllers import main_bp
    app.register_blueprint(main_bp)

    return app
