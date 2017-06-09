import urllib
import cv2
import numpy as np
import os

def storePositives():
    url = ""
    imageURLs = urllib.urlopen(url).read().decode('ascii', 'ignore').encode('ascii', 'ignore')

    if not os.path.exists("pos"):
        os.makedirs("pos")

    picIndex = 1
    for i in imageURLs.split('\n'):
        try:
            urllib.urlretrieve(i,"/pos/"+str(picIndex)+'.jpg')
            img = cv2.imread("/pos/"+str(picIndex)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized = cv2.resize(img, (100, 100))
            cv2.imwrite("/pos/"+str(picIndex)+'.jpg', resized)
            picIndex += 1
        except Exception as err:
            print err
            pass

def storeNegatives():
    url = ""
    imageURLs = urllib.urlopen(url).read().decode('ascii', 'ignore').encode('ascii', 'ignore')

    if not os.path.exists("/neg"):
        os.makedirs("/neg")

    picIndex = 1
    for i in imageURLs.split('\n'):
        try:
            urllib.urlretrieve(i,"/neg/"+str(picIndex)+'.jpg')
            img = cv2.imread("/neg/"+str(picIndex)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized = cv2.resize(img, (100, 100))
            cv2.imwrite("/neg/"+str(picIndex)+'.jpg', resized)
            picIndex += 1
        except Exception as err:
            print err
            pass


if __name__ == "__main__":
    storePositives()
    storeNegatives()