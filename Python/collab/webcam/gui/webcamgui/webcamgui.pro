#-------------------------------------------------
#
# Project created by QtCreator 2010-11-01T20:40:33
#
#-------------------------------------------------

QT       += core gui

TARGET = webcamgui
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui

RESOURCES +=

win32:INCLUDEPATH += "c:\\OpenCV2.1\\include\\opencv\\"

#LIBS += "C:\\openCV2.1\\lib\\cv210.lib C:\\openCV2.1\\lib\\highgui210.lib"


win32:LIBS += "C:\\openCV2.1\\lib\\cv210.lib"
win32:LIBS += "C:\\openCV2.1\\lib\\highgui210.lib"
