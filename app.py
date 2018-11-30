import loft

from flask import (Flask, url_for, request, render_template, flash)

app = Flask(__name__)

app.secret_key = "Mb.Jp2u/6XT/)b`."

@app.route('/start/', methods = ['POST', 'GET'])
# For first time users to create an account
# Would need to create an extra section for tenants
def addUser():
    if request.method == 'POST':
        conn = loft.getConn('loft')
        name = request.form.get('name')
        email = request.form.get('email')
        school = request.form.get('school')
        pw = request.form.get('pw')
        pw2 = request.form.get('pw_confirm')
        
        # print(any(char.isdigit() for char in pw))
        # valid = True
        if(len(name) < 4):
            flash("Name must be at least 4 characters long")
            valid = False
        if(email[-4:] != ".edu" or "@" not in email):
            flash("Please enter a valid school email")
            valid = False
        if(pw != pw2):
            flash("The passwords do not match")
            valid = False
        elif (len(pw) < 6 or any(char.isdigit() for char in pw) == False): #only checks when passwords match
            flash("Password is too weak, must be longer than 6 characters and contain a digit")
            valid = False
        
        # print valid
        if valid == True:
            loft.createUser(conn, name, email, school, pw)
        return render_template('account.html')
    else:
        return render_template('account.html')

@app.route('/add-property/', methods = ["GET","POST"])
# For first time users to create an account
def addProperty():
    if request.method == 'POST':
        conn = loft.getConn('loft')
        name = request.form.get('name')
        descrip = request.form.get('descrip')
        loc = request.form.get('location')
        price = request.form.get('price')
        smoker = request.form.get('smoker')
        gender = request.form.get('gender')
        pet = request.form.get('pet')
        
        loft.createProperty(conn, name, descrip, loc, price, smoker, gender, pet)
        
        PID = loft.getLastProperty(conn)['PID']
        start = request.form.get('start_date') #as of now, assuming there is only one time period
        end = request.form.get('end_Date')
        
        loft.createDate(conn, PID, start, end)
    else:
        return

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

@app.route('/home/', methods = ["GET"])
def homePage():
    conn = loft.getConn('properties')
    propList = loft.getAll(conn)
    return render_template('index.html', propList = propList)

@app.route('/show/<id>', methods = ["GET"])
def showPage(PID):
    conn = loft.getConn('properties')
    prop = loft.getOne(conn, PID)
    return render_template('index.html', item = prop)

@app.route('/edit/<id>', methods = ["GET", "POST"])
def editPage():
    return render_template('show.html')

@app.route('/profile/', methods = ["GET"])
def profilePage():
    return render_template('profile.html')

@app.route('/delete/<id>', methods = ["DELETE"])
def deletePage():
    return render_template('show.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8081)
