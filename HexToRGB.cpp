// HexToRGB.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
using namespace std;
using namespace cv;
const unsigned int redHex	= 0xFF0000;
const unsigned int greenHex = 0x00FF00;
const unsigned int blueHex	= 0x0000FF;

void createColoredImage(int R, int G, int B);
int main()
{
	//32 bits
	cout << "Enter hex color code: \n";
	unsigned int RGBA_Value;
	cin >> std::hex >> RGBA_Value;
	//RGBA:
	//Blue:   bits    0 .. 7
	//Green:  bits	  8 .. 15
	//Red:    bits	  16 .. 24

	unsigned char R = (RGBA_Value & redHex) >> 16;
	unsigned char G = (RGBA_Value & greenHex) >> 8;
	unsigned char B = (RGBA_Value & blueHex);

	cout << "RGB: " << static_cast<int>(R) << ", " << static_cast<int>(G) << ", " << static_cast<int>(B) << endl;
	createColoredImage(static_cast<int>(R), static_cast<int>(G), static_cast<int>(B));

	system("PAUSE");
    return 0;
}

void createColoredImage(int R, int G, int B) {
	Mat image(200, 200, CV_8UC3, Scalar(R, G, B));
	imshow("color", image);

	waitKey(0);
	cvReleaseData;
	cvReleaseImage;
}