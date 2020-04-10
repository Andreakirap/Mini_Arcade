import pygame
pygame.init()

def menu(screen):
        font = pygame.font.Font("font/pixelart.ttf",45)
        text = font.render("SPACE INVADERS",True,(255,255,255))
        textRect = pygame.Rect((165,200),(0,0))
        screen.blit(text,textRect)
