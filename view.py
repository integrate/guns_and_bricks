import pygame, settings

import model


def draw():
    screen.fill([0, 0, 0])

    # draw guns
    starty = 60
    # pygame.draw.rect(screen, [255, 255, 255], [50, starty, 800, 480])

    line_height = (600 - 120) / len(model.guns)
    if line_height>80:
        line_height=80
    line_rects = []
    for i in model.guns:
        r = pygame.Rect(50, starty, 800, line_height)
        # pygame.draw.rect(screen, [255, 7, 89], r)

        r2 = pygame.Rect(50, starty+5, 800, line_height-10)
        # pygame.draw.rect(screen, [12, 255, 89], r2)
        starty+=line_height

        line_rects.append(r2)

    pygame.draw.line(screen, [0, 0, 255], [155, 0], [155, 600])

    i = 0
    for gun in model.guns:
        draw_gun(gun, line_rects[i])
        i+=1



    # draw bullets
    i=0
    for bul_line in model.bullet_lines:
        for bul in bul_line:
            draw_bul(bul, line_rects[i])
        i+=1

    # draw bricks
    i=0
    for brick_line in model.brick_lines:
        for brick in brick_line:
            draw_brick(brick, line_rects[i])
        i+=1

    if model.game_over:
        screen.blit(game_over_pic, [450-game_over_pic.get_width()/2, 300-game_over_pic.get_height()/2])

    pygame.display.flip()


def draw_gun(gun, rect):
    pic = get_gun_pic(gun["level"])

    height = rect.height
    width = pic.get_width() * height / pic.get_height()

    pic = pygame.transform.scale(pic, [width, height])
    screen.blit(pic, [155-width, rect.top])
    # pygame.draw.rect(screen, [255, 255, 255], rect, 1)


def draw_bul(bul, line_rect):
    pygame.draw.ellipse(screen, [125, 14, 234], [bul['x'], line_rect.centery - 3, bul["power"] * 3, 6],
                        bul["power"] * 2)


def draw_brick(brick, line_rect):
    pic = get_brick_pic(brick['level'])

    height = line_rect.height
    width = pic.get_width() * height / pic.get_height()

    pic = pygame.transform.scale(pic, [width, height])
    screen.blit(pic, [brick['x'], line_rect.top])

    hp = font.render(str(brick["hp"]), True, [255, 0, 0], [0, 0, 0])
    screen.blit(hp, [brick['x']+2, line_rect.top+2])



def load_gun(number):
    gunpic = pygame.image.load("images/space_gun" + str(number) + ".png")
    gunpic = pygame.transform.flip(gunpic, True, False)
    return gunpic


def load_brick(number):
    pic = pygame.image.load("images/brick" + str(number) + ".png")
    return pic


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


def get_brick_pic(level):
    if level == 1:
        return brickpic1
    if level == 2:
        return brickpic2
    if level == 3:
        return brickpic3
    if level == 4:
        return brickpic4

pygame.init()

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
gunpic1 = load_gun(1)
gunpic2 = load_gun(2)
gunpic3 = load_gun(3)
gunpic4 = load_gun(4)
gunpic5 = load_gun(5)
gunpic6 = load_gun(6)
gunpic7 = load_gun(7)
gunpic8 = load_gun(8)

brickpic1 = load_brick(1)
brickpic2 = load_brick(2)
brickpic3 = load_brick(3)
brickpic4 = load_brick(4)

print(pygame.font.get_fonts())
font = pygame.font.SysFont("arial", 12, True)
font_game_over = pygame.font.SysFont("comicsansms", 140, True)
game_over_pic = font_game_over.render("GAME OVER", True, [255, 10, 10])