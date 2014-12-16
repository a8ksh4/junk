#!/usr/bin/python
# -*- coding: utf-8 -*-

#Note! So far, this is code to initialize a fresh DB to muck with.
#I'm usig a DB called "dantest".
#Assumes Grid from -1000 to +1000 in x and y directions. 

import MySQLdb

class Galaxy:
    def __init__(self, dbserver='localhost', login='root', passwd='R1ven', dbname='dantest'):
        self.con = MySQLdb.connect(dbserver, login, passwd, dbname)
        self.cur = self.con.cursor()
    
    def createNewTables(self):
        self.cur.execute("""
        
        CREATE TABLE data (
            entity VARCHAR NOT NULL,
            attribute VARCHAR NOT NULL,
            value LONGTEXT,
            PRIMARY KEY (entity, attribute));
        
        DROP TABLES Players, PlanetTypes, SolarSystems, SystemPlanets, ShipGroups;
        
        CREATE TABLE Players (
            ID INT(10) PRIMARY KEY NOT NULL, 
            Name VARCHAR(12) NOT NULL, 
            Email VARCHAR(50) NOT NULL,
            PasswdHash VARCHAR(50) NOT NULL, 
            StartDate DATE NOT NULL, 
            Score INT(5));
            
        CREATE TABLE PlanetTypes (
            PTypeID INT(5) PRIMARY KEY NOT NULL,
            Name VARCHAR(12) NOT NULL,
            MineralCount INT(5) NOT NULL,
            WaterCount INT(5) NOT NULL,
            BioCount INT(5) NOT NULL);     
                
        CREATE TABLE SolarSystems (
            SystemID INT(5) PRIMARY KEY NOT NULL,
            XLocation INT(5) NOT NULL,
            YLocation INT(5) NOT NULL,
            IsBlackHole VARCHAR(3) NOT NULL);
        
        CREATE TABLE ShipGroups (
            GroupID INT(5)  NOT NULL,
            PlayerID INT(5) NOT NULL,
            Name VARCHAR(30),
            SystemID INT(5) NOT NULL,
            PlanetID INT(5),
            FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
            FOREIGN KEY (SystemID, PlanetID) REFERENCES SystemPlanets(SystemID, PlanetID),
            PRIMARY KEY (PlayerID, GroupID));
        """)
        
    def insertNewTableRows(self): 
        self.cur.executemany("""INSERT INTO Players (ID, Name, Email, PasswdHash, StartDate, Score) VALUES (%s, %s, %s, %s, %s, %s)""",
                             [
                              (1, 'Aria', 'aria.kraft@gmail.com', 'xxxx', '2012-01-01', 0), 
                              (2, 'Brian', 'brian.barnes@gmail.com', 'xxxx', '2012-01-01', 0), 
                              (3, 'Dan', 'spam.dn@gmail.com', 'xxxx', '2012-01-01', 0)
                             ] )
        
        self.cur.executemany("""INSERT INTO SolarSystems (SystemID, XLocation, YLocation, IsBlackHole) VALUES (%s, %s, %s, %s)""", 
                             [
                              (0, 0, 0, 'YES'),
                              (1, 0, 1, 'NO'),
                              (2, 1, 0, 'NO'),
                              (3, 1, 1, 'NO'),
                              (4, 0, 2, 'NO')
                             ] )
        
        self.cur.executemany("""INSERT INTO PlanetTypes (PTypeID, Name, MineralCount, WaterCount, BioCount) VALUES (%s, %s, %s, %s, %s)""",
                             [
                              (0, 'Gas Giant', 1, 2, 3),
                              (1, 'Terrestrial', 4, 6, 5)
                             ] )
        
        self.cur.executemany("""INSERT INTO SystemPlanets (SystemID, PlanetID, PTypeID, MineralUsed, WaterUsed, BioUsed) VALUES (%s, %s, %s, %s, %s, %s)""", 
                             [
                              (0, 0, 0, 0, 0, 0),
                              (0, 1, 1, 4, 2, 0),
                              (1, 0, 0, 0, 0, 0),
                              (2, 0, 0, 0, 0, 0),
                              (3, 0, 0, 2, 1, 3),
                              (3, 1, 0, 5, 9, 0),
                              (3, 2, 1, 5, 5, 5),
                              (3, 3, 2, 6, 0, 0),
                              (4, 0, 0, 0, 0, 0),
                              (4, 1, 1, 2, 6, 3)
                             ] )
        
        self.cur.executemany("""INSERT INTO ShipGroups (UserID, GroupID, Name, SystemID, PlanetID) VALUES (%s, %s, %s, %s, %s)""",
                             [
                              (1, 0, 'Home Ship', 0, 0),
                              (1, 1, 'Squad A', 0, 1),
                              (1, 2, 'Squad B', 4, 1),
                              (1, 3, 'Squad C', 4, 0),
                              (2, 0, 'Home Ship', 0, 0),
                              (2, 1, 'Squad A', 3, 2),
                              (2, 2, 'Squad B', 3, 3),
                              (2, 3, 'Squad C', 3, 1),
                              (3, 0, 'Home Ship', 3, 2),
                              (3, 1, 'Squad A', 4, 0),
                              (3, 2, 'Squad B', 4, 1),
                              (3, 3, 'Squad C', 1, 0)
                             ] )
    
    

# Not really needed...
#    def closedb(self):
#        self.con.close()


#def index():
#    mygalaxy = Galaxy()
#    return mygalaxy.test()
#
#    mygalaxy.closedb()

        
if __name__ == "__main__":

    
    
#

#
