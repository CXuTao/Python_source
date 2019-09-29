"""
要安装三方库，需要知道模块的名字
#Pillow  非常强大的处理图像的工具库
pip install Pillow
pip install --upgrade pip
"""
#引入第三方库
from PIL import Image

#打开图片
im = Image.open("1.png")
#查看图片的信息
print(im.format, im.size, im.mode)
#设置图片的大小
im.thumbnail((100,100))
#保存为新图片
im.save("temp.png", "PNG")