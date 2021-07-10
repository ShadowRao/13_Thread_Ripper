
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template , url_for
from FlaskWebProject1 import app
from flask import request
global RealEmail
@app.route('/')

@app.route('/home')

def home():
    """Renders the home page."""
   
    return render_template(
        'INDEX.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/LoginButton' , methods=['GET', 'POST'])
def LoginButton():
    return render_template('Hack1.html')

@app.route('/RegisterButton' , methods=['GET', 'POST'])
def RegisterButton():
    return render_template('DONOR1.html')

@app.route('/donorreg')
def donoreg():
    "background-image: url('/static/img/maps.jpg')"
    return render_template('DONOR1.html')

@app.route('/Appointment')
def Appointment():
    return render_template('calender.html')
@app.route('/Calender')
def Calender():
    if request.method == "POST":
        return "Apppointment Succesfully booked"

@app.route('/BloodStat')
def BloodStat():
    return render_template('BloodStat.html')

@app.route('/Search')
def Search():
    return render_template('home.html')



@app.route('/donorform')
def donorform():
    return render_template('donor1.html')


    
@app.route('/donosubmit', methods=['GET', 'POST'])
def donosubmit():
    donosubmit.RealEmail = request.form.get("InputEmail")
    donosubmit.RealPass = request.form.get("InputPass")
    return render_template('Hack1.html')

@app.route('/.hom')
def hom():
    return render_template('home.html') 


@app.route('/maps', methods =["GET", "POST"])
def maps():
    if request.method == "POST":
        MPIN = request.form.get("pininput")
        if MPIN == "575001":
            return render_template("MMaps.html")
        elif MPIN == "576101":
            return render_template("UMaps.html")
        else:
            return "Wrong Pincode"




@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST":
        Username1 = request.form.get("Uname")
        Pass1 = request.form.get("pass1")
        if Username1 == donosubmit.RealEmail and Pass1 == donosubmit.RealPass:
            return render_template('INDEX2.html')
        else:
            render_template('Wronglogin.html')



