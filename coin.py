import pygame
import random


class Coin:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.coin = pygame.image.load('coin.png')
        self.coin = pygame.transform.scale(self.coin, (ai_settings.coin_size, ai_settings.coin_size))
        self.rect = self.coin.get_rect()
        self.mask = pygame.mask.from_surface(self.coin)

        self.rect.left = ai_settings.screen_width / 2
        self.rect.top = ai_settings.screen_high / 2

        self.screen_rect = screen.get_rect()

    def update_coin(self):
        if self.ai_settings.coin_f == 700:  # 控制苹果更新频率
            self.rect.left = random.randint(0, self.ai_settings.screen_width)
            self.rect.top = random.randint(100, self.ai_settings.screen_high - self.ai_settings.tree_high)

        self.ai_settings.coin_f += 1

        if self.ai_settings.coin_f > 700:
            self.ai_settings.coin_f = 0

    def blit_coin(self):
        self.screen.blit(self.coin, self.rect)