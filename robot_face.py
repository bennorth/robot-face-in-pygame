import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.draw.rect(screen, pygame.Color('red'), (50, 50, 50, 50))
pygame.draw.rect(screen, pygame.Color('red'), (700, 50, 50, 50))

pygame.display.flip()
