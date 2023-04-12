from flask import Flask, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)

@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config['APP_NAME']}"


@app.route("/")
def index():
    posts = mongo.db.posts.find()
    content_url = url_for("read_content", title="Novidades de 2023")
    return (
        f"<h1>{app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Novidades de 2023</a>"
        "<hr>"
        f"{list(posts)}"
    )

@app.route("/<title>")
def read_content(title):
    index_url = url_for("index")
    return f"<h1>title</h1> <a href='{index_url}'>Voltar</a>"
