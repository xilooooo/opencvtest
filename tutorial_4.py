import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
image=cv2.imread("D:/table/spbj/mao.jpg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#BGR转换为灰度
image= cv2.cvtColor(gray,cv2.COLOR_BGR2RGB)
#灰度的BGR转换为RGB显示格式
plt.imshow(image)  
plt.title("灰度处理")    
plt.axis("off")
# 关闭坐标轴
plt.show()
