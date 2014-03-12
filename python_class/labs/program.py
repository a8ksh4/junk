"""
This program accepts a filename and a column name on the command line
and optionally a value. If the value is specified it prints the row
from the file that contains the value in the column, else it prints
the column. Files are assumed to be .csv with columnames in the first
row.

So:

file.txt:
foo,bar
one,two
three,four

$ program.py --file=file.txt --column=foo
one
three

$ program.py --file=file.txt --column=foo one
one,two

"""


