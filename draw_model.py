import pygame, model

line_rects = []

selected_line_num = None
increase_shoot_speed_rect = None
increase_shoot_power_rect = None
increase_shoot_count_rect = None
increase_gun_level_rect = None

new_gun_rect = pygame.Rect(50, 10, 20, 20)


def make_lines(screen):
    line_rects.clear()
    starty = 60

    # pygame.draw.rect(screen, [255, 255, 255], [50, starty, 800, 480])

    line_height = (600 - 120) / len(model.guns)
    if line_height > 80:
        line_height = 80

    for i in model.guns:
        r = pygame.Rect(50, starty, 800, line_height)
        # pygame.draw.rect(screen, [255, 7, 89], r)

        r2 = pygame.Rect(50, starty + 5, 800, line_height - 10)
        # pygame.draw.rect(screen, [12, 255, 89], r2)
        starty += line_height

        line_rects.append(r2)


def make_upgrade_rects(screen):
    global increase_shoot_speed_rect, increase_shoot_power_rect, increase_shoot_count_rect, increase_gun_level_rect

    if selected_line_num == None:
        increase_shoot_power_rect = None
        increase_shoot_count_rect = None
        increase_shoot_speed_rect = None
        increase_gun_level_rect = None
        return

    rect = line_rects[selected_line_num]
    top = rect.top

    button_size = 30

    increase_shoot_speed_rect = pygame.Rect(155 - button_size, top - button_size, button_size, button_size)
    # pygame.draw.rect(screen, [255, 0, 0], increase_shoot_speed_rect)

    increase_shoot_power_rect = pygame.Rect(155 - 2*button_size-5, top - button_size, button_size, button_size)
    # pygame.draw.rect(screen, [255, 0, 0], increase_shoot_power_rect)

    increase_shoot_count_rect = pygame.Rect(155 - 3*button_size-10, top - button_size, button_size, button_size)
    # pygame.draw.rect(screen, [255, 0, 0], increase_shoot_count_rect)

    increase_gun_level_rect = pygame.Rect(rect.left, rect.top , 155-rect.left, rect.height)
    # pygame.draw.rect(screen, [123, 45, 255], increase_gun_level_rect)


def click_button(x, y):
    global selected_line_num

    if increase_shoot_count_rect is not None and increase_shoot_count_rect.collidepoint(x, y):
        model.buy_shot_count(selected_line_num)
        return

    if increase_shoot_speed_rect is not None and increase_shoot_speed_rect.collidepoint(x, y):
        model.buy_shot_speed(selected_line_num)
        return

    if increase_shoot_power_rect is not None and increase_shoot_power_rect.collidepoint(x, y):
        model.buy_shot_power(selected_line_num)
        return

    if increase_gun_level_rect is not None and increase_gun_level_rect.collidepoint(x, y):
        model.buy_gun_level(selected_line_num)
        return

    num = 0
    for i in line_rects:
        if i.collidepoint(x, y):
            selected_line_num = num
            return
        num+=1

    selected_line_num = None

    if new_gun_rect.collidepoint(x, y):
        model.add_gun()
        return

    print(selected_line_num)