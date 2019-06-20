""" Main Application and Routing Logic for Twitoff"""
#!/usr/bin/env python3

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User


def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)
    app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'debug'
    
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    
    return app



