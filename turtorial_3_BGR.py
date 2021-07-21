import cv2 as cv
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 显示中文
image = cv.imread("D:/table/spbj/mao.jpg")
B = image[:, :, 0]
# blue
G = image[:, :, 1]
# green
R = image[:, :, 2]
# red
print("B", B)
print("G", G)
print("R", R)
# 3  通道的获取
B = cv.cvtColor(B, cv.COLOR_BGR2RGB)
G = cv.cvtColor(G, cv.COLOR_BGR2RGB)
R = cv.cvtColor(R, cv.COLOR_BGR2RGB)
# BGR invert to RGB
# B, G, R = cv.split(image)
titles = ["B通道", "G通道", "R通道"]
img = [B, G, R]
for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(img[i])
    plt.title(titles[i])
    plt.axis("off")
    # 关闭坐标轴
plt.show()
'''通道合并
img = cv.merge([B, G, R])
img = cv. cvtColor(img, cv.COLOR_BGR2RGB)'''