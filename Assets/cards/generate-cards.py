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
textheight=150

font1 = pygame.font.Font(resource_path('freesansbold.ttf'), textheight)
font3 = pygame.font.Font(resource_path('freesansbold.ttf'), int(round(textheight/3.5)))
font4 = pygame.font.Font(resource_path('freesansbold.ttf'), int(round(textheight/2.2)))

WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))



class card():
    def __init__ (self, x,y, width, height, cost, text, cardtype):
        self.x = x
        self.y0=y
        self.y = y
        self.width = width
        self.height = height
        self.cost = cost
        self.text = text
        self.cardtype = cardtype

    def cardDraw(self):
        cardSurf = pygame.Surface((self.width, self.height),pygame.SRCALPHA)
        cardRect = cardSurf.get_rect()
        cardBG = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
            resource_path(self.cardtype)).convert(),(self.width, self.height)), 0)
        textSurf = font3.render(self.text, 1, BLACK)
        fontHeight = font3.size("Tg")[1]
        textRect = textSurf.get_rect()
        textRect.top = 0#textRect.width/2#self.y
        y = textRect.top
        textRect.left = 0#self.x
        lineSpacing=-2
        bkg=0
        WIN.blit(cardBG,(self.x,self.y))
        text=self.text
        text2=text
        while text:
            i = 1
            while font3.size(text[:i])[0] < (cardRect.width-50) and i < len(text):
                i += 1
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
            if bkg:
                image = font3.render(text[:i], 1, BLACK, bkg)
                image.set_colorkey(bkg)
            else:
                image = font3.render(text[:i], 1, RED)
            imageRect=image.get_rect()
            y += fontHeight + lineSpacing
            text = text[i:]
        yold=y
        text=text2
        
        textRect.top = 0
        y = textRect.top
        while text:
            i = 1

            while font3.size(text[:i])[0] < (cardRect.width-150) and i < len(text):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
            # render the line and blit it to the surface
            if bkg:
                image = font3.render(text[:i], 1, BLACK, bkg)
                image.set_colorkey(bkg)
            else:
                image = font3.render(text[:i], 1, BLACK)
            imageRect=image.get_rect()
            WIN.blit(image, (self.x + cardRect.width/2 - imageRect.width/2, y+self.y +cardRect.height/2-imageRect.height/2-yold/2+25))
            y += fontHeight + lineSpacing
            text = text[i:]
        #print(self.cost)
        cardCost=font4.render(str(self.cost), 1, WHITE)
        WIN.blit(cardCost,(55,25))





cardinfo=[]
cardinfo.append([1,'Deal 3 Damage','deal3dmg','cardbaseAtt-01.png'])
cardinfo.append([2,'Deal 6 Damage','deal6dmg','cardbaseAtt-01.png'])
cardinfo.append([1,'Deal 2 Damage, Gain 2 Health','deal2gain2health','cardbaseAtt-01.png'])
cardinfo.append([1,'Gain 5 Health','gain5health','cardbaseDef.png'])
cardinfo.append([1,'Gain 2 Counter','gain2counter','cardbaseDef.png'])
cardinfo.append([0,'Discard 1 Card, Draw 1 Card','disc2draw2','cardbaseDef.png'])
cardinfo.append([0,'Gain 10 Health. Can only be played if only card in hand','gain10onlycard','cardbaseDef.png'])
cardinfo.append([0,'Deal 7 Damage. Can only be played if only card in hand','deal7onlycard','cardbaseAtt-01.png'])
cardinfo.append([2,'Stun a random enemy','stun1random','cardbaseEff.png'])
cardinfo.append([1,'Discard 2 Cards, Gain 2 Mana','disc2gain2mana','cardbaseEff.png'])
cardinfo.append([0,'Gain 1 Attack','gain1att','cardbaseEff.png'])


for i in range(len(cardinfo)):
    cardprint=card(0,0,WIDTH,HEIGHT,cardinfo[i][0],cardinfo[i][1],cardinfo[i][3])
    cardprint.cardDraw()
    savename="finishedcards/"+cardinfo[i][2]+".png"
    pygame.image.save(WIN, savename)