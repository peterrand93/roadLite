import pygame
import os
import random
clock = pygame.time.Clock()

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
BLUE = (0, 0, 255)

textheight=35

font1 = pygame.font.Font(resource_path('Assets/freesansbold.ttf'), textheight)
font2 = pygame.font.Font(resource_path('Assets/ManuskriptGothischUNZ1A.ttf'), textheight)
font3 = pygame.font.Font(resource_path('Assets/freesansbold.ttf'), int(round(textheight/2)))


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RoadLite")
background=pygame.transform.rotate(pygame.transform.smoothscale(pygame.image.load(
            os.path.join('Assets', "flyingKitchen-01.png")),(WIDTH, HEIGHT)), 0)

def redrawGameWindow(characters,cards,endTurn,manaPop):
    WIN.blit(background, (0,0))
    if characters[0].stunned==True:
        WIN.blit(font1.render("stunned!", 1, BLACK),(75,150))
    if characters[1].stunned==True:
        WIN.blit(font1.render("stunned!", 1, BLACK),(725,25))
    for i in range(len(characters)):
        characters[i].drawChar()
    #attackmenu.make_popup()
    endTurn.make_popup()
    manaPop.make_popup()
    for i in range(len(cards)):
        cards[i].cardDraw()
    #manaleft = font1.render(str(mana), 1, BLACK)
    #pygame.draw.circle(WIN, BLUE, (100,525), 20)
    #WIN.blit(manaleft,(100,525))
    pygame.display.update()

def drawGameover(text,click):
    endScreen=pygame.Surface((WIDTH,HEIGHT))
    endScreen.fill(BLACK)
    #endScreen=pygame.Rect(0,0,WIDTH,HEIGHT)
    textSurf = font1.render(text, 1, WHITE)
    ScreenRect = endScreen.get_rect()
    textRect=textSurf.get_rect()
    retry=font1.render("Retry?",1,WHITE)
    retryRect=retry.get_rect()
    retryRect.top=ScreenRect.centery-retryRect.height/2+50
    retryRect.left=ScreenRect.centerx-retryRect.width/2
    #textRect.left=0
    WIN.blit(endScreen, (0,0))
    WIN.blit(textSurf,(ScreenRect.centerx-textRect.width/2,ScreenRect.centery-textRect.height/2))
    WIN.blit(retry,(ScreenRect.centerx-retryRect.width/2,ScreenRect.centery-retryRect.height/2+50))
    mousex,mousey=pygame.mouse.get_pos() 
    if retryRect.collidepoint(mousex, mousey):
        retry=font1.render("Retry?",1,RED)
        WIN.blit(retry,(ScreenRect.centerx-retryRect.width/2,ScreenRect.centery-retryRect.height/2+50))
        if click:
                retryOpt=True
                return retryOpt
            #else:
                #retryOpt=False
            
        #return options[i]
    pygame.display.update()

class character():
    def __init__ (self, x,y, width, height, health, attack, reflect, stunned, model):
        self.stunned=stunned
        self.attack=attack
        self.attack0=attack
        self.x = x
        self.y = y
        self.width = width
        self.health0 = health
        self.height = height
        self.health = health
        self.reflect = reflect
        pic = pygame.image.load(
            os.path.join('Assets', model)).convert_alpha()
        self.model = pygame.transform.rotate(pygame.transform.smoothscale(pic,(width, height)), 0)
    def drawChar(self):
        WIN.blit(self.model,(self.x,self.y))
        pygame.draw.rect(WIN, (0,0,0), (self.x-3, self.y - 33, self.width+6, 16))
        pygame.draw.rect(WIN, (255,0,0), (self.x, self.y - 30, self.width, 10))
        if self.health>0:
            pygame.draw.rect(WIN, (0,128,0), (self.x, self.y - 30, self.width*self.health/self.health0, 10))


class popupmenu():
    def __init__ (self, x,y, width, height,text, BG):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text=text
        self.BG = BG

    def make_popup(self):
        offsetval=0
        popupSurf = pygame.Surface((self.width, self.height),pygame.SRCALPHA)
        SCROLL=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', self.BG)),(self.width+25, self.height+25)), 0)
       # SCROLL=pygame.Surface()
        #options = ['Attack',
        #           'Defend',
        #           'Special',
        #           'Run']
        options=self.text
        for i in range(len(options)):
            textSurf = font1.render(options[i], 1, BLACK)
            textRect = textSurf.get_rect()
            textRect.top = offsetval#self.y
            textRect.left = 0#self.x
            mousex,mousey=pygame.mouse.get_pos() 
            if textRect.collidepoint(mousex-self.x, mousey-self.y):
                textSurf = font1.render(options[i], 1, RED)
            offsetval += pygame.font.Font.get_linesize(font2)
            popupSurf.blit(textSurf, textRect)
        popupRect = popupSurf.get_rect()
        popupRect.x = self.x
        popupRect.y = self.y
        WIN.blit(SCROLL,(self.x-12.5,self.y-12.5))
        WIN.blit(popupSurf, popupRect)
    
    def option_selected(self):
        popupSurf = pygame.Surface((self.width, self.height))
        #options = ['Attack',
        #           'Defend',
        #           'Special',
        #           'Run']
        options=self.text
        offsetval=0
        popupRect = popupSurf.get_rect()
        popupRect.x = self.x
        popupRect.y = self.y
        for i in range(len(options)):
            textSurf = font2.render(options[i], 1, RED)
            textRect = textSurf.get_rect()
            textRect.top = offsetval+self.y#self.y+popupRect.y
            textRect.left = 0+self.x#self.x+popupRect.x
            offsetval += pygame.font.Font.get_linesize(font2)
            mousex,mousey=pygame.mouse.get_pos() 
            if textRect.collidepoint(mousex, mousey):
                return options[i]

class card():
    def __init__ (self, x,y, width, height,image):
        self.x = x
        self.y0=y
        self.x0=x
        self.y = y
        self.width = width
        self.height = height
        self.width0 = width
        self.height0 = height
        self.image=image


    def cardDraw(self):
        path='Assets/cards/finishedcards/'
        path+=self.image
        cardSurf0=pygame.transform.rotate(pygame.transform.smoothscale(pygame.image.load(
            resource_path(path)).convert_alpha(),(self.width0, self.height0)), 0)
        cardSurf = pygame.transform.rotate(pygame.transform.smoothscale(pygame.image.load(
            resource_path(path)).convert_alpha(),(self.width, self.height)), 0)
        cardRect = cardSurf0.get_rect()
        mousex,mousey=pygame.mouse.get_pos()
        WIN.blit(cardSurf,(self.x,self.y))
        if cardRect.collidepoint(mousex-self.x0, mousey-self.y0):
            self.y = 100
            self.x = 400
            self.width=200
            self.height=300
        else: 
            self.y=self.y0
            self.x=self.x0
            self.width=self.width0
            self.height=self.height0
        #WIN.blit(cardSurf,(self.x,self.y))

    def selected(self):
        cardSurf = pygame.Surface((self.width0, self.height0),pygame.SRCALPHA)
        cardRect = cardSurf.get_rect() 
        mousex,mousey=pygame.mouse.get_pos()
        if cardRect.collidepoint(mousex-self.x0, mousey-self.y0):
            return self.image

def discardMode(cards,numcards):
    j=0
    toGo=[]
    while j<numcards:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(cards)):
                    if cards[i].selected():
                        print('selected')
                        toGo.append(i)
                        j+=1
                        if j >= numcards:
                            print(toGo)
                            toGo = sorted(toGo,reverse=True)
                            print(toGo)
                            for p in toGo:
                                cards.remove(cards[p])
                            return
        

def cardFunction(characters,cards,mana):
    cardChosen=False
    manaloss=0
    damage=0
    if characters[0].stunned==True:
        #WIN.blit(font1.render("stunned!", 1, BLACK),(100,100))
        return manaloss
    for i in range(len(cards)):
        TEXT = cards[i].selected()
        if TEXT=='deal3dmg.png' and mana > 0:
            characters[0].x+=100
            damage=3
            cards.remove(cards[i])
            cardChosen=True
            manaloss=1
        if TEXT=='deal6dmg.png' and mana > 1:
            characters[0].x+=100
            damage=6
            cards.remove(cards[i])
            cardChosen=True
            manaloss=2
        if TEXT=='gain5health.png' and mana > 0:
            characters[0].health+=5
            if characters[0].health>characters[0].health0:
                characters[0].health=characters[0].health0
            cards.remove(cards[i])
            cardChosen=True
            manaloss=1
        if TEXT=='gain2counter.png' and mana > 0:
            characters[0].reflect+=2
            cards.remove(cards[i])
            cardChosen=True
            manaloss=1  
        if TEXT=='gain1att.png':
            characters[0].attack+=1
            cards.remove(cards[i])
            cardChosen=True
            manaloss=0 
        if TEXT=='stun1random.png' and mana > 1:
            characters[1].stunned=True
            cards.remove(cards[i])
            cardChosen=True
            manaloss=2
        if TEXT=='disc2gain2mana.png' and mana > 0:
            cards.remove(cards[i])
            j=0
            discardMode(cards,2)
            #while len(cards)>0 and j < len(cards)+1 and j <2:
               #cards.remove(cards[0])
                #j+=1
            cardChosen=True
            manaloss=-1
        if TEXT=='deal7onlycard.png':
            if len(cards)>1:
                cardChosen=False
            else:
                characters[0].x+=100
                damage=7
                cards.remove(cards[i])
                cardChosen=True
                manaloss=0
        if TEXT=='gain10onlycard.png':
            if len(cards)>1:
                cardChosen=False
            else:
                characters[0].health+=10
                if characters[0].health>characters[0].health0:
                    characters[0].health=characters[0].health0
                #damage=7
                cards.remove(cards[i])
                cardChosen=True
                manaloss=0
        if TEXT=='disc1draw1.png':
            cards.remove(cards[i])
            j=0
            #while j < len(cards) and j <1:
                #cards.remove(cards[0])
                #j+=1
            discardMode(cards,1)
            cardText=random.choice(os.listdir(resource_path('Assets/Cards/finishedcards/')))
            cards.append(card(250+i*100,450,100,150,cardText))
            cardChosen=True
            manaloss=0
        if TEXT=='deal2gain2health.png' and mana > 0:
            characters[0].x+=100
            damage=2
            characters[0].health+=2
            if characters[0].health>characters[0].health0:
                characters[0].health=characters[0].health0
            cards.remove(cards[i])
            cardChosen=True
            manaloss=1
        if cardChosen:
            characters[1].health-=damage*(1+characters[0].attack0)
            return manaloss
            break 
    return manaloss

