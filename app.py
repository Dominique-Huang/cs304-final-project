import MySQLdb
import bcrypt
import loft

from flask import (Flask, url_for, redirect, request, render_template, flash, session)

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
        valid = True
        
        if(email[-4:] != ".edu" or "@" not in email):
            flash("Please enter a valid school email")
            valid = False
        if(pw != pw2):
            flash("The passwords do not match")
            valid = False
        elif (len(pw) < 6 or any(char.isdigit() for char in pw) == False): #only checks when passwords match
            flash("Password is too weak, must be longer than 6 characters and contain a digit")
            valid = False
        
        curs = conn.cursor(MySQLdb.cursors.DictCursor)
        curs.execute('SELECT email FROM users WHERE email = %s', [email])
        row = curs.fetchone()
        if row is not None:
            flash('An account with that email already exists')
            valid = False
        
        if valid == True:
            hashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
            loft.createUser(conn, name, email, hashed, school)
            return redirect(url_for('login'))
        else:
            return render_template('account.html')
    else:
        return render_template('account.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['pw']
        conn = loft.getConn('loft')
        curs = conn.cursor(MySQLdb.cursors.DictCursor)
        curs.execute('SELECT pw FROM users WHERE email = %s',
                     [email])
        row = curs.fetchone()
        if row is None:
            # Same response as wrong password, so no information about what went wrong
            flash('login incorrect. Try again or join')
            return redirect( url_for('login'))
        hashed = row['pw']
        # strings always come out of the database as unicode objects
        if bcrypt.hashpw(passwd.encode('utf-8'),hashed.encode('utf-8')) == hashed:
            curs2 = conn.cursor(MySQLdb.cursors.DictCursor)
            curs2.execute('''select UID from users where email = %s''',
                        [email]) #emails are unique
            row2 = curs2.fetchone()
            UID = row2['UID']
            
            flash('successfully logged in with '+email)
            session['UID'] = UID
            #session['logged_in'] = True
            #session['visits'] = 1
            return redirect(url_for('showProperties'))
        else:
            flash('login incorrect. Try again or join')
            return redirect(url_for('login'))
    else:
        if 'UID' in session:
            flash('You are already logged in. Please first logout to log in again.')
            return redirect(url_for('showProperties'))
        return render_template('login.html')


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
        print((conn, name, descrip, loc, price, smoker, gender, pet))
        row = loft.createProperty(conn, name, descrip, loc, price, smoker, gender, pet)
        
        PID = row['last_insert_id()']
        
        #right now, each property only has 3 date ranges initially
        start1 = request.form.get('start1')
        end1 = request.form.get('end1')
        if start1 != '' and end1 != '':
            loft.createDate(conn, PID, start1, end1)
        
        start2 = request.form.get('start2')
        end2 = request.form.get('end2')
        if start2 != '' and end2 != '':
            loft.createDate(conn, PID, start2, end2)
        
        start3 = request.form.get('start3')
        end3 = request.form.get('end3')
        if start3 != '' and end3 != '':
            loft.createDate(conn, PID, start3, end3)

        UID = session['UID']
        loft.addHostProp(conn, UID, PID)
        
        return redirect(url_for('showProperties'))
    else:
        if 'UID' not in session:
            flash('You must be logged in to create a property')
            return redirect(url_for('login'))
        else:
            return render_template('addProp.html')

@app.route('/', methods = ["GET","POST"])
def showProperties():
    conn = loft.getConn('loft')
    if request.method == 'POST':
        gender = int(request.form.get('gender'))
        location = request.form.get('location')
        price = request.form.get('price') #might use price ranges in the future
        if price == "":
            price = 100000 #no upper limit
        start = request.form.get('start')
        end = request.form.get('end')
        print(start)
        print(end)
        propList = loft.searchProp(conn, gender, location, price, start, end)
    else: 
        propList = loft.getAll(conn) #shows all properties
    return render_template('index.html', propList = propList)

@app.route('/show/<id>', methods = ["POST", "GET"])
def showPage(id):
    conn = loft.getConn('loft')
    if request.method == 'POST':
        if 'UID' not in session:
            flash('You must be logged in to book')
            return redirect(request.referrer)
        
        UID = session['UID']
        prop = loft.getOne(conn, id)
        dates = loft.getDates(conn, id)

        start = request.form.get('start')
        end = request.form.get('end')
        loft.book(conn, UID, id, start, end)
        
        #ideally, this would redirect to my reservations
        return render_template('show.html', item = prop, dates = dates)
    else:
        prop = loft.getOne(conn, id)
        dates = loft.getDates(conn, id)
        return render_template('show.html', item = prop, dates = dates)

@app.route('/profile/<id>', methods = ["GET"])
def profilePage(id):
    conn = loft.getConn('loft')
    profile = loft.getProfile(conn, id)
    return render_template('profile.html', profile = profile)

@app.route('/edit/<id>', methods = ["GET", "POST"])
def edit(id):
    if request.method == 'GET':
        conn = loft.getConn('loft')
        prop = loft.getOne(conn, id)
        return render_template('edit.html', item = prop)
    else:
        conn = loft.getConn('loft')
        name = request.form.get('name')
        descrip = request.form.get('descrip')
        loc = request.form.get('location')
        price = request.form.get('price')
        smoker = request.form.get('smoker')
        gender = request.form.get('gender')
        pet = request.form.get('pet')
        loft.updateProperty(conn, id, name, descrip, loc, price, smoker, gender, pet)
        return redirect(url_for('showPage', id = id))
    
@app.route('/delete/<id>', methods = ["POST"])
def delete(id):
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8081)
