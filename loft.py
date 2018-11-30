#!/usr/bin/python2.7

import sys
import MySQLdb

def getConn(db):
    conn =  MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='',
                           db=db)
    conn.autocommit(True)
    return conn

#def createUser(conn, name, email, school, pw):
#    curs = conn.cursor(MySQLdb.cursors.DictCursor)
#    curs.execute('''insert into `users` values (%s, %s, &s, %s)''', 
#                (name, email, school, pw,))
#    return curs.fetchone()

#--Adding to Database-- 
def createUser(conn, name, email, pw, university):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into users values (%s, %s, %s, %s, NULL)''',
                (name, email, pw, university,))
    return curs.fetchone()
    
def createProperty(conn, name, loc, price, smoker, gender, pet):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into properties values (%s, %s, %s, &s, %s, %s, %s, NULL)''', 
                (name, loc, price, smoker, gender, pet,))
    return curs.fetchone()

def createDate(conn, PID, start, end):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into dates values (%s, %s, %s)''',
                (PID, start, end,))
    return curs.fetchone()

def addTenantFeature(conn, UID, feature):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into featuresTenants values (%s, %s)''',
                (UID, feature,))
    return curs.fetchone()

def addPropertyFeature(conn, PID, feature):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into featuresProperties values (%s, %s)''',
                (PID, feature,))
    return curs.fetchone()
    
def addHostProp(conn, UID, PID):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into host_prop values (%s, %s)''',
                (UID, PID,))
    return curs.fetchone()

# Searching properties based on specific filters
def searchProp(conn, gender, location, price):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    if(gender == 3): #no preference
        gender = "1, 2, 3"
    location = "%" + location + "%"
    curs.execute('''select * from properties where gender in (%s) and location like %s and price < %s''',
                (gender, location, price))
    return curs.fetchall()

def getAll(conn):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from properties''')
    return curs.fetchall()

def getOne(conn):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    cure.execute('''select * from properties where PID = %s''', (id))
    return curs.fetchone()

if __name__ == '__main__':
    conn = getConn('loft')
    user = createUser(conn, 'Ally', 'ally@tufts.edu', 'Password123', 'Tufts University')