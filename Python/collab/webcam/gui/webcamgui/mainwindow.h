#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTimer>
#include <cv.h>
#include <highgui.h>

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    CvCapture *capture;
    IplImage  *frame;
    QTimer *timer;

private slots:
    void on_pushButton_clicked();
    void update_frame();
};

#endif // MAINWINDOW_H
