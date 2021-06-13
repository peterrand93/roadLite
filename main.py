import pygame
import os

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RoadLite")
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space2.jpeg')), (WIDTH, HEIGHT))

FPS=60 

def draw_window():
    WIN.blit(SPACE, (0,0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()

if __name__ == "__main__":
    main()
