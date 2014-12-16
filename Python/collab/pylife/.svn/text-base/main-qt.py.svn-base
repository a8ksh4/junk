#!/usr/bin/python
import PyQt4.QtCore
import PyQt4.QtGui
import sys, random
from gridThing import *

class Cellmap(PyQt4.QtGui.QWidget):
    def __init__(self, gridthing, size):
        PyQt4.QtGui.QWidget.__init__(self)
        self.setAttribute(PyQt4.QtCore.Qt.WA_OpaquePaintEvent)
        self.gridthing = gridthing
        self.size = size
        
    def resizeEvent(self, resizeEvent):
        self.r = self.rect()
        self.pixmap = PyQt4.QtGui.QPixmap(self.width(), self.height())
        self.spacex = self.width() / self.size
        self.spacey = self.height() / self.size
        if(self.spacex < 5 or self.spacey < 5):
            self.cellborder = 0
        else:
            self.cellborder = 1

    def paintEvent(self, event):
        self.setUpdatesEnabled(False)
        self.painter = PyQt4.QtGui.QPainter(self.pixmap)
        self.painter.fillRect(self.rect(), PyQt4.QtCore.Qt.white)
        for y in range(0, self.size):
            for x in range(0, self.size):
                if self.gridthing.grid[x][y]:
                    self.painter.fillRect(x * self.spacex, y * self.spacey,
                        self.spacex - self.cellborder, self.spacey - self.cellborder, PyQt4.QtCore.Qt.black)
        self.painter.end()
        self.painter = PyQt4.QtGui.QPainter(self)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.setUpdatesEnabled(True)
        self.painter.end()

    def mouseReleaseEvent(self, event):
        for y in range(0, self.size-1):
            for x in range(0, self.size-1):
                v = self.gridthing.grid[x][y]
                if event.x() >= x * self.spacex and event.y() >= y * self.spacey and event.x() < (x + 1) * self.spacex and event.y() < (y + 1) * self.spacey:
                    self.gridthing.setState(x, y, not v)
        self.update()
        
class MyWindow(PyQt4.QtGui.QMainWindow):
    def __init__(self):
        PyQt4.QtGui.QMainWindow.__init__(self)
        self.setAttribute(PyQt4.QtCore.Qt.WA_OpaquePaintEvent)
        self.size = 50
        self.gridthing = GridThing(self.size, True)
        self.cellmap = Cellmap(self.gridthing, self.size)
        self.gridthing.randomize(1)
        self.setCentralWidget(self.cellmap)
        screen = PyQt4.QtGui.QDesktopWidget().screenGeometry()
        self.scrBuffer = 60
        if(screen.width() > screen.height()):
            self.winsize = screen.height() - self.scrBuffer
        else:
            self.winsize = screen.width() - self.scrBuffer
        self.winsize = 800
        self.setGeometry(screen.width() / 2 - self.winsize / 2, screen.height() / 2 - self.winsize / 2, self.winsize, self.winsize)
        self.timer = PyQt4.QtCore.QTimer()
        PyQt4.QtCore.QObject.connect(self.timer, PyQt4.QtCore.SIGNAL("timeout()"), self.timerUpdate)
        self.delay = 0
        self.gridthing.setEffectiveRule(0)
        self.fullscreen = False
        self.timer.start(self.delay)
        self.generations = 0
                
    def timerUpdate(self):
        self.generations += 1
        self.cellmap.repaint()
        self.gridthing.step()
        if self.generations > 200:
            sys.exit()
    
    def keyReleaseEvent(self, event):
        if event.key() == PyQt4.QtCore.Qt.Key_C:
            self.gridthing.clear()
        elif event.key() == PyQt4.QtCore.Qt.Key_Space:
            self.timer.stop()
            self.gridthing.step()
        elif event.key() == PyQt4.QtCore.Qt.Key_Return:
            self.timer.start(self.delay)
        elif event.key() == PyQt4.QtCore.Qt.Key_Plus:
            self.delay -= 10
            if(self.delay < 0):
                self.delay = 0
            self.timer.setInterval(self.delay)
        elif event.key() == PyQt4.QtCore.Qt.Key_Minus:
            self.delay += 10
            self.timer.setInterval(self.delay)
        elif event.key() == PyQt4.QtCore.Qt.Key_R:
            self.gridthing.randomize()
        elif event.key() == PyQt4.QtCore.Qt.Key_T:
            if(self.gridthing.getEffectiveRule() == 0):
                self.gridthing.setEffectiveRule(1)
            else:
                self.gridthing.setEffectiveRule(0)
        elif event.key() == PyQt4.QtCore.Qt.Key_F:
            self.setWindowState(self.windowState() ^ PyQt4.QtCore.Qt.WindowFullScreen)
        self.update()

if __name__ == "__main__":
#    import psyco
#    psyco.full()
    app =  PyQt4.QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
