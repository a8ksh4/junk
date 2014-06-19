#!/usr/bin/env python

from president import President

def fn(self):
    return '{0} {1}'.format(self.FirstName,self.LastName)
    
setattr(President,'FullName',property(fn))
# or just
# President.getFullName = fn

abe = President(16)
print abe.FullName
