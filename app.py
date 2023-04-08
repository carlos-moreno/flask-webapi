from flask import Flask, url_for, request

app = Flask(__name__)

app.config["APP_NAME"] = "Meu Blog"

@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config['APP_NAME']}"

# app.register_error_handler(404, not_found_page)

@app.route("/")
def index():
    content_url = url_for("read_content", title="Novidades de 2023")
    return (
        f"<h1>{app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Novidades de 2023</a>"
        "<hr>"
        f"{dir(request)}"
    )

@app.route("/<title>")
def read_content(title):
    index_url = url_for("index")
    return f"<h1>title</h1> <a href='{index_url}'>Voltar</a>"

# app.add_url_rule("/<title>", view_func=read_content)
