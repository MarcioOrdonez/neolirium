from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from ..models import Post
from ..models import User
from ..app import db
from .email_handler import email_handler

import datetime

module = Blueprint('post',__name__)

@module.route('/creator')
@login_required
def creator():
    return render_template('post_manager.html')

@module.route('/creator', methods=["POST"])
@login_required
def creator_post():
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
    user_list = User.query.all()
    email_sender = email_handler(user_list,new_post)
    email_sender.send()

    return redirect(url_for('post.post',id = new_post.id))

@module.route('/post/<id>')
@login_required
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html',post = post)


@module.route('/editor/<id>')
@login_required
def editor(id):
    if current_user.admin:
        post = Post.query.filter_by(id=id).first()
        return render_template('post_editor.html',post = post)

@module.route('/editor/<id>', methods=["POST"])
@login_required
def editor_post(id):
    if current_user.admin:
        post = Post.query.filter_by(id=id).first()
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        post.preview = request.form.get('preview')
        db.session.commit()
        inputFile = request.files['inputFile']
        inputFile.save('src/static/images/'+post.image)

        return redirect(url_for('post.post',id = post.id))
@module.route('/delete', methods=["POST"])
@login_required
def delete_post(id):
    if current_user.admin:
        id = request.form.get('id')
        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('main.index'))