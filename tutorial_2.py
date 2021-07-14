import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s, channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 255
    # img[;, ;, 0] blue 1 green 2 red   jpg三个通道png四个
    cv.imshow("new image", img)


src = cv.imread("D:/table/spbj/mao.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
create_image()
t2 = cv.getTickCount()
print("time : %s ms" % ((t2 - t1) / cv.getTickFrequency() * 1000))
cv.waitKey(0)

cv.destroyAllWindows()
