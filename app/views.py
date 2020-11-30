from app import app
from flask import render_template


@app.route('/carlist')
def carlist():
    return "Add in url for the car list"