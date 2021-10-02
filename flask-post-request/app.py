# This is a simple Flask app using the post method

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    word = request.form.get('text')
    # return f'New word added: {word}'
    return render_template('register.html', word=word)

    
