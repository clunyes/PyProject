# @Time    : 2024/1/8 PM1:40
# @Author  : kang
# @File    : day28.py
# @Desc    :

from PIL import Image

# 读取图像获得Image对象
image = Image.open('dm.jpg')
# 通过Image对象的format属性获得图像的格式
print(image.format) # JPEG
# 通过Image对象的size属性获得图像的尺寸
print(image.size)   # (500, 750)
# 通过Image对象的mode属性获取图像的模式
print(image.mode)   # RGB
# 通过Image对象的show方法显示图像
image.show()
