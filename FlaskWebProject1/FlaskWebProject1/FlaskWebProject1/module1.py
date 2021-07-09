from datetime import datetime
from flask import render_template , url_for
from FlaskWebProject1 import app
from flask import request
@app.route('/.hom')
def hom():
    return render_template('home.html') 
    

@app.route('/', methods =["GET", "POST"])
def maps():
    if request.method == "GET":
        MPIN = request.form.get("pininput")
        if MPIN == "1":
            
            return render_template("MMaps.html")
        elif MPIN == "2":
            return render_template("UMaps.html")
        else:
            return "Wrong Pincode"