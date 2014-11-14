#!/usr/bin/env python

from datetime import datetime, date, timedelta

def mkdate(year, month, day):
    if year:
        return date(int(year), int(month), int(day) )
    else:
        return date.today()

def get_info(index):
    pres_data = {}
    with open("../DATA/presidents.txt") as pfile:
        for line in pfile:
            flds = line[:-1].split(":")
            if int(flds[0]) == index:
                pres_data["lastname"] = flds[1]
                pres_data["firstname"] = flds[2]
    
                pres_data["birthdate"] = mkdate(flds[3], flds[4], flds[5])
                pres_data["deathdate"] = mkdate(flds[6], flds[7], flds[8])
    
                pres_data["birthplace"] = flds[9]
                pres_data["birthstate"] = flds[10]
    
                pres_data["termstart"] = mkdate(flds[11], flds[12], flds[13])
                pres_data["termend"] = mkdate(flds[14], flds[15], flds[16])
    
                pres_data["party"] = flds[17]
    
                break
            
        else:
            print "No president with that index!"

    return pres_data

def get_all_data():
    return [get_info(i) for i in range(1,44)]

def get_age_at_term_end(pinfo):
    birthdate = pinfo["birthdate"]
    termend = pinfo["termend"]
    if termend is None:
        termend = date.today()
    age_at_end = termend-birthdate
    return age_at_end.days

def get_age_at_term_start(pinfo):
    birthdate = pinfo["birthdate"]
    termstart = pinfo["termstart"]
    if termstart is None:
        termstart = date.today()
    age_at_start = termstart-birthdate
    return age_at_start.days

def get_youngest():
    all_raw = get_all_data()
    all_cooked = sorted(all_raw, key=get_age_at_term_start, reverse=True)
    return all_cooked[-1]

def get_oldest():
    all_raw = get_all_data()
    all_cooked = sorted(all_raw, key=get_age_at_term_end)
    return all_cooked[-1]


