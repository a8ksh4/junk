#!/usr/bin/env python

from sh import grep
grep('root','/etc/passwd',_out='grep.out')