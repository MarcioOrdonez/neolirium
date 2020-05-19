from flask import Blueprint, render_template 
from flask_login import login_required, current_user
from ..models import Post
from base64 import b64encode

module = Blueprint('main',__name__)

@module.route('/')
def index():
    post = Post.query.all()
    return render_template('home.html',posts = post)



@module.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)