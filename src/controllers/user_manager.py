from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import User
from ..app import db

module = Blueprint('user_manager',__name__)

@module.route('/manage')
@login_required
def manager():
    users = User.query.all()
    return render_template('user_manager.html', users = users)

@module.route('/manage', methods=["POST"])
@login_required
def user_manager():
    id = request.form.get('id')
    user = User.query.get(id)
    if request.form.get('editor') == 'True':
        user.admin = True
    else:
        user.admin = False
    # db.session.add()
    db.session.commit()

    return redirect(url_for('user_manager.manager'))


