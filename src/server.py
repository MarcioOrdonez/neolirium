import os
import sqlite3

from flask import Flask
from flask import request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template
from datetime import datetime as dt

#from src.model import user,post
#import src.model.user as User
#import src.model.post as Post

project_dir = os.path.dirname(os.path.abspath(__file__))
#database_file = "sqlite:///{}".format(os.path.join(project_dir,'..', "neolirium.db"))
database_file = "sqlite:///../neolirium.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
login_manager = LoginManager()

@app.route("/", methods=["GET"])
def home():
    post_list = post.Post.query.all()
    return render_template("home.html", posts=post_list)

@app.route("/post", methods=["GET", "POST"])
def create_post():
    title = request.values['title']
    body = request.values['body']
    if title and body:
        new_post = post.Post(title=title,
                             body=body,
                             created=dt.now())
        db.session.add(new_post)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return "foi"

@app.route("/account", methods=["GET", "POST"])
def create_user():
    """Create a user."""
    username = request.values['username']
    email = request.values['email']
    if username and email:
        new_user = user.User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_user} successfully created!")

@app.route("/users", methods=['GET',"POST"])
def get_users():
    print(user.User.query.all())
    return 'oi'





if __name__ == '__main__':
    from src.model import user, post
    db.create_all()
    app.run(debug=True, port=3000)
