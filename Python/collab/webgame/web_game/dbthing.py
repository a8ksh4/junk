#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class dbthing:
    def __init__(self, dbserver='localhost', login='root', passwd='R1ven', dbname='Web_game'):
        self.con = None
        try:
            self.con = mdb.connect(dbserver, login, passwd, dbname)
            self.cur = self.con.cursor()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
            
    def testDBConnection(self):
        self.cur.execute("SELECT VERSION()")
        data = self.cur.fetchone()
        return "Database version : %s " % data
    
    def getString(self):
        pass
    
    def getInt(self):
        pass
    
    def getFloat(self):
        pass
    
    def set(self):
        pass
    
    def setNew(self):
    
    
if __name__ == '__main__':
    mygalaxy = dbthing()
    print mygalaxy.testDBConnection()
