import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.Game_W, self.Game_H = 480, 270
        self.Screen_W, self.Screen_H = 960, 540
        self.game_canvas = pygame.Surface((self.Game_W, self.Game_H))
        self.screen = pygame.display.set_mode((self.Screen_W, self.Screen_H))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Note Attack')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(60)