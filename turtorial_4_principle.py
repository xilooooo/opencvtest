import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
img = cv2.imread("my.jpg")
h, w = img.shape[0:2]
# 获取图像尺寸
gray = np.zeros((h, w), dtype=img.dtype)
# 自定义空白单通道图像，用于存放灰度图
for i in range(h):
    for j in range(w):
        gray[i, j] = 0.11*img[i, j, 0]+0.59*img[i, j, 1]+0.3*img[i, j, 2]
        # Y=0.3R+0.59G+0.11B
# 对原图像进行遍历，然后分别对B\G\R按比例灰度化
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
# BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
plt.imshow(gray)
plt.title('Y-亮度：灰度处理')    
plt.axis('off')
# 关闭坐标轴
plt.show()
