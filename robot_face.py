import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
finished = False

eyes = 10
eyes_up = 10
pupil_sz = 10

key_a_down = False
key_d_down = False
key_w_down = False
key_s_down = False

while True:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key_a_down = True
            elif event.key == pygame.K_d:
                key_d_down = True
            elif event.key == pygame.K_w:
                key_w_down = True
            elif event.key == pygame.K_s:
                key_s_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key_a_down = False
            elif event.key == pygame.K_d:
                key_d_down = False
            elif event.key == pygame.K_w:
                key_w_down = False
            elif event.key == pygame.K_s:
                key_s_down = False

    if key_a_down:
        eyes -= 3
        if eyes < 0: eyes = 0

    if key_d_down:
        eyes += 3
        if eyes > 40: eyes = 40

    if key_s_down:
        eyes_up += 3
        if eyes_up > 40: eyes_up = 40

    if key_w_down:
        eyes_up -= 3
        if eyes_up < 0: eyes_up = 0

    if finished:
        break

    # Redraw the background
    screen.fill(pygame.Color('grey'))

    pygame.draw.rect(screen, pygame.Color('white'), (50, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('white'), (700, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('brown'), (700 + eyes, 50 + eyes_up, pupil_sz, pupil_sz))
    pygame.draw.rect(screen, pygame.Color('brown'), (50 + eyes, 50 + eyes_up, pupil_sz, pupil_sz))
    pygame.draw.rect(screen, pygame.Color('pink'), (50, 600, 700, 100))
    pygame.draw.rect(screen, pygame.Color(120, 120, 120), (350, 350, 100, 100))

    pygame.display.flip()
