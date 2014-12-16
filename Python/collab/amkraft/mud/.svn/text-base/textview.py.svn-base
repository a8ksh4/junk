#!/usr/bin/env python
import pygtk
import gtk

def close_application(widget):
    gtk.main_quit()

def InitApp():
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_resizable(True)  
    window.connect("destroy", close_application)
    window.set_title("TextView")
    window.set_default_size(400, 400)

    cont = gtk.VBox()
    window.add(cont)
    cont.show()

    sw = gtk.ScrolledWindow()
    sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    textview = gtk.TextView()
    textview.set_editable(False)
    textview.set_cursor_visible(False)
    textview.set_wrap_mode(gtk.WRAP_WORD)
    
    textbuffer = textview.get_buffer()
    sw.add(textview)
    sw.show()
    textview.show()

    cont.pack_start(sw)
    infile = open("textview.py", "r")

    if infile:
        string = infile.read()
        infile.close()
        textbuffer.set_text(string)

    button = gtk.Button("close")
    button.connect("clicked", close_application)
    cont.pack_start(button, False)
    button.set_flags(gtk.CAN_DEFAULT)
    button.grab_default()
    button.show()
    window.show()

if __name__ == "__main__":
    InitApp()
    gtk.main()
