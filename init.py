import pygame
import os

pygame.font.init()
pygame.mixer.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
#font1 = pygame.font.SysFont("comicsans", 30, True)
textheight=50

font1 = pygame.font.Font(resource_path('Assets/freesansbold.ttf'), textheight)

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RoadLite")
SPACE=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', "space2.jpeg")),(WIDTH, HEIGHT)), 0)

class character():
    def __init__ (self, x,y, width, height, health, model):
        #self.health0=health
        self.x = x
        self.y = y
        self.width = width
        self.health0=health
        self.height = height
        self.health=health
        pic = pygame.image.load(
            os.path.join('Assets', model))
        self.model = pygame.transform.rotate(pygame.transform.scale(pic,(width, height)), 0)
    def drawChar(self):
        WIN.blit(self.model,(self.x,self.y))
        pygame.draw.rect(WIN, (255,0,0), (self.x, self.y - 30, self.width, 10))
        pygame.draw.rect(WIN, (0,128,0), (self.x, self.y - 30, self.width*self.health/self.health0, 10))
    def attack(self):
        xattack=self.x+100
        WIN.blit(self.model,(xattack,self.y))
        pygame.draw.rect(WIN, (255,0,0), (self.x, self.y - 30, self.width, 10))
        pygame.draw.rect(WIN, (0,128,0), (self.x, self.y - 30, self.width*self.health/self.health0, 10))

class popupmenu():
    def __init__ (self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.Rect=pygame.Rect(self.x,self.y,self.width,self.height)

    def make_popup(self):
        offsetval=0
        popupSurf = pygame.Surface((self.width, self.height))
        #popupSurf.fill(RED)
        options = ['Attack',
                   'Talk']
        for i in range(len(options)):
            textSurf = font1.render(options[i], 1, WHITE)
            textRect = textSurf.get_rect()
            textRect.top = offsetval#self.y
            textRect.left = 0#self.x
            #self.y += pygame.font.Font.get_linesize(font1)
            offsetval += pygame.font.Font.get_linesize(font1)
            popupSurf.blit(textSurf, textRect)
        popupRect = popupSurf.get_rect()
        popupRect.x = self.x
        popupRect.y = self.y
        WIN.blit(popupSurf, popupRect)
        #pygame.display.update()
    
    def option_selected(self):
        popupSurf = pygame.Surface((self.width, self.height))
        options = ['Attack',
                   'Talk']
        #offsetval=-2*len(options)*pygame.font.Font.get_linesize(font1)
        offsetval=0
        popupRect = popupSurf.get_rect()
        popupRect.x = self.x
        popupRect.y = self.y
        #self.y -= 2*pygame.font.Font.get_linesize(font1) #to account for two options offsetting y above in popupmenu()
        for i in range(len(options)):
            textSurf = font1.render(options[i], 1, WHITE)
            textRect = textSurf.get_rect()
            textRect.top = offsetval+self.y#self.y+popupRect.y
            textRect.left = 0+self.x#self.x+popupRect.x
            offsetval += pygame.font.Font.get_linesize(font1)
            #self.y += pygame.font.Font.get_linesize(font1)
            mousex,mousey=pygame.mouse.get_pos() 
            if textRect.collidepoint(mousex, mousey):
                return options[i]

