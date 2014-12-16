import sys, pygtk, matplotlib, gtk, gtk.glade, matplotlib.backends.backend_gtk, pylab

class app:
    def __init__(self):
        self.wTree = gtk.glade.XML("mplglade.glade")
        self.wTree.signal_autoconnect(self)
        self.figure = matplotlib.backends.backend_gtk.Figure()
        self.axis = self.figure.add_subplot(111)
        self.ba = self.axis.bar([0, 1, 2], (4,5,6), 0.15, color='r')
        self.bb = self.axis.bar([0.15, 1.15, 2.15], (3,2,1), 0.15, color='b')
        self.canvas = matplotlib.backends.backend_gtk.FigureCanvasGTK(self.figure)
        self.canvas.show()
        self.grahview = self.wTree.get_widget("vbox")
        self.grahview.pack_start(self.canvas, True, True)

    def on_btn_draw_clicked(self, widget):
#        self.axis.bar([0, 1, 2], (1,2,3), 0.15, color='r')
#        self.axis.bar([0.15, 1.15, 2.15], (4,5,6), 0.15, color='b')
#        self.canvas = matplotlib.backends.backend_gtk.FigureCanvasGTK(self.figure)
#        self.canvas.show()
#        self.grahview = self.wTree.get_widget("vbox")
#        self.grahview.pack_start(self.canvas, True, True)

        self.ba = self.axis.bar([0, 1, 2], (1,2,3), 0.15, color='g')
        self.canvas.show()

app = app()
gtk.main()