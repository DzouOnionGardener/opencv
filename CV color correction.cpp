// CV color correction.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <c:\openCV-3.1.0\opencv\build\include\opencv2\imgproc\imgproc.hpp>
#include <c:\openCV-3.1.0\opencv\build\include\opencv2\core.hpp>
#include <c:\openCV-3.1.0\opencv\build\include\opencv\highgui.h>
#include <c:\openCV-3.1.0\opencv\build\include\opencv2\opencv.hpp>
#include <c:\openCV-3.1.0\opencv\build\include\opencv\cv.h>
#include <iostream>
using namespace cv;
using namespace std;

int main()
{
	Mat my_image = imread("bug.jpg");

	imshow("bug", my_image);
	cvWaitKey(0);

	system("PAUSE");
	return EXIT_SUCCESS;
}

//postponed
