import cv2 as cv
import matplotlib.pyplot as plt
image = cv.imread("D:/table/spbj/mao.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# RGR转换为RGB显示格式
img = image[200:400, 300:500]
# 获取图像高度为200：400，宽度200：500区域的图像
image[:200, :200] = img
# ROI区域一直到原图左上角
images = [image, img]
# 对比显示
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.axis("off")
    # 关闭坐标轴，on为开启坐标轴.
plt.show()
