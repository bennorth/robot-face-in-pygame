import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
finished = False

pupil_x = 10
pupil_y = 10
pupil_sz = 20

while True:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    if finished:
        break

    # Redraw the background
    screen.fill(pygame.Color(0, 0, 0, 255))

    pygame.draw.rect(screen, pygame.Color('red'), (50, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('black'), (50 + pupil_x, 50 + pupil_y, pupil_sz, pupil_sz))
    pygame.draw.rect(screen, pygame.Color('red'), (700, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('black'), (700 + pupil_x, 50 + pupil_y, pupil_sz, pupil_sz))

    pygame.display.flip()
