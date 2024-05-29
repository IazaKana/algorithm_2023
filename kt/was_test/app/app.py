# 1. routing code

from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contents')
def contents():
    return render_template('contents.html')

app.run(debug=True)
