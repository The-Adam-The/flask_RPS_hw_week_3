from flask import render_template
from app import app



@app.route('/test')
def index():
    return "Hello World"


