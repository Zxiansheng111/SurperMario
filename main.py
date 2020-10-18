import pygame
import wave
from pygame import mixer
import time
import egame_functions as gf
from esettings import Esettings
import sys
from coin import Coin
from character import Character
from tree import Tree


pygame.init()  # 初始化

pygame.mixer.init()
pygame.mixer.music.load("Maliao.mp3") # 载入音乐
pygame.mixer.music.set_volume(1)# 设置音量
pygame.mixer.music.play() # 播放音乐

ai_settings = Esettings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_high))
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("超级马里奥！")
background = pygame.image.load("background1.jpg")
background = pygame.transform.scale(background, (ai_settings.screen_width, ai_settings.screen_high))


gf.game_intro()
pygame.quit()
quit()