#include <cv.h>
#include <highgui.h>
#include <stdio.h>

void main(int argc, char *argv[])
{
	CvCapture *capture = 0;
	IplImage  *frame = 0;
	int key = 0;

	capture = cvCaptureFromCAM( 0 );

	if (!capture) {
		printf("Cannot open initialize webcam!\n");
		return;
	}

	cvNamedWindow("result", CV_WINDOW_AUTOSIZE );

	for(int c = 0; c < 0; c++)
	{
		frame = cvQueryFrame(capture);
	}


	while(key != 'q') {
		frame = cvQueryFrame(capture);
		if(!frame)
			break;
		cvShowImage("result", frame);
		key = cvWaitKey(1);
	}

	cvDestroyWindow("result");
	cvReleaseCapture(&capture);
}
