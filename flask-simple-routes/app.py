from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'

@app.route("/hello/<name>")
def hello2(name):
    return f"<h1>Hello, {name}!</h1>"

