import pygame
import os

img_path = os.path.join ("white_car.jpg")
pygame.init()
class Car(object):
    def __init__(self):
        self.image = pygame.image.load(img_path)
        self.x = 0
        self.y = 0
def handle_keys(self) :
        key = pygame.key.get_pressed ()
        dist = 5  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] :  # down key
            self.y += dist  # move down
        elif key[pygame.K_UP] :  # up key
            self.y -= dist  # move up
        if key[pygame.K_RIGHT] :  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT] :  # left key
            self.x -= dist  # move left

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


screen = pygame.display.set_mode((640, 400))

car = Car()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    car.handle_keys()

    screen.fill((255,255,255))
    car.draw(screen)
    pygame.display.update()

    clock.tick(40)