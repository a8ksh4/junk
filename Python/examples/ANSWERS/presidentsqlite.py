#!/usr/bin/env python
import sqlite3

PRES_QUERY = '''
select num, lname, fname, dstart, dend, birthplace, birthstate,
    dbirth, ddeath, party
from presidents
where num = ?
'''


class President(object):

    def __init__(self,index):
        self._get_data(index)

    def _get_data(self,index):
        conn = sqlite3.connect("../DATA/PRESIDENTS")
        cur = conn.cursor()
        cur.execute(PRES_QUERY, (index,))
        row = cur.fetchone()
        self._termnum = row[0]
        self._lname = row[1]
        self._fname = row[2]
        self._ts_date = row[3]
        self._te_date = row[4]
        self._bplace = row[5]
        self._bstate = row[6]
        self._bdate = row[7]
        self._ddate = row[8]

    @property
    def LastName(self):
        return self._lname

    @property
    def FirstName(self):
        return self._fname

    @property
    def BirthDate(self):
        return self._bdate

    @property
    def DeathDay(self):
        return self._ddate

    @property
    def BirthPlace(self):
        return self._bplace

    @property
    def BirthState(self):
        return self._bstate

    @property
    def TermStart(self):
        return self._ts_date

    @property
    def TermEnd(self):
        return self._te_date

    @property
    def Party(self):
        return self._party

if __name__ == '__main__':
    for term in 1, 16, 26, 44:
        p = President(term)
        print p.FirstName, p.LastName