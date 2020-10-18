import pygame

pygame.init()

class Esettings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_high = 600
        self.character_width = 120
        self.character_high = 120
        self.characterx = 0
        self.charactery = 0
        self.gv = 1
        self.tree_width = 150
        self.tree_high = 300
        self.tree_x = 5
        self.tree_f = 0
        self.coin_size = 80
        self.coin_f = 0
        self.fps = 70
        self.character_jumping = False
        self.score = 0
        self.fclock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont('宋体', 32, True)
        self.num = 1
        self.tree_once=True