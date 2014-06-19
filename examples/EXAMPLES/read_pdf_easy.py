#!/usr/bin/env python

import sys
import os

import requests

url = 'http://www.gutenberg.org/dirs/etext98/2ws2610.pdf'
saved_pdf_file = 'hamlet.pdf'

# auth and proxy
# response = requests.get(url,auth=('jrhacker','$3cr3t'),proxies={'http','http://www.random.com'})

response = requests.get(url)
if response.status_code == requests.codes.OK:

    with open(saved_pdf_file,'wb') as HAM:
        HAM.write(response.content)
    
    if sys.platform == 'win32':
        cmd = saved_pdf_file
    elif sys.platform == 'darwin':
        cmd = 'open ' + saved_pdf_file
    else:
        cmd = 'acroread ' + saved_pdf_file
    
    os.system(cmd)