import sys
import pygame


staticCharacter = "logo.png"

delta = {
    pygame.K_LEFT: (-20, 0),
    pygame.K_RIGHT: (+20, 0),
    pygame.K_UP: (0, -20),
    pygame.K_DOWN: (0, +20),
    }

class Ball(pygame.sprite.Sprite):

    # creating object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(staticCharacter)
        self.rect = self.image.get_rect()
        self.speed = [2, 2]
        self.area = pygame.display.get_surface().get_rect()

    # border reverser
    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.area.width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.area.height:
            self.speed[1] = -self.speed[1]

class Main(object):


    def __init__(self):
        self.setup()

    # init
    def setup(self):
        pygame.init()
        size = (self.width, self.height) = (640,640)
        self.black = (0, 0, 0)
        self.screen = pygame.display.set_mode(size, 0, 32)
        self.ball = Ball()
        self.setup_background()

    def setup_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.black)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ball.image, self.ball.rect)
        pygame.display.flip()

    # game loop start
    def event_loop(self):
        ball = self.ball
        # infinite loop
        while True:
            for event in pygame.event.get():
                # exit statements
                if ((event.type == pygame.QUIT) or
                    (event.type == pygame.KEYDOWN and
                     event.key == pygame.K_ESCAPE)):
                    sys.exit()

                #     pygame.K_LEFT: (-20, 0),
                #     pygame.K_RIGHT: (+20, 0),
                #     pygame.K_UP: (0, -20),
                #     pygame.K_DOWN: (0, +20),

                elif event.type == pygame.KEYDOWN:
                    deltax, deltay = delta.get(event.key, (0, 0))
                    ball.speed[0] += deltax
                    ball.speed[1] += deltay
            ball.speed = [0.99*s for s in ball.speed]
            ball.update()
            self.draw()
            pygame.time.delay(10)

if __name__ == '__main__':
    app = Main()
    app.event_loop()