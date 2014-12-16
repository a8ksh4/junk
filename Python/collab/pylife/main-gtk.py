#!/usr/bin/env python
import gobject
import gtk
import gridThing

class MyWindow():
    def __init__(self):
        self.generations = 0
        self.size = 800
        self.border = 1
        self.count = 200
        self.cellsize = self.size / self.count
        if(self.cellsize < 5):
            self.border = 0
        self.worldwrap = True
        self.gridthing = gridThing.GridThing(self.count, self.worldwrap)
        self.gridthing.randomize(1)
        self.initwin()
        
    def initwin(self):
        self.win = gtk.Window()
        self.drawing_area = gtk.DrawingArea()
        self.drawing_area.set_size_request(self.size, self.size)
        self.win.connect("destroy", gtk.main_quit)
        self.win.add(self.drawing_area)
        self.win.show_all()
        self.white = self.drawing_area.get_style().white_gc
        self.black = self.drawing_area.get_style().black_gc
        gobject.idle_add(self.idle)
        
    def idle(self):
        self.draw()
        self.generations += 1
        self.gridthing.step()
        return True
    
    def draw(self) :
        r = self.drawing_area.get_allocation()
        self.drawing_area.window.begin_paint_rect(r)
        gc = self.drawing_area.window.new_gc()
        self.drawgrid()
        self.drawing_area.window.end_paint()

    def drawgrid(self):
        self.drawing_area.window.draw_rectangle(self.white, True, 0, 0, self.size, self.size)
        for y in range(self.count):
            for x in range(self.count):
                if self.gridthing.grid[x][y]:
                    self.drawing_area.window.draw_rectangle(self.black, True, x * self.cellsize, y * self.cellsize,
                        self.cellsize - self.border, self.cellsize - self.border)
    
if __name__ == "__main__":
    #import psyco
    #psyco.full()
    win = MyWindow()
    print win.gridthing 
    gtk.main()
