'''
Created on Dec 6, 2013

@author: drnorris
'''
from subprocess import check_output,Popen,PIPE
import csv


def runProc(command, type="csv", fieldMap=None):
    '''
    If fieldMap is defined, accepts dict like: {'fullid': 0, 'class': 1} and returns
    output as list of dictionaries. 
    If type is not csv, then returns list of lines, else list of lists (or dicts). 
    '''
    proc = Popen(command, shell=True, stdout=PIPE)

    output = []
    while True:
        line = proc.stdout.readline().strip()
        if line:
            if type == "csv":
                for row in csv.reader([line]):
                    if fieldMap == None:
                        output.append(row)
                    else:
                        output.append({})
                        for key in fieldMap.keys():
                            output[-1][key] = row[fieldMap[key]]
            else:
                output.append(line)
        else:
            break

    return output
