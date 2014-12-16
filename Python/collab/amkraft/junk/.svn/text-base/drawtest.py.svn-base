import gobject, gtk, random

class Window:
    def __init__(self):
        self.rand = random.Random()
        self.size = 400
        self.border = 1
        self.count = 10
        self.cellsize = self.size / self.count
        if(self.cellsize < 5):
            self.border = 0
        self.initwin()
        
    def createColorGC(self, colorStr):
        color = self.drawing_area.window.new_gc()
        color.set_rgb_fg_color(gtk.gdk.color_parse(colorStr))
        return color
        
    def initwin(self):
        self.win = gtk.Window()
        self.drawing_area = gtk.DrawingArea()
        self.drawing_area.set_size_request(self.size, self.size)
        self.win.connect("destroy", gtk.main_quit)
        self.win.add(self.drawing_area)
        self.win.show_all()
        self.blue = self.createColorGC("blue")
        self.red = self.createColorGC("red")
        self.white = self.createColorGC("white")
        self.black = self.createColorGC("black")
        gobject.idle_add(self.idle)
        
    def idle(self):
        self.drawgrid()
        return True

    def drawgrid(self):
        self.drawing_area.window.draw_rectangle(self.white, True, 0, 0, self.size, self.size)
        for y in range(self.count):
            for x in range(self.count):
                if self.rand.randint(0, 1):
                    color = self.red
                else:
                    color = self.white
                    
                self.drawing_area.window.draw_rectangle(color, True, y * self.cellsize, x * self.cellsize,
                    self.cellsize - self.border, self.cellsize - self.border)
    
if __name__ == "__main__":
    Window()
    gtk.main()
