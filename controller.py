import pygame

import model

TIMER_BRICK = pygame.event.custom_type()
pygame.time.set_timer(TIMER_BRICK, 1000)

TIMER_WAVE = pygame.event.custom_type()
pygame.time.set_timer(TIMER_WAVE, 1000)

def process_events():
    evs = pygame.event.get()
    for e in evs:
        if e.type == pygame.QUIT:
            exit()

        if e.type==TIMER_BRICK:
            model.make_bricks()

        if e.type==TIMER_WAVE:
            model.brick_points_per_second+=1