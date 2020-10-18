import pygame
import sys
from coin import Coin
from character import Character
from tree import Tree
from esettings import Esettings
ai_settings = Esettings()

screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_high))
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("超级玛丽！")
background = pygame.image.load("background1.jpg")
background = pygame.transform.scale(background, (ai_settings.screen_width, ai_settings.screen_high))

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
yellow=(255,215,0)
bright_yellow=(255,255,0)

display_width = 800
display_height = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

character = Character(ai_settings, screen)
tree = Tree(ai_settings, screen)
coin = Coin(ai_settings, screen)




def check_keydown_events(event, ai_settings):
    global pause
    if event.key == pygame.K_UP:
        if not ai_settings.character_jumping:
            ai_settings.charactery = -30
            ai_settings.character_jumping = True

    elif event.key == pygame.K_LEFT:
            ai_settings.characterx = -5
    elif event.key == pygame.K_RIGHT:
            ai_settings.characterx = 5
    elif event.key == pygame.K_SPACE:
            pause = True
            paused()

def check_keyup_events(event, ai_settings):
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        ai_settings.characterx = 0


def check_events(ai_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings)


def all_move(character, tree, coin):
    character.character_move()
    tree.tree_move(character)
    coin.update_coin()


def crash_test(character, tree, coin, ai_settings):
    if pygame.sprite.collide_mask(character, tree):
        ai_settings.fclock.tick(30)
        over()
        pygame.display.update()
    elif pygame.sprite.collide_mask(character, coin):
        coin.rect.left = ai_settings.screen_width + 1
        coin.rect.top = ai_settings.screen_high + 1
        ai_settings.score += 1
        ai_settings.tree_x -= 1


def screen_update(character, tree, coin, screen, background, ai_settings):
    screen.blit(background, (0, 0))  # 更新背景
    tree.blit_tree()
    character.blit_character()
    coin.blit_coin()
    screen.blit(ai_settings.game_font.render('SCORE: %d  ' % ai_settings.score, True, [255, 255, 255]), [300, 20])
    screen.blit(ai_settings.game_font.render('SPEED: %d  ' % ai_settings.tree_x, True, [255, 255, 255]), [450, 20])
    pygame.display.update()
    ai_settings.fclock.tick(ai_settings.fps)

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def quitgame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac, action=None):#按键函数
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():#初始界面
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        character_png= pygame.image.load("background3.jpg")
        character_png = pygame.transform.scale(character_png, (1200,600))
        screen.blit(character_png, (0, 0))
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('SUPER MARIO', largeText)
        TextRect.center = (600, 50)
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont('comicsansms', 40)
        button("Begin", 200, 500, 100, 50, green, bright_green, game_loop)
        button("Quit", 800, 500, 100, 50, red, bright_red, quitgame)
        button("Help", 500, 500, 100, 50, yellow, bright_yellow, help)
        pygame.display.update()
        clock.tick(15)


def help():#介绍界面
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        largeText = pygame.font.SysFont('comicsansms', 40)
        TextSurf, TextRect = text_objects('MOVE:left&right      Jump:up       Pause:space', largeText)
        TextRect.center = (400, 100)
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont('comicsansms', 25)
        TextSurf, TextRect = text_objects('Editor:   Zhuwenhao', largeText)
        TextRect.center = (400, 200)
        gameDisplay.blit(TextSurf, TextRect)
        button("Back", 350, 300, 100, 50, green, bright_green, game_intro)
        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause = False


def paused():#暂停界面
    global pause
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects('Paused', largeText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue", 150, 275, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 275, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)


def over():#游戏结束界面

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        character_png= pygame.image.load("background4.jpg")
        character_png = pygame.transform.scale(character_png, (1200,600))
        screen.blit(character_png, (0, 0))

        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('Game Over', largeText)
        #TextRect.center = ((display_width / 2), 60)
        TextRect.center = (600, 60)
        gameDisplay.blit(TextSurf, TextRect)
        button("Quit", 600, 450, 100, 50,red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)


def game_loop():#主循环
    while True:
        check_events(ai_settings)
        all_move(character, tree, coin)
        crash_test(character, tree, coin, ai_settings)
        screen_update(character, tree, coin, screen, background, ai_settings)