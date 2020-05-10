from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from ..models import Post
from ..app import db

import datetime

module = Blueprint('post',__name__)

@module.route('/editor')
@login_required
def editor():
    return render_template('post_manager.html')

@module.route('/editor', methods=["POST"])
@login_required
def editor_post():
    title = request.form.get('title')
    body = request.form.get('body')
    preview = request.form.get('preview')
    created = datetime.datetime.now()
    username = current_user.username
    email = current_user.email
    inputFile = request.files['inputFile']
    image = secure_filename(str(datetime.datetime.now()))+inputFile.filename

    new_post = Post(title = title, body =  body, preview = preview, created = created, username = username, email = email, image = image)
    db.session.add(new_post)
    db.session.commit()
    inputFile.save('src/static/images/'+image)

    return redirect(url_for('post.post',id = new_post.id))

@module.route('/post/<id>')
@login_required
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html',post = post)