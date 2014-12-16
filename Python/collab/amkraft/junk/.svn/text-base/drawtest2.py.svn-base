import gtk

def expose_handler(widget, event) :
    widget.window.draw_rectangle(red, True, 200, 200, 100, 100)
    widget.window.draw_rectangle(blue, True, 250, 250, 100, 100)

win = gtk.Window()
drawing_area = gtk.DrawingArea()
drawing_area.set_size_request(600, 400)
win.add(drawing_area)
drawing_area.connect("expose-event", expose_handler)
win.show_all()

red = drawing_area.window.new_gc()
red.set_rgb_fg_color(gtk.gdk.color_parse("red"))
blue = drawing_area.window.new_gc()
blue.set_rgb_fg_color(gtk.gdk.color_parse("blue"))

gtk.main()
