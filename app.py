import loft
import bcrypt
import MySQLdb

from flask import (Flask, url_for, redirect, request, render_template, flash, session)
from werkzeug import secure_filename

import sys, os, random
import imghdr



app = Flask(__name__)

app.secret_key = "Mb.Jp2u/6XT/)b`."

app.config['UPLOADS'] = 'uploads'


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
        
        # print valid
        if valid == True:
            hashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
            curs = conn.cursor(MySQLdb.cursors.DictCursor)
            curs.execute('SELECT email FROM users WHERE email = %s', [email])
            row = curs.fetchone()
            if row is not None:
                flash('An account with that email already exists')
                return redirect(url_for('addUser'))
            loft.createUser(conn, name, email, hashed, school)
            return redirect(url_for('showProperties'))
        else:
            user = {
                "name": name,
                "email": email, 
                "school": school,
                "pw": pw,
                "pw2": pw2
            }
            return render_template('account.html', user = user)
    else:
        return render_template('account.html')

     
#@app.route('/login/', methods=["POST"])
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
            flash('successfully logged in with '+email)
            #session['username'] = username
            #session['logged_in'] = True
            #session['visits'] = 1
            return redirect(url_for('showProperties'))
        else:
            flash('login incorrect. Try again or join')
            return redirect( url_for('login'))
    else:
        return render_template('login.html')


@app.route('/add-property/', methods = ["GET","POST"])
# For first time users to create an account
def addProperty():
    if request.method == 'POST':
        if 'UID' not in session:
            flash('You must be logged in to book')
            return redirect(request.referrer)
        
        conn = loft.getConn('loft')

        UID = session['UID']

        name = request.form.get('name')
        descrip = request.form.get('descrip')
        loc = request.form.get('location')
        price = request.form.get('price')
        smoker = request.form.get('smoker')
        gender = request.form.get('gender')
        pet = request.form.get('pet')

        
        try:
            f = request.files['pic'] #update front-end to ask for pic
            print(f)
            mime_type = imghdr.what(f.stream)
            print mime_type.lower()
            if mime_type.lower() not in ['jpeg','gif','png']:
                raise Exception('Not a JPEG, GIF or PNG: {}'.format(mime_type))
            filename = secure_filename('{}.{}'.format(UID,mime_type))
            print("filename: ", filename)
            pathname = os.path.join(app.config['UPLOADS'],filename)
            print("pathname: ", pathname)
            f.save(pathname)
            flash('Upload successful')
            
        except Exception as err:
            flash('Upload failed {why}'.format(why=err))
            print('Upload failed {why}'.format(why=err))
            return render_template('addProp.html')
        
        print((conn, name, descrip, loc, price, smoker, gender, pet, filename))

        row = loft.createProperty(conn, name, descrip, loc, price, smoker, gender, pet, filename)

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


        
        # PID = loft.getLastProperty(conn)['PID']
        # start = request.form.get('start_date') #as of now, assuming there is only one time period
        # end = request.form.get('end_Date')
        
        # loft.createDate(conn, PID, start, end)

        
        return redirect(url_for('showProperties'))
    else:
        return render_template('addProp.html')

@app.route('/', methods = ["GET","POST"])
def showProperties():
    conn = loft.getConn('loft')
    if request.method == 'POST':
        gender = int(request.form.get('gender'))
        location = request.form.get('location')
        price = request.form.get('price') #might use price ranges in the future
        # THIS DOESN'T REALLY MAKE SENSE
        # if price == "":
        #     price = 100000 #no upper limit
        propList = loft.searchProp(conn, gender, location, price)
    else: 
        propList = loft.getAll(conn) #shows all properties
    return render_template('index.html', propList = propList)

@app.route('/show/<id>', methods = ["GET"])
def showPage(id):
    #conn = loft.getConn('properties')
    conn = loft.getConn('loft')
    prop = loft.getOne(conn, id)
    print ("TESTING: ", prop)
    #return render_template('index.html', item = prop)
    return render_template('show.html', item = prop)

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
    
@app.route('/delete/<id>', methods = ['GET', 'DELETE'])
def delete(id):
    conn = loft.getConn('loft')
    loft.deleteProp(conn, id)
    return redirect(url_for('showProperties'))
   
 
@app.route('/logout/')
def logout():
    try:
        if 'UID' in session:
            UID = session['UID']
            session.pop('UID')
            #session.pop('logged_in')
            flash('You are logged out')
            return redirect(url_for('login'))
        else:
            flash('you are not logged in. Please login or join')
            return redirect( url_for('login') )
    except Exception as err:
        flash('some kind of error '+str(err))
        return redirect( url_for('index') )

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8081)
