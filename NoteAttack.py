import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
         
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Note Attack')

    def draw(self):
        self.game_canvas.fill((210, 150, 250))
        self.screen.blit(self.game_canvas, (0, 0))
        pygame.display.update()

    def update(self):
        self.draw()
        self.clock.tick(60)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.update()