from flask import Blueprint, jsonify
from .models import Blog
from .db import db

blog_routes = Blueprint('blog', __name__)

@blog_routes.route('/')
def list_blogs():
    #find query id 1
    blogs = Blog.query.filter(Blog.id.like(1))
    return jsonify([{'id': blog.id, 'title': blog.title} for blog in blogs])
