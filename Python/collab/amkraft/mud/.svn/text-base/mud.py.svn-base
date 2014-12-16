#!/usr/bin/env python
import sys
import sqlite3

chatindex = 0

def list():
    global c
    print "list:"
    c.execute("select msg from comm;")
    for row in c:
        print row[0]

def getnewchat():
    global chatindex
    global c
    c.execute("select id, msg from comm where id > %d;" % chatindex)
    
    while True:
        o = c.fetchone()
        if(o == None):
            break
        sys.stdout.write('"%s"\n' % o[1])
        chatindex = o[0]

def userloop():
    global c, conn
    while True:
        try:
            userin = None
            userin = raw_input("$ ")
        except EOFError:
            sys.stdout.write("\n")
            break
        except KeyboardInterrupt:
            sys.stdout.write("\n")
            break
        
        if userin == "quit":
            break
        elif userin == "list":
            list()
        elif userin != "":
            t = (userin,)
            c.execute("""insert into comm values
                (NULL, ?)""", t)
            conn.commit()
        getnewchat()
        
def dbopen():
    global conn, c
    conn = sqlite3.connect('mud.db')
    c = conn.cursor()
    
    c.execute('''create table IF NOT EXISTS comm
        ( id INTEGER PRIMARY KEY,
        msg TEXT )''')
    
def dbclose():
    global c
    c.close()

def main():
    dbopen()
    getnewchat()
    userloop()
    dbclose()

main()
