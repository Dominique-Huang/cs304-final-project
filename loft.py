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

#--Adding to Database-- 
def createUser(conn, name, email, pw, university):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into users values (%s, %s, %s, %s, NULL)''',
                (name, email, pw, university,))
    return curs.fetchone()
    
def createProperty(conn, name, descrip, loc, price, smoker, gender, pet, picfile):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into properties values (%s, %s, %s, %s, %s, %s, %s, %s, NULL)''', 
                (name, descrip, loc, price, smoker, gender, pet, picfile))
    curs.execute('''select last_insert_id() from properties''')
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

def addRenterProp(conn, UID, PID, start, end):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''insert into renter_prop values (%s, %s, %s, %s)''',
                (UID, PID, start, end))
    return curs.fetchone()

# Searching properties based on specific filters
def searchProp(conn, gender, location, price, start, end):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    location = "%" + location + "%"
    if (gender == 3): #no preference
        PID_list = curs.execute('''select * from (properties inner join dates
                        on dates.PID = properties.PID)
                        where propLocation like %s and propPrice < %s
                        and startDate <= %s and endDate >= %s 
                        group by properties.PID''',
                    (location, price, start, end))
    else:
        curs.execute('''select * from (properties inner join dates
                        on dates.PID = properties.PID)
                        where propGender = %s and propLocation like %s and propPrice < %s
                        and startDate <= %s and endDate >= %s 
                        group by properties.PID''',
                    (gender, location, price, start, end))
    return curs.fetchall()

#updating table values
def updateUser(conn, UID, name, email, pw, university):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''update users set name = %s, email = %s, pw = %s, university = %s where UID = %s''', 
                (name, email, pw, university, UID))
    return curs.fetchone
def updateProperty(conn, PID, name, descrip, loc, price, smoker, gender, pet):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''update properties 
                        set 
                            propName = %s, 
                            propDescription = %s, 
                            propDescription = %s, 
                            propPrice = %s, 
                            propSmoker = %s, 
                            propGender = %s, 
                            propPet = %s 
                        where 
                            PID = %s''', 
                (name, descrip, loc, price, smoker, gender, pet, PID))
    return curs.fetchone()

def deleteDate(conn, PID, start):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''delete from dates where PID = %s and startDate = %s''',
                (PID, start)) #assuming no two date ranges start at the same time
    return curs.fetchone()

def book(conn, UID, PID, start, end):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    addRenterProp(conn, UID, PID, start, end)
    deleteDate(conn, PID, start)
    curs.execute('''select * from renter_prop where UID = %s''', [UID])
    return curs.fetchall()

def getAll(conn):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from properties''')
    return curs.fetchall()

def getOne(conn, id):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from properties where PID = %s''', [id])
    return curs.fetchone()
    
def getProfile(conn, id):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from users where UID = %s''', [id])
    return curs.fetchone()
    
def deleteProp(conn, id):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''delete from properties where PID = %s''', [id])
    return 

def getDates(conn, id):
    '''retrieves all available dates for this property'''
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from dates where PID = %s''', [id])
    return curs.fetchall()

def getHostProps(conn, UID):
    '''retrieves all the host's properties'''
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from (host_prop inner join properties 
                on host_prop.PID = properties.PID)
                where host_prop.UID = %s''', [UID])
    return curs.fetchall()

def getRenterProps(conn, UID):
    '''retrieves all the renter's properties'''
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select * from (renter_prop inner join properties 
                on renter_prop.PID = properties.PID)
                where renter_prop.UID = %s''', [UID])
    return curs.fetchall()
    
if __name__ == '__main__':
    conn = getConn('loft')
    # createDate(conn, 2, '2018-01-01', '2018-06-01')
    print(searchProp(conn,3,'',100000, '2019-12-31','2020-05-01'))
    print(searchProp(conn,3,'',100000, '3000-12-31', '1000-01-01'))
    print(searchProp(conn,2,'',100000, '3000-12-31','1000-01-01'))
    # user = createUser(conn, 'Ally', 'ally@tufts.edu', 'Password123', 'Tufts University')
    # prop = createProperty(conn, 'House', 'A House in Boston', 'Boston', 800, 0, 1, 0)
    # print prop
    # print(searchProp(conn,3,'Cambridge',10000))
