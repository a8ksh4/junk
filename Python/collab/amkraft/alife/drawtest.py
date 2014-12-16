import pygtk, gtk, operator, time, string
pygtk.require('2.0')

class DrawingAreaExample:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Drawing Area Example")
        window.connect("destroy", self.main_quit)
        self.area = gtk.DrawingArea()
        self.area.set_size_request(200, 200)
        window.add(self.area)
        self.area.connect("expose-event", self.area_expose_cb)
        window.show_all()
        cmap = self.area.get_colormap()
        self.color = cmap.alloc_color("blue")
        self.style = self.area.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]

    def main_quit(self, data=None):
        gtk.main_quit()

    def area_expose_cb(self, areaa, eventa):
        self.gc.set_foreground(self.color)
        self.area.window.draw_rectangle(self.gc, True, 10, 10, 20, 20)

if __name__ == "__main__":
    DrawingAreaExample()
    gtk.main()
