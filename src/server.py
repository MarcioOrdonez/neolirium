import os

from flask import Flask
from flask import request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

from .model.user import User
from .model.post import Post

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,'..', "neolirium.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "<h1>asdasdasdasds</h1>"

@app.route("/login", methods=["POST"])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_user} successfully created!")



if __name__ == '__main__':
    app.run(debug=True, port=3000)
