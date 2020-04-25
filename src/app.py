import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///../neolirium.db"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


from .models import User
from .models import Post

db.create_all(app=app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .controllers import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .controllers import main as main_blueprint
app.register_blueprint(main_blueprint)

from .controllers import post as post_blueprint
app.register_blueprint(post_blueprint)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port='3000')
