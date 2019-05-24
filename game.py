import random
import time
import pygame
import os

charX = 320
charY = 180

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (charX, charY)
pygame.init ()

display_width = 1280
display_height = 720

car_width = 50
car_height = 118

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

bg = pygame.image.load("background.png")#.convert()
gameDisplay = pygame.display.set_mode ((display_width, display_height))
pygame.display.set_caption ( "The Game" )
icon = pygame.image.load ( "logo.png" )
pygame.display.set_icon ( icon )
clock = pygame.time.Clock ()
white_car = pygame.image.load ( "white_car.jpg" )


def things_dodged(count) :
    font = pygame.font.SysFont ( None, 25 )
    text = font.render ( "Dodged: " + str ( count ), True, black )
    gameDisplay.blit ( text, (80, 50) )


def things(thingx, thingy, thingw, thingh, color) :
    pygame.draw.rect ( gameDisplay, color, [thingx, thingy, thingw, thingh] )


def car(x, y) :  # car is 50x118
    gameDisplay.blit ( white_car, (x, y) )


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
    x = (display_width * 0.45)
    y = (display_height * 0.4)
    x_change = 0
    y_change = 0

    thing_starty = -600
    thing_speed = 14
    thing_width = 100
    thing_startx = random.randrange ( 207, 1010)
    thing_height = 100
    dodged = 0
    gameExit = False

    # beginn game loop

    while not gameExit :
        
        # controls
        for event in pygame.event.get () :
            if event.type == pygame.QUIT :
                pygame.quit ()
                quit ()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_a :
                    x_change = -10
                elif event.key == pygame.K_d :
                    x_change = 10
                elif event.key == pygame.K_w :
                    y_change = -10
                elif event.key == pygame.K_s :
                    y_change = 10
                elif event.key == pygame.K_SPACE :
                    y_change = 0

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_a or event.key == pygame.K_d :
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s :
                    y_change = 0
                if event.key == pygame.K_SPACE :
                    y_change = 0
        x += x_change
        y += y_change

        gameDisplay.fill ( white )
        gameDisplay.blit ( bg, (0, 0) )

        # things(thingx, thingy, thingw, thingh, color)
        things ( thing_startx, thing_starty, thing_width, thing_height, black )
        thing_starty += thing_speed
        car ( x, y )
        things_dodged ( dodged )

        # side collision
#        if x > display_width - car_width or x < 0 or y + car_height > display_height or y < 0 :
 #           crash ()
        if x < 270 or x + car_width > 1010 or y + car_height > display_height or y < 0:
            crash ()



        # loops things and counts dodge's
        if thing_starty > display_height :
            thing_starty = 0 - thing_height
            thing_startx = random.randrange ( 270, 1010 )
            dodged += 1

        # things collision
        if x + car_width > thing_startx and x < thing_startx + thing_width :
            if y + car_height > thing_starty and y < thing_starty + thing_height :
                crash ()

        pygame.display.update ()
        clock.tick ( 60 )


game_loop ()
pygame.quit ()
quit ()