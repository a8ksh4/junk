#!/usr/bin/env python

import sys

import urllib
import urllib2
import json

DATA_TYPE = 'application/json'

def main(args):

    if len(args) < 1:
        print "Please specify a search term"
        sys.exit(1)
    
    query_terms = { 'q': args[0] }
    params = urllib.urlencode(query_terms)
    
    url = 'http://lcboapi.com/products?' + params
    
    response = urllib2.urlopen(url)
    
    raw_result = response.read()    
    # print('RAW RESULT:', raw_result, '\n\n')

    raw_json = json.loads(raw_result)
    # print('RAW JSON:', raw_json, '\n\n')
    if raw_json['result']:
        for result in raw_json['result']:
            print "PRODUCT NUMBER:", result['product_no']
            print "NAME:", result['name']
            print "PACKAGE:", result['package']
            print "PRICE: ${0:5.2f}/liter".format(result['price_per_liter_in_cents']/100)
            print
    else:
        print "Sorry, no items matched your query."

if __name__ == '__main__':
    main(sys.argv[1:])