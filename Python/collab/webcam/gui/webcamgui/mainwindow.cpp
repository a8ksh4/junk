#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    capture = cvCaptureFromCAM( 0 );
    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(update_frame()));
    timer->start(60);
}

MainWindow::~MainWindow()
{
    cvReleaseCapture(&capture);
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    frame = cvQueryFrame(capture);

    QImage image = QImage((const uchar *)frame->imageData, frame->width, frame->height, QImage::Format_RGB888).rgbSwapped();
    ui->label->setPixmap(QPixmap::fromImage(image));
}

void MainWindow::update_frame()
{
    frame = cvQueryFrame(capture);

    QImage image = QImage((const uchar *)frame->imageData, frame->width, frame->height, QImage::Format_RGB888).rgbSwapped();
    ui->label->setPixmap(QPixmap::fromImage(image));

}
