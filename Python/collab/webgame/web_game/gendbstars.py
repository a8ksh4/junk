#!/usr/bin/python
# -*- coding: utf-8 -*-

    def __init__(self, dbserver='localhost', login='root', passwd='R1ven', dbname='dantest'):
        self.con = MySQLdb.connect(dbserver, login, passwd, dbname)
        self.cur = self.con.cursor()


if __name__ == "__main__":
    con = MySQLdb.connect('localhost', 'root', 'R1ven', 'Web_game')
    cur = con.cursor()
    
    items=[];
   
    for count in range(10):
        randx = random.randint(-300, 300)
        randy = random.randint(-300, 300)