import pygame
import menu

pygame.init()

screen1 = pygame.display.set_mode((800,600))

while True:
    screen1.fill((0,0,0))
    menu.menu(screen1)
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

