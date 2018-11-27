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

def createUser(conn, name, email, school, pw):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into `users` values (%s, %s, &s, %s)''', 
                (name, email, school, pw,))
    return curs.fetchone()

if __name__ == '__main__':
    conn = getConn('loft')