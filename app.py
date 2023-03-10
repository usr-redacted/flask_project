import flask
from infrastructure.view_modifiers import response

app = flask.Flask(__name__)


@app.route("/")
@response(template_file="index.html")
def index():
    return {"msg": "Hello world; what did you expect?"}


@app.route("/about")
@response(template_file="about.html")
def about():
    return {}


if __name__ == "__main__":
    app.run(debug=True)
