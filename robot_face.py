import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
finished = False

eyes = 10
eyes_up = 10
pupil_sz = 20

key_a_down = False
key_d_down = False

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key_a_down = False
            elif event.key == pygame.K_d:
                key_d_down = False

    if key_a_down:
        eyes -= 3
        if eyes < 5: eyes = 5

    if key_d_down:
        eyes += 3
        if eyes > 25: eyes = 25

    sys.stdout.write('%d %d\r' % (eyes, eyes_up))
    sys.stdout.flush()

    if finished:
        break

    # Redraw the background
    screen.fill(pygame.Color(0, 0, 0, 255))

    pygame.draw.rect(screen, pygame.Color('red'), (50, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('black'), (50 + eyes, 50 + eyes_up, pupil_sz, pupil_sz))
    pygame.draw.rect(screen, pygame.Color('red'), (700, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('black'), (700 + eyes, 50 + eyes_up, pupil_sz, pupil_sz))

    pygame.display.flip()
