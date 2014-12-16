#!/usr/bin/env python
import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)

while 1:
    c = stdscr.getch()
    if c == ord('p'): print "hello"
    elif c == ord('q'): break  # Exit the while()
    print c


stdscr.nodelay(0)
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
