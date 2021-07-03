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

font3 = pygame.font.Font(resource_path('freesansbold.ttf'), 100)

WIDTH, HEIGHT = 1000, 1500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))



cardSurf = pygame.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
cardSurf.fill(WHITE)
cardRect = cardSurf.get_rect()


     
image = font3.render('Deal 3 Damage', 1, BLACK)
imageRect=image.get_rect()

WIN.blit(cardSurf, (0,0))
WIN.blit(image, (0,int(round(HEIGHT/2))))



savename="finishedcards/test.png"
pygame.image.save(WIN, savename)