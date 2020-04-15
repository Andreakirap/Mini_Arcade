import pygame

pygame.init()

screen1 = pygame.display.set_mode((800,600))

FONT = pygame.font.Font("font/pixelart.ttf",40)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
x = 1
y = 1
enemy_img = pygame.image.load('sprites/enemy1_1.png')

class Player():
    def __init__(self):
        self.x = 400
        self.y = 60
        self.img = pygame.image.load('sprites/enemy1_1.png')
    def movement(self,key):
        if key == 100:
            self.x += 10
                         
    

def drawtext(text,x,y,screen):
    text = FONT.render(text,True,WHITE)
    textRect = pygame.Rect((x,y),(0,0))
    screen.blit(text,textRect)

def menu():
    while True:
        drawtext("Space invaders",200,120,screen1)
        drawtext("Press any key to continue",70,180,screen1)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == 2:
                return 0
            elif e.type == pygame.QUIT:
                quit()
                
menu()
player = Player()
while True:
    screen1.fill((0,0,0))
    screen1.blit(player.img,(player.x,player.y))
    pygame.display.update()
   
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == 100:
                player.movement(e.key)

