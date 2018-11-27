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
    
if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8081)
    