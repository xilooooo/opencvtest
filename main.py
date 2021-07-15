import cv2 as cv


src = cv.imread("D:/table/spbj/mao.jpg")
# 读取图片文件
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 创见一个名字为“input image”的窗口
cv.imshow("input image", src)
# 在这个窗口显示读取的图片文件
cv.waitKey(0)
# 等待用户操作

cv.destroyAllWindows()
# 释放所有窗口
# 123
