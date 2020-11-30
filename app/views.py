from app import app
from flask import render_template


@app.route('/carlist')
def carlist():
    return render_template('index.html')