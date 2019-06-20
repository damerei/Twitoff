"""
Entry point for twitoff Flask application
"""
#!/usr/bin/env python3

from .app import create_app

APP = create_app()
