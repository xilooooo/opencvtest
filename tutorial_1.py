import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    # 打开摄像头，捕捉摄像头实时信息，参数“0”表示为摄像头的编号
    # 如果加载视频，视频无声，只对帧进行分析
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        # 将图片水平翻转，第二个参数指的是上下是否颠倒，0进行上下颠倒
        cv.imshow("video", frame)
        # 将每一帧在窗口中显示
        c = cv.waitKey(50)
        # 参数指的是刷新频率，毫秒
        if c == 27:
            break
        # 等有键输入（这里指c=27=ESC）


def get_image_info(image):
    print(type(image))
    # 图像类别
    print(image.shape)
    # 返回图像的纵向横向像素及其通道数
    print(image.size)
    # 图像总的大小，长*宽*通道数
    print(image.dtype)
    # 每个像素点的字节数
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread("D:/table/spbj/mao.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
video_demo()
# gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)  # 灰度图
# cv.imwrite("D:/result.jpg", gray)
# cv.imwrite("D:/result.jpg", src)
cv.waitKey(0)

cv.destroyAllWindows()
