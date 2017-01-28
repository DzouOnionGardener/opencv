import cv2
import numpy as np

def main():
    xml_file = 'cars.xml'
    car_classifier = cv2.CascadeClassifier(xml_file)
    camera = cv2.VideoCapture("Baltimore.mp4")

    print("video file read")
    while (cv2.waitKey(1) != 27):
        ret, frame = camera.read()
        if not ret or frame is None:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        car = car_classifier.detectMultiScale(gray, 1.1, 3)
        
        for (x, y, w, h) in car:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow("capture", frame)
    print("stopping")
    camera.release()
    cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    main()
