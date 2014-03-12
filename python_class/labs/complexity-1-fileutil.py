"""
>>> from StringIO import StringIO
>>> input_data = StringIO('''localhost - - [09/Jul/2010:13:08:34 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 949462 Send-Document successful-ok
... localhost - - [09/Jul/2010:13:08:34 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok
... localhost - - [09/Jul/2010:13:09:15 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1669 Create-Job successful-ok
... localhost - - [09/Jul/2010:13:09:15 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 79979 Send-Document successful-ok
... localhost - - [09/Jul/2010:13:09:16 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok
... localhost - - [09/Jul/2010:13:09:54 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1496 Create-Job successful-ok
... localhost - - [09/Jul/2010:13:09:54 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 73339 Send-Document successful-ok
... localhost - - [09/Jul/2010:13:09:54 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok
... localhost - - [11/Jul/2010:22:05:31 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1453 Create-Job successful-ok
... ''')
>>> grep(input_data, 'HTTP')
['localhost - - [09/Jul/2010:13:08:34 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 949462 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:08:34 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok', 'localhost - - [09/Jul/2010:13:09:15 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1669 Create-Job successful-ok', 'localhost - - [09/Jul/2010:13:09:15 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 79979 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:09:16 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok', 'localhost - - [09/Jul/2010:13:09:54 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1496 Create-Job successful-ok', 'localhost - - [09/Jul/2010:13:09:54 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 73339 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:09:54 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok', 'localhost - - [11/Jul/2010:22:05:31 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1453 Create-Job successful-ok']
>>> input_data.seek(0)
>>> grep(input_data, '09/Jul/2010:13:08:34')
['localhost - - [09/Jul/2010:13:08:34 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 949462 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:08:34 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok']
>>> input_data.seek(0)
>>> grep(input_data, 'localhost', inverse=True)
[]
>>> input_data.seek(0)
>>> grep(input_data, '13:09', inverse=True)
['localhost - - [09/Jul/2010:13:08:34 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 949462 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:08:34 -0700] "POST / HTTP/1.1" 200 313 Set-Job-Attributes successful-ok', 'localhost - - [11/Jul/2010:22:05:31 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 1453 Create-Job successful-ok']
>>> input_data.seek(0)
>>> grep(input_data, r'200 \d{5,6} ', extended=True)
['localhost - - [09/Jul/2010:13:08:34 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 949462 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:09:15 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 79979 Send-Document successful-ok', 'localhost - - [09/Jul/2010:13:09:54 -0700] "POST /printers/HP_LaserJet_P2015_Series HTTP/1.1" 200 73339 Send-Document successful-ok']
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
