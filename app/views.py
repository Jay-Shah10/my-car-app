from app import app
from flask import render_template
from flask import redirect


@app.route('/')
def carlist():
    return render_template('index.html')

@app.route('/mainapp')
def mainapp():
   try:
       return redirect('http://192.168.50.92:5003', code=302)
   except Exception as e:
       e