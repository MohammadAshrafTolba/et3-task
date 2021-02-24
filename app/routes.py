"""
This file is responsible for routing requests to the appropriate handlers
"""

from .init_app import app


@app.route('/')
def route_placeholder():
    return 'app initialized!'