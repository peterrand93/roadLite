import pygame
import os
import random
import init

clock = pygame.time.Clock()

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

FPS=60

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RoadLite")

  
sc1x0=50
clock = pygame.time.Clock()

def main():
    characters = []  
    characters.append(init.character(sc1x0,240,200,240,20,0,0,False,"Peep-01.png"))
    characters.append(init.character(700,110,200,200,25,0,0,False,"nonfatbutter-01.png"))
    run=True
    draw=True
    mana=3
    draw5=True
    endFight=False
    cards = []  
    endTurn=init.popupmenu(800,500,150,int(round(init.textheight/1.2)),['End Turn'],'endTurnBG.png')

    while run:
        manaPop=init.popupmenu(100,525,18,29,[str(mana)],'manaBG.png') 

        OPTION=0
        #fontcolor=BLACK
        clock.tick(FPS)
        characters[0].x=sc1x0
        click=False
        #attackmenu = init.popupmenu(75,75,120,init.textheight*4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT
            if event.type == pygame.MOUSEBUTTONUP:
                click=True
                #if mana>0:
                manaloss=init.cardFunction(characters,cards,mana)
                mana-=manaloss
                    #print(mana)
                if endTurn.option_selected():
                    if characters[1].stunned==False:
                        enemyAttack=random.randrange(0,3)
                        characters[0].stunned=False
                        if enemyAttack==0:
                            damage=10
                            characters[0].health-=damage-characters[0].reflect
                            characters[1].health-=characters[0].reflect
                        elif enemyAttack==1:
                            characters[1].health+=7
                            if characters[1].health>characters[1].health0:
                                characters[1].health=characters[1].health0
                        else:
                            characters[0].stunned=True
                    else:
                        characters[1].stunned=False
                    #init.discardMode(cards,1)
                    draw5=True
                
                
        if draw5:
            for i in range(len(characters)):
                characters[i].reflect=0
            mana=3
            cards = []  
            for i in range(5):
                cardText=random.choice(os.listdir(init.resource_path('Assets/Cards/finishedcards/')))
                cards.append(init.card(250+i*100,450,100,150,cardText))
                draw5=False
        if characters[0].health<1 or characters[1].health<1:
            if characters[0].health<1:
                winlose='You Lose!!'
            else:
                winlose='You Win!!'
            #pygame.time.delay(2000)
            retry=init.drawGameover(winlose,click)
            if retry:
                main()
                break
        else:
            for i in range(len(cards)):
                cards[i].x=250+i*100
                cards[i].x0=cards[i].x
            init.redrawGameWindow(characters,cards,endTurn,manaPop)

if __name__ == "__main__":
    main()