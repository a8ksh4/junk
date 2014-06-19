#!/usr/bin/env python

from sh import wc

wc_output = wc('-l', '/etc/passwd')
pw_lines, junk = wc_output.split()

print "{0} lines in /etc/passwd".format(pw_lines)

