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
        
        print(any(char.isdigit() for char in pw))
        valid = True
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
        return render_template('login.html')
    else:
        return render_template('login.html')
=======
def getConn(db):
    conn =  MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='',
                           db=db)
    conn.autocommit(True)
    return conn

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
>>>>>>> 2a65f14c4289da38ef6afe71810de179f25902e3

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
# For first time users to create an account
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
    conn = getConn('properties')
    propList = helper.getAll(conn)
    return render_template('index.html', propList = propList)

@app.route('/show/<id>', methods = ["GET"])
def showPage(id):
    conn = getConn('properties')
    prop = helper.getOne(conn, id)
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
