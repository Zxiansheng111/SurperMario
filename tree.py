import pygame

class Tree():
    def __init__(self,ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen

        self.tree = pygame.image.load("shirenhua.png")  # 设置食人花的参数
        self.tree = pygame.transform.scale(self.tree, (self.ai_settings.tree_width, self.ai_settings.tree_high))
        self.rect = self.tree.get_rect()
        self.mask = pygame.mask.from_surface(self.tree)

        self.rect.left = self.ai_settings.screen_width - self.ai_settings.tree_width
        self.rect.top = self.ai_settings.screen_high - self.ai_settings.tree_high

    def tree_move(self, character):
        if self.rect.left <= 0:  # 控制食人花 使其一直在屏幕内运动
            self.rect.left += self.ai_settings.screen_width - self.ai_settings.tree_width
            self.ai_settings.tree_once = True
        else:
            self.rect.left -= self.ai_settings.tree_x

        if self.ai_settings.tree_f == 500:  # 控制树加速频率
            self.ai_settings.tree_x += 1
        self.ai_settings.tree_f += 1
        if self.ai_settings.tree_f > 500:
            self.ai_settings.tree_f = 0

        if self.rect.right <= character.rect.left and self.ai_settings.character_jumping and self.ai_settings.tree_once == True:
            self.ai_settings.score += self.ai_settings.num
            self.ai_settings.num = 0
            self.ai_settings.tree_once = False
        if not self.ai_settings.character_jumping:
            self.ai_settings.num = 1

    def blit_tree(self):
        self.screen.blit(self.tree, self.rect)  # 树