from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy

def configure_jinja(app):
    @app.context_processor
    def inject_static():
        return dict(STATIC_URL=url_for('static', filename=''))

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
configure_jinja(app)

from app import views, models