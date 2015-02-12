
import pygame
tear_fall = False
tear_Y = 0
mouth_wide = 700
mouth_height = 75
speak = ''
disabled = False
#0 = full left and 40 = full right
eyes_up = 0
eyes = 0
finished = False

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        #
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                if not tear_fall:
                    tear_fall = True
                    tear_Y = 100
            if event.key == pygame.K_y:
                disabled = True
            if event.key == pygame.K_RETURN:
                disabled = False
                pass

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        eyes -=3
    if eyes < 0: eyes = 0

    if keys[pygame.K_d]:
        eyes +=3
    if eyes > 40: eyes = 40

    if keys[pygame.K_s]:
        eyes_up +=3
    if eyes_up >40: eyes_up = 40

    if keys[pygame.K_w]:
        eyes_up -=3
    if eyes_up < 0: eyes_up = 0

    if keys[pygame.K_DOWN]:
        mouth_height +=10
    if mouth_height > 120: mouth_height = 120

    if keys[pygame.K_UP]:
        mouth_height -=10
    if mouth_height < 5: mouth_height = 5

    if keys[pygame.K_LEFT]:
        mouth_wide +=10
    if mouth_wide > 700: mouth_wide = 700

    if keys[pygame.K_RIGHT]:
        mouth_wide -=10
    if mouth_wide < 45: mouth_wide = 45

    if keys[pygame.K_t]:
        speak = 'WAA(cry)'
    elif keys[pygame.K_h]:
        speak = 'hello'
    elif keys[pygame.K_z]:
        speak = 'My'
    elif keys[pygame.K_x]:
        speak = 'name'
    elif keys[pygame.K_c]:
        speak = 'is'
    elif keys[pygame.K_v]:
        speak = 'John'
    elif keys[pygame.K_b]:
        speak = 'Paul'
    elif keys[pygame.K_n]:
        speak = 'Sparki'
    else:
        speak = ''

    if tear_fall:
        tear_Y += 5
        if tear_Y > 480:
            tear_fall = False

    screen.fill(pygame.Color('grey'))

    pygame.draw.rect(screen, pygame.Color('white'), (50, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('white'), (700, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('brown'), (700 + eyes, 50 + eyes_up, 10, 10))
    pygame.draw.rect(screen, pygame.Color('brown'), (50 + eyes, 50 + eyes_up, 10, 10))

    total_space = 800 - mouth_wide
    mouth_space = total_space / 2

    pygame.draw.rect(screen, pygame.Color('pink'), (mouth_space, 450,
                                                    mouth_wide, 100 + mouth_height))
    if keys[pygame.K_SPACE]:
        pygame.draw.circle(screen, pygame.Color('green'), (380, 400), 20)

    pygame.draw.rect(screen, pygame.Color(120, 120, 120), (350, 300, 100, 100))

    if tear_fall:
        pygame.draw.circle(screen, pygame.Color(120, 120, 255), (100, tear_Y), 15)
        pygame.draw.circle(screen, pygame.Color(120, 120, 255), (700, tear_Y), 15)

    speech = myfont.render(speak, 1, (255, 0, 0))
    screen.blit(speech, (377, 535))

    pygame.display.flip()


