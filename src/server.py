import os

from flask import Flask
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,'..', "neolirium.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "<h1>asdasdasdasds</h1>"

@app.route("/post", methods=["POST"])
def post():
    if request.values:
        print(request.values['title'])
    return request.values['title']



if __name__ == '__main__':
    app.run(debug=True, port=3000)
