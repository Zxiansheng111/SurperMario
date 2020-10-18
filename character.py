import pygame

class Character:
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        self.character = pygame.image.load("maliao.png")
        self.character = pygame.transform.scale(self.character, (ai_settings.character_width, ai_settings.character_high))
        self.rect = self.character.get_rect()
        self.mask = pygame.mask.from_surface(self.character)

        self.rect.left = 0
        self.rect.top = ai_settings.screen_high - ai_settings.character_high

    def character_move(self):
        if self.rect.left <= 0 and self.ai_settings.characterx < 0:     #防止马里奥超出左右边界
            self.ai_settings.characterx = 0
        elif self.rect.right >= self.ai_settings.screen_width and self.ai_settings.characterx > 0:
            self.ai_settings.characterx = 0

        self.rect = self.rect.move(self.ai_settings.characterx, self.ai_settings.gv)  # 马里奥左右移动

        if self.rect.bottom >= self.ai_settings.screen_high:  # 马里奥落地后下降速度为0
            self.ai_settings.gv = 0

        if self.ai_settings.character_jumping:  # 判定马里奥是否在跳跃状态
            self.ai_settings.charactery += 1
            self.rect = self.rect.move(0, self.ai_settings.charactery)
            if self.rect.bottom >= self.ai_settings.screen_high:  # 如果落地 重置long_jumping
                self.ai_settings.charactery = 0
                self.ai_settings.character_jumping = False

    def blit_character(self):
        self.screen.blit(self.character, self.rect)