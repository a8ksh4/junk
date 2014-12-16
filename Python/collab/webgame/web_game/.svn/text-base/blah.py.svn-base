#!/usr/bin/python

import MySQLdb as mdb

#dbserver='localhost', login='root', passwd='R1ven', dbname='Web_game'):
if __name__ == "__main__":
    print 'test\n'
    con = None
        
    try:
        con = mdb.connect("localhost", "root", "R1ven", "Web_game")
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()
        print "Database version : $s " % data
    except mdb.Error, e:
        print "Error $d: $s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()

    
