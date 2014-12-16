import matplotlib.figure, matplotlib.backends.backend_gtkagg, numpy, gtk, gtk.glade

class MainApp:
    def setupGraph(self):
        self.figure = matplotlib.figure.Figure()
        self.axis = self.figure.add_subplot(111)
        t = numpy.arange(0.0, 3.0, 0.01)
        s = numpy.sin(2 * numpy.pi * t)
        food = [10, 5, 30]
        bugs = [5, 10, 25]
        self.axis.plot(food, '-gs', label='food')
        self.axis.plot(bugs, '-bo', label='bugs')
        self.axis.set_xlabel('time (s)')
        self.axis.set_ylabel('voltage')
        self.canvas = matplotlib.backends.backend_gtkagg.FigureCanvasGTKAgg(self.figure)
        self.canvas.set_size_request(600, 400)
        self.vboxMain.pack_start(self.canvas, True, True)
        self.navToolbar = matplotlib.backends.backend_gtkagg.NavigationToolbar2GTKAgg(self.canvas, self.windowMain)
        self.vboxMain.pack_start(self.navToolbar)
        sep = gtk.HSeparator()
        self.vboxMain.pack_start(sep, True, True)
        self.vboxMain.reorder_child(self.buttonClickMe, -1)

    def __init__(self):
        self.widgets = gtk.Builder()
        self.widgets.add_from_file('mpl_with_glade2.glade')
        self.windowMain = self.widgets.get_object('windowMain')
        self.vboxMain = self.widgets.get_object('vboxMain')
        self.buttonClickMe = self.widgets.get_object('buttonClickMe')
        self.windowMain.connect('destroy', gtk.main_quit)
        self.setupGraph()
        self.windowMain.show_all()

mainapp = MainApp()
gtk.main()