#先要安装pygame
import time
import pygame

#音乐路径
filePath = r"E:\python\office文件操作\6.音乐播放器\sound1.mp3"

#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)
#播放
pygame.mixer.music.play()
#
time.sleep(10)
#暂停
pygame.mixer.music.pause()
#停止
pygame.mixer.music.stop()