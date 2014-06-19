#!/usr/bin/env python

from sh import ls, glob
print ls('-ld', glob('/etc/pr*'))
