import pygame
from pygame.locals import *
import sys
import os

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

W, H = 1208, 720
HW, HH = W / 2, H / 2
AREA = W * H

os.environ["SDL_VIDEO_WINDOW_POS"] = "50, 50"

pygame.init ()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("This is just pure Scrap")
FPS = 120

background = pygame.image.load("background.png").convert()
x = 0
y = 0
while True:
    events()

    rel_y = y % background.get_rect().height
    DS.blit(background, (x, rel_y - background.get_rect().height))
    y += 10
    if rel_y < H:
        DS.blit(background, (x, rel_y))

    pygame.display.update()
    CLOCK.tick(FPS)