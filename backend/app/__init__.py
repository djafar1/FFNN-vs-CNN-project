from flask import Flask
from .db import db, init_app
from .routes import blog_routes

app = init_app()
app.register_blueprint(blog_routes)
