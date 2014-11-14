#!/usr/bin/env python

from president import President

p = President(26)

lastname = getattr(p, 'LastName')
firstname = getattr(p, 'FirstName')
party = getattr(p, 'Party')
print firstname, lastname, 'was a', party