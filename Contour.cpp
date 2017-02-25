#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <vector>
using namespace cv;
using namespace std;
//

int main() {
    //load and convert image into gray image
    Mat image = imread("/home/dzou/CLionProjects/ObjectDetection/lemur.jpg", CV_LOAD_IMAGE_GRAYSCALE);
    Mat CannyImage;
    vector<Vec4i> hierarchy;
    vector<vector<Point>> contours;

    //blur image to reduce the amount of noise before using Canny edge detection
    bilateralFilter(image, CannyImage, 0, 175, 3, 0);
    //Canny detection
    Canny(image, CannyImage, 100, 150, 3);
    dilate(CannyImage, CannyImage, Mat::ones(2,2,CV_8UC1));

    //find contours
    findContours( CannyImage, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE ,Point(0, 0));
    Mat contouredImage( image.size(), CV_8UC3, Scalar(0) );
    //draw
    for (int i = 0; i< contours.size(); i++) {
        drawContours( contouredImage, contours, i, (255,255,255), 1, 8, hierarchy, 1, Point(0,0) );
    }
    //display results
    imshow("normal image", image);
    imshow("Contoured Image", contouredImage);
    waitKey();

    image.release();
    return 0;
}
