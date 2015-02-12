
import pygame
key_a_down = False
key_d_down = False
key_s_down = False
key_w_down = False
key_UP_down = False
key_DOWN_down = False
key_RIGHT_down = False
key_LEFT_down = False
key_SPACE_down = False
tear_fall = False
tear_Y = 0
mouth_wide = 700
mouth_hight = 75
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
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:finshed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key_a_down = True
            if event.key == pygame.K_d:
                key_d_down = True
            if event.key == pygame.K_s:
                key_s_down = True
            if event.key == pygame.K_w:
                key_w_down = True
            if event.key == pygame.K_UP:
                key_UP_down = True
            if event.key == pygame.K_DOWN:
                key_DOWN_down = True
            if event.key == pygame.K_RIGHT:
                key_RIGHT_down = True
            if event.key == pygame.K_LEFT:
                key_LEFT_down = True
            if event.key == pygame.K_SPACE:
                key_SPACE_down = True
            if event.key == pygame.K_t:
                speak = 'WAA(cry)'
                if not tear_fall:
                    tear_fall = True
                    tear_Y = 100
            if event.key == pygame.K_h:
                speak = 'hello'
            if event.key == pygame.K_z:
                speak = 'My'
            if event.key == pygame.K_x:
                speak = 'name'
            if event.key == pygame.K_c:
                speak = 'is'
            if event.key == pygame.K_v:
                speak = 'John'
            if event.key == pygame.K_b:
                speak = 'Paul'
            if event.key == pygame.K_n:
                speak = 'Sparki'
            if event.key == pygame.K_y:
                disabled = True
            if event.key == pygame.K_RETURN:
                disabled = False
                pass


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key_a_down = False
            if event.key == pygame.K_d:
                key_d_down = False
            if event.key == pygame.K_s:
                key_s_down = False
            if event.key == pygame.K_w:
                key_w_down = False
            if event.key == pygame.K_UP:
                key_UP_down = False
            if event.key == pygame.K_DOWN:
                key_DOWN_down = False
            if event.key == pygame.K_RIGHT:
                key_RIGHT_down = False
            if event.key == pygame.K_LEFT:
                key_LEFT_down = False
            if event.key == pygame.K_SPACE:
                key_SPACE_down = False
            if event.key in [pygame.K_h, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n, pygame.K_t]:
                speak = ''

    if key_a_down:
        eyes -=3
    if eyes < 0: eyes = 0

    if key_d_down:
        eyes +=3
    if eyes > 40: eyes = 40

    if key_s_down:
        eyes_up +=3
    if eyes_up >40: eyes_up = 40

    if key_w_down:
        eyes_up -=3
    if eyes_up < 0: eyes_up = 0

    if key_DOWN_down:
        mouth_hight +=10
    if mouth_hight > 120: mouth_hight = 120

    if key_UP_down:
        mouth_hight -=10
    if mouth_hight < 5: mouth_hight = 5

    if key_LEFT_down:
        mouth_wide +=10
    if mouth_wide > 700: mouth_wide = 700

    if key_RIGHT_down:
        mouth_wide -=10
    if mouth_wide < 45: mouth_wide = 45

    total_space = 800 - mouth_wide
    mouth_space = total_space / 2

    if tear_fall:
        tear_Y += 5
        if tear_Y > 480:
            tear_fall = False

    if key_SPACE_down:
        mouth_hight -=10
    if mouth_hight < 5: mouth_hight = 5

    if key_LEFT_down:
        mouth_wide +=10
    if mouth_wide > 700: mouth_wide = 700

    if key_RIGHT_down:
        mouth_wide -=10
    if mouth_wide < 45: mouth_wide = 45

    total_space = 800 - mouth_wide
    mouth_space = total_space / 2

    if tear_fall:
        tear_Y += 5
        if tear_Y > 480:
            tear_fall = False

    screen.fill(pygame.Color('grey'))
    pygame.draw.rect(screen, pygame.Color('white'), (50, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('white'), (700, 50, 50, 50))
    pygame.draw.rect(screen, pygame.Color('brown'), (700 + eyes,50 + eyes_up, 10, 10))
    pygame.draw.rect(screen, pygame.Color('brown'), (50 + eyes, 50 + eyes_up, 10,10))
    pygame.draw.rect(screen, pygame.Color('pink'), (mouth_space, 450, mouth_wide, 100 + mouth_hight))
    if key_SPACE_down:
        pygame.draw.circle(screen, pygame.Color('green'), (380,400),20)
    pygame.draw.rect(screen, pygame.Color(120,120,120),(350,300,100,100 ))
    if tear_fall:
        pygame.draw.circle(screen, pygame.Color(120,120,255), (100, tear_Y), 15)
        pygame.draw.circle(screen, pygame.Color(120,120,255), (700, tear_Y), 15)

    speech = myfont.render(speak, 1, (255,0,0))
    screen.blit(speech, (377, 535))

    pygame.display.flip()


