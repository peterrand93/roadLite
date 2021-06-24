import pygame
import os
import init

from pygame.constants import MOUSEBUTTONUP
clock = pygame.time.Clock()

pygame.font.init()
pygame.mixer.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS=15
#font1 = pygame.font.Font('Assets/freesansbold.ttf', textheight)

WIDTH, HEIGHT = 1000, 600
width, height = 500, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RoadLite")
sc1x0=150


HEALTH_LOSS = pygame.USEREVENT + 1

def redrawGameWindow():
    init.WIN.blit(init.SPACE, (0,0))
    sc1.drawChar()
    sc2.drawChar()
    attackmenu.make_popup()
    pygame.display.update()

sc1=init.character(sc1x0,400,100,100,20,"Scorpion.png")#.drawChar()     
sc2=init.character(650,100,200,200,10,"Scorpion.png")#.drawChar()  

clock = pygame.time.Clock()
run = True

run=True
while run:
    OPTION=''
    clock.tick(FPS)
    attackmenu = init.popupmenu(50,100,200,init.textheight*2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.QUIT
        if event.type == pygame.MOUSEBUTTONUP:
            OPTION = attackmenu.option_selected()
    #keys_pressed = pygame.key.get_pressed()
    #if keys_pressed[pygame.K_SPACE]:  
    #    pygame.event.post(pygame.event.Event(HEALTH_LOSS))
    if OPTION == 'Attack':
        sc1.x=sc1x0+100
        if sc2.health > 1:
            sc2.health-=1
    else:
        sc1.x=sc1x0

    redrawGameWindow()
