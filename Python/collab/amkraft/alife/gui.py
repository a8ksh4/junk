import pygtk
pygtk.require("2.0")
import gobject, gtk, random, sys
import worldGrid, organism, food

class Window:
    def __init__(self):
        self.paused = False
        self.rand = random.Random()
        self.world = worldGrid.WorldGrid(gridSize=20, foodValue=100,
                                         movementCost=1, rand=self.rand)
        self.size = 400
        self.border = 1
        self.count = self.world.gridSize
        self.cellsize = self.size / self.count
        if(self.cellsize < 5):
            self.border = 0
        self.initwin()
            
    def on_pause_clicked(self, widget, data=None):
        self.paused = not self.paused
    
    def on_step_clicked(self, widget, data=None):
        self.paused = True
        self.world.stepGrid()
        
    def on_reset_clicked(self, widget, data=None):
        self.world.reset()
        
    def on_stats_ok_clicked(self, widget, data=None):
#        p = self.statswin.get_position()
        self.statswin.hide()
#        self.statswin.move(p[0], p[1])
        pass
    
    def on_stats_clicked(self, widget, data=None):
        self.statswin.show_all()
        pass

    def initwin(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("alife.glade")
        self.builder.connect_signals(self)
        
        win = self.builder.get_object("window1")
        self.statswin = self.builder.get_object("window2")

        self.drawing_area = self.builder.get_object("drawingarea1")
        self.drawing_area.set_size_request(self.size, self.size)
        win.connect("destroy", gtk.main_quit)
        
        self.pausebtn = self.builder.get_object("pause")
        self.stepbtn = self.builder.get_object("step")
        self.resetbtn = self.builder.get_object("reset")
        
        win.show_all()
        
        self.cmap = self.drawing_area.get_colormap()
        self.white = self.cmap.alloc_color("white")
        self.black = self.cmap.alloc_color("black")
        self.red = self.cmap.alloc_color("red")
        self.green = self.cmap.alloc_color("green")
        self.blue = self.cmap.alloc_color("blue")
        self.gray = self.cmap.alloc_color("gray")
        self.style = self.drawing_area.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
    
        gobject.idle_add(self.idle)
        
    def idle(self):
        self.draw()
        if(not self.paused):
            self.world.stepGrid()
#            bugsCount = self.world.countItemsOfType(organism.Organism)
#            foodCount = self.world.countItemsOfType(food.Food)
#            self.stats.append([bugsCount, foodCount])
        return True

    def draw(self) :
        c = self.gc.foreground
        r = self.drawing_area.get_allocation()
        self.drawing_area.window.begin_paint_rect(r)
        
        self.gc.foreground = self.gray
        self.drawing_area.window.draw_rectangle(self.gc, True, 0, 0, self.size, self.size)
        for y in range(self.count):
            for x in range(self.count):
                items = self.world.getItems(x, y)
                if len(items) > 0:
                    if isinstance(items[0], organism.Organism):
                        color = self.blue
                    elif isinstance(items[0], food.Food):
                        color = self.green
                else:
                    color = self.white
                self.gc.foreground = color
                self.drawing_area.window.draw_rectangle(self.gc, True, y * self.cellsize, x * self.cellsize,
                    self.cellsize - self.border, self.cellsize - self.border)
        self.drawing_area.window.end_paint()
        self.gc.foreground = c
    
if __name__ == "__main__":
    Window()
    gtk.main()
