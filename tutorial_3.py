import cv2 as cv
import matplotlib.pyplot as plt
image = cv.imread("D:/table/spbj/mao.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# RGR转换为RGB显示格式
img = image[200:400, 200:500]
# 获取图像高度为200：400，宽度200：500区域的图像
images = [image, img]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.axis("off")
    # 关闭坐标轴
plt.show()
