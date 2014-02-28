from flask import Flask, url_for

def configure_jinja(app):
    @app.context_processor
    def inject_static():
        return dict(STATIC_URL=url_for('static', filename=''))

app = Flask(__name__)
configure_jinja(app)
from app import views