import pygame
import os
import random
#import serial #For sensor ctrl only

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
HEIGHT2 = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Light Runner")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
#arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=.001) #For sensor ctrl only

RED_HIT = pygame.USEREVENT + 1

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space2.jpeg')), (WIDTH, HEIGHT2))

def draw_window(red,spaceY,rectangles):
    SF = round(spaceY/HEIGHT2) #spaceFrames for space drawing
    WIN.blit(SPACE, (0, spaceY+HEIGHT-SF*HEIGHT2))
    WIN.blit(SPACE, (0, spaceY-HEIGHT2+HEIGHT-SF*HEIGHT2))
    for rects in rectangles:
        ASTEROIDPIC = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'asteroid.png')), (rects.length, rects.width))
        WIN.blit(ASTEROIDPIC, (rects.x, rects.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    draw_text = WINNER_FONT.render(str(spaceY), 1, WHITE)
    WIN.blit(draw_text, (50 , 50))
    pygame.display.update()

def red_handle_movement(keys_pressed, red, handspd):
    VEL=5
    if keys_pressed[pygame.K_SPACE]:  # SPEED BOOST
        VEL=20
    if keys_pressed[pygame.K_a] and red.x - VEL > 0:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL
    numbers = [] #Only used with sensor mode
    for word in handspd.split():
        if word.isdigit() or word=="-":
            numbers.append(int(word))
    for spds in numbers:
        if abs(spds)-2000<1000:
            if red.x<WIDTH-SPACESHIP_WIDTH:
                if (spds-2000)>0:
                    red.x += (spds-2000)/50
            if red.x>0:
                if (spds-2000)<0:
                    red.x += (spds-2000)/50

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def handleAST(red,rectangles):
    spriteRED=pygame.sprite.Sprite()
    spriteRED.image=pygame.Surface((red[2],red[3]))
    spriteRED.rect = red
    for ASTEROIDS in rectangles:
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = pygame.Surface((ASTEROIDS.length, ASTEROIDS.width), pygame.SRCALPHA)
        pygame.draw.circle(sprite1.image, (255, 0, 0), (ASTEROIDS.length/2,ASTEROIDS.width/2),ASTEROIDS.width/2)
        sprite1.rect = pygame.Rect(ASTEROIDS.x,ASTEROIDS.y,ASTEROIDS.length,ASTEROIDS.width)
        sprite1.radius = ASTEROIDS.length/2*.8
        test_group = pygame.sprite.Group(spriteRED)
        if pygame.sprite.spritecollide(sprite1, test_group, False, pygame.sprite.collide_circle):
            pygame.event.post(pygame.event.Event(RED_HIT))
        ASTEROIDS.y+=ASTEROIDS.yspd
        ASTEROIDS.x+=ASTEROIDS.xspd

def write_read():#Sensor extra only
    arduino.write(bytes(str(0), 'utf-8'))
    data = arduino.readline().decode('utf-8').rstrip()
    return data

class Rectangle:
    def __init__ (self, x,y, width, length,xspd,yspd):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.xspd = xspd
        self.yspd = yspd

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    spaceY = 0
    dead=False
    rectangles = []
    dy=10
    rectpos=Rectangle(0,20001,0,0,0,0)
    i=0
    while i<10:
        rectangles.append(rectpos)
        i += 1
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == RED_HIT:
                dead = True
                print("dead")
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if dead==True:
            winner_text = "BOOM!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        handspd = str(2000)#write_read() #sensor extra only
        red_handle_movement(keys_pressed, red,handspd)
        for ASTEROIDS in rectangles:
            if ASTEROIDS.y>500:
                rectangles.remove(ASTEROIDS)
                asteroidsize=random.randrange(0,200)
                ASTEROIDPOS =Rectangle(random.randrange(0,WIDTH-100),random.randrange(-1000,-500),asteroidsize,asteroidsize,random.randrange(-2,2),random.randrange(3,12))
                rectangles.append(ASTEROIDPOS)
        handleAST(red,rectangles)
        draw_window(red,spaceY,rectangles)
        spaceY += dy #March forward
    main()

if __name__ == "__main__":
    main()
