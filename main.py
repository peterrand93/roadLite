import pygame
import os
import random
import init
import constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
FPS=15
SCREENWIDTH, SCREENHEIGHT = 1000, 600

WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("RoadLite")

  
sc1x0=50
sc1y0=243

def main():
    characters = []  
    characters.append(init.character(sc1x0,sc1y0,200,240,20,0,0,False,'peep'))
    characters.append(init.character(700,110,250,200,25,0,0,False,"nonfatbutter"))
    run=True
    draw=True
    mana=3
    draw5=True
    endFight=False
    cards = []  
    endTurn=init.popupmenu(800,500,150,int(round(init.textheight/1.2)),['End Turn'],'endTurnBG.png')
    numdiscard= 0
    cardeffect=(0,0) #manaloss, num2discard
    while run:
        manaPop=init.popupmenu(100,525,18,29,[str(mana)],'manaBG.png') 

        OPTION=0
        constants.clock.tick(FPS)
        characters[0].x=sc1x0
        characters[0].y=sc1y0
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT
            if event.type == pygame.MOUSEBUTTONUP:
                if cardeffect[1]>0:
                    for i in range(len(cards)):
                        if cards[i].selected():
                            print("check")
                            cards.remove(cards[i])
                            cardeffect[1]-=1
                            break
                else:
                    cardeffect=init.cardFunction(characters,cards,mana)
                    #numdiscard=cardeffect(1)
                    #manaloss=cardeffect(2)
                    #print(cardeffect)
                    mana-=cardeffect[0]
                click=True
                #manaloss=init.cardFunction(characters,cards,mana)
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
            cardeffect=(0,0)
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
            retry=init.drawGameover(winlose,click)
            if retry:
                main()
                break
        else:
            for i in range(len(cards)):
                cards[i].x=250+i*100
                cards[i].x0=cards[i].x
            init.redrawGameWindow(characters=characters,cards=cards,endTurn=endTurn,manaPop=manaPop,numdiscard=cardeffect[1],test="testoo")
            #numdiscard=cardeffect[1]
            #init.redrawGameWindow(characters,cards,endTurn,manaPop,numdiscard)
if __name__ == "__main__":
    main()