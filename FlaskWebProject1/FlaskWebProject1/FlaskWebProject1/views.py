
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template , url_for
from FlaskWebProject1 import app
from flask import request

@app.route('/')

@app.route('/home')

def home():
    """Renders the home page."""
   
    return render_template(
        'Hack1.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/.hom')
def hom():
    return render_template('home.html') 

@app.route('/maps', methods =["GET", "POST"])
def maps():
    if request.method == "POST":
        MPIN = request.form.get("pininput")
        if MPIN == "1":
            return render_template("MMaps.html")
        elif MPIN == "2":
            return render_template("UMaps.html")
        else:
            return "Wrong Pincode"

#@app.route('/contact')
#def contact():
    """Renders the contact page."""
  #  return render_template(
 #       'contact.html',
     #   title='Contactesu',
   #     year=datetime.now().year,
   #     message='Your contact page.'
  #  )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/gfg', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        Username1 = request.form.get("Uname")
        Pass1 = request.form.get("pass1")
        if Username1 == "Shadwal":
            return "DOne"
        else:
            return "Try Again"



