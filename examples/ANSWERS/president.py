#!/usr/bin/env python
from datetime import date

class President(object):

    def __init__(self,index):
        self.num = index
        self._lname = None
        self._fname = None
        self._bdate = None
        self._ddate = None
        self._birthplace = None
        self._birth_state = None
        self._ts_date = None
        self._te_date = None
        self._party = None
        self._get_data(index)

    @staticmethod
    def _mk_date(year, month, day):
        if year:
            return date(int(year), int(month), int(day) )
        else:
            return None

    def _get_data(self,index):
        with open("../DATA/presidents.txt") as pfile:
            for line in pfile:
                fields = line.split(":")
                if int(fields[0]) == int(index):
                    self._lname = fields[1]
                    self._fname = fields[2]
    
                    self._birth_date = self._mk_date(fields[3], fields[4], fields[5])
                    self._death_date = self._mk_date(fields[6], fields[7], fields[8])

                    self._birthplace = fields[9]
                    self._birth_state = fields[10]
    
                    self._ts_date = self._mk_date(fields[11], fields[12], fields[13])
                    self._te_date = self._mk_date(fields[14], fields[15], fields[16])
    
                    self._party = fields[17]
    
                    break

    @property
    def LastName(self):
        return self._lname

    @property
    def FirstName(self):
        return self._fname

    @property
    def BirthDate(self):
        return self._birth_date

    @property
    def DeathDate(self):
        return self._death_date

    @property
    def BirthPlace(self):
        return self._birthplace

    @property
    def BirthState(self):
        return self._birth_state

    @property
    def TermStart(self):
        return self._ts_date

    @property
    def TermEnd(self):
        return self._te_date

    @property
    def Party(self):
        return self._party

