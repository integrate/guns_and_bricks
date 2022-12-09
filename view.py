import pygame, settings

import model


def draw():
    screen.fill([0, 0, 0])

    # draw guns
    start = 60
    height = (600 - 120) / len(model.guns)
    for gun in model.guns:
        draw_gun(gun, pygame.Rect(50, start + 5, 100, height - 10))
        start += height

    pygame.draw.line(screen, [255, 0, 0], [155, 0], [155, 600])

    start = 60
    for bul_line in model.bullet_lines:
        for bul in bul_line:
            draw_bul(bul, start+height/2)
        start+=height

    pygame.display.flip()


def draw_gun(gun, rect):
    pic = get_gun_pic(gun["level"])

    height = rect.height
    width = pic.get_width() * height / pic.get_height()

    pic = pygame.transform.scale(pic, [width, height])
    screen.blit(pic, [rect.right - width, rect.top])
    # pygame.draw.rect(screen, [255, 255, 255], rect, 1)


def load_gun(number):
    gunpic = pygame.image.load("images/space_gun" + str(number) + ".png")
    gunpic = pygame.transform.flip(gunpic, True, False)
    return gunpic


def get_gun_pic(level):
    if level == 1:
        return gunpic1
    if level == 2:
        return gunpic2
    if level == 3:
        return gunpic3
    if level == 4:
        return gunpic4
    if level == 5:
        return gunpic5
    if level == 6:
        return gunpic6
    if level == 7:
        return gunpic7
    if level == 8:
        return gunpic8

def draw_bul(bul, line_height):
    pygame.draw.ellipse(screen, [125, 14, 234], [150+bul['x'], line_height-3, bul["power"]*3, 6], bul["power"]*2)

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
gunpic1 = load_gun(1)
gunpic2 = load_gun(2)
gunpic3 = load_gun(3)
gunpic4 = load_gun(4)
gunpic5 = load_gun(5)
gunpic6 = load_gun(6)
gunpic7 = load_gun(7)
gunpic8 = load_gun(8)
