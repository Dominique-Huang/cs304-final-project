import loft

from flask import (Flask, url_for, request, render_template, flash)

app = Flask(__name__)

app.secret_key = "Mb.Jp2u/6XT/)b`."

@app.route('/login/', methods = ["POST"])
def login():
    conn = loft.getConn('loft')
    name = request.form.get('name')
    email = request.form.get('email')
    school = request.form.get('school')
    pw = request.form.get('pw')
    pw2 = request.form.get('pw2')

    valid = True
    if(name.length < 4):
        flash("Name must be at least 4 characters long")
        valid = False
    if(email[-4:] != ".edu" and "@" not in email):
        flash("Please enter a valid school email")
        valid = False
    if(pw != pw2):
        flash("The pas")
    loft.createUser(conn, name, email, school, pw)
    return render_template('login.html')

@app.route('/properties/', methods = ["GET","POST"])
def showProperties():
    conn = loft.getConn('loft')
    if request.method == 'POST':
        gender = request.form.get('gender')
        location = request.form.get('location')
        price = request.form.get('price')
        lofts = loft.searchProp(conn, gender,location,price)
    else: 
        lofts = loft.searchProp(conn, 3, "", 100000) #shows all properties
    return render_template('', lofts = lofts)
    
@app.route('/add-property/', methods = ["POST"])
def addProperty():
    conn = loft.getConn('loft')
    name = request.form.get('name')
    loc = request.form.get('location')
    price = request.form.get('price')
    smoker = request.form.get('smoker')
    gender = request.form.get('gender')
    pet = request.form.get('pet')
    
    loft.createProperty(conn, name, loc, price, smoker, gender, pet)

@app.route('/home/', methods = ["GET"])
def homePage():
    return render_template('index.html')

@app.route('/show/<id>', methods = ["GET"])
def showPage():
    return render_template('show.html')

@app.route('/edit/<id>', methods = ["GET", "POST"])
def editPage():
    return render_template('show.html')

@app.route('/profile/', methods = ["GET"])
def profilePage():
    return render_template('profile.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8081)
