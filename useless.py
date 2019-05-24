import random
import time
import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (320, 180)
pygame.init ()

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# temp
count = 0

gameDisplay = pygame.display.set_mode ( (display_width, display_height))
bg = pygame.image.load("background1.png").convert()
pygame.display.set_caption ( "The Game" )
icon = pygame.image.load ( "logo.png" )
pygame.display.set_icon ( icon )
clock = pygame.time.Clock ()

class Car(object):
    def __init__(self):
        self.image = pygame.image.load("white_car.png")
        self.x = 640
        self.y = 500
        self.width = 50
        self.height = 118

    def handle_keys(self) :
        key = pygame.key.get_pressed ()
        dist = 5
        if key[pygame.K_s] :
            self.y += dist
            print("down")
        elif key[pygame.K_w] :
            self.y -= dist
            print("up")
        if key[pygame.K_d] :
            self.x += dist
            print("right")
        elif key[pygame.K_a] :
            self.x -= dist
            print("left")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load("enemy_car.png")
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 92

    def dodged(self):
        font = pygame.font.SysFont ( None, 25 )
        text = font.render ( "Dodged: " + str ( count ), True, black )
        gameDisplay.blit ( text, (80, 50) )

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

def crash() :
    message_display ( "You crashed" )

def text_objects(text, font) :
    textSurface = font.render ( text, True, black )
    return textSurface, textSurface.get_rect ()

def message_display(text) :
    largeText = pygame.font.Font ( "freesansbold.ttf", 115 )
    TextSurf, TextRect = text_objects ( text, largeText )
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit ( TextSurf, TextRect )

    pygame.display.update ()
    time.sleep ( 2 )
    game_loop ()

def game_loop() :

    vpspeed = 8     # virtual speed (background speed)
    dodged = 0
    gameExit = False
    yb = 0
    xb = 0

    car = Car()
    enemy = Enemy()
    enemy.x = random.randint ( 270, 1010 - enemy.width )
    # beginn game loop
    while not gameExit :

        # controls
        for event in pygame.event.get () :
            if event.type == pygame.QUIT :
                pygame.quit ()
                quit ()

        car.handle_keys()

        # looped background
        gameDisplay.fill ( white )
        rel_y = yb % bg.get_rect ().height
        gameDisplay.blit ( bg, (xb, rel_y - bg.get_rect ().height) )
        yb += vpspeed
        if rel_y < display_height :
            gameDisplay.blit ( bg, (xb, rel_y) )

        car.draw(gameDisplay)

        if car.x < 270 or car.x + car.width > 1010 or car.y + car.height >  display_height or car.y < 0 :
            crash()

        enemy.draw ( gameDisplay )
        enemy.y += 5


        if enemy.y > display_height :
            enemy.y = 0 -enemy.height
            enemy.x = random.randint ( 270, 1010 - enemy.width )

        if car.x + car.width > enemy.x and car.x < enemy.x + enemy.width :
            if car.y + car.height > enemy.y and car.y < enemy.y + enemy.height :
                crash ()


        '''
        # things(thingx, thingy, thingw, thingh, color)
        things ( thing_startx, thing_starty, thing_width, thing_height, red )
        thing_starty += thing_speed
        car ( x, y )
        things_dodged ( dodged )

        # loops things and counts dodge's
        if thing_starty > display_height :
            thing_starty = 0 - thing_height
            thing_startx = random.randrange ( 270, 1010 - thing_width )
            dodged += 1

        # things collision
        if x + car_width > thing_startx and x < thing_startx + thing_width :
            if y + car_height > thing_starty and y < thing_starty + thing_height :
                crash ()
        '''

        pygame.display.update ()
        clock.tick ( 120 )

game_loop ()
pygame.quit ()
quit ()