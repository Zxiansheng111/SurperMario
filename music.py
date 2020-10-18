import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("bg_music.wav") # 载入音乐
pygame.mixer.music.set_volume(0.2)# 设置音量为 0.2
pygame.mixer.music.play() # 播放音乐




