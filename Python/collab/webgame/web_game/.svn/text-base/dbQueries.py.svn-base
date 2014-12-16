#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys




class dbQueries:
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
      
    
    def listPlayers(self):
        self.cur.execute("SELECT ID, Name, Email, StartDate, Score from Players")
        data = self.cur.fetchall()
        for count in range(len(data)):
            print data[count]
            
    def listWhatsNearbyXY(self, x, y, distance):
        self.cur.execute("SELECT SystemID, XLocation, YLocation FROM SolarSystems WHERE ABS(SQRT(POW(SolarSystems.XLocation - %s, 2) + POW(SolarSystems.YLocation - %s,2))) < %s" % (x, y, distance))
        return self.cur.fetchall()
        
    def listWhatsNearbyShipGroup(self, playerID, shipGroupID, distance):
        self.cur.execute("SELECT SystemID from ShipGroups WHERE PlayerID like '%s' AND GroupID like '%s';" % (playerID, shipGroupID))
        systemID = self.cur.fetchone()
        
        self.cur.execute("SELECT XLocation, YLocation FROM SolarSystems WHERE SystemID LIKE '%s';" % systemID)
        systemXY = self.cur.fetchone()
        return self.listWhatsNearbyXY(systemXY[0], systemXY[1], distance)


if __name__ == '__main__':
    mygalaxy = dbQueries()
    print mygalaxy.testDBConnection()
    
    print "\nList of Users:"
    mygalaxy.listPlayers()
    
    print "\nItems within distance of 2 from coordinate 0,3:"
    items = mygalaxy.listWhatsNearbyXY(0,3,2)
    for count in range(len(items)):
        print items[count]
        
    print "\nItems within distance of 1.2 from ShipGroup 2 of player 1:"
    items = mygalaxy.listWhatsNearbyShipGroup(1, 2, 4.2)
    for count in range(len(items)):
        print items[count]
        
    print "\nAll done.\n\n"
    
    #mygalaxy.listPlayers()
    