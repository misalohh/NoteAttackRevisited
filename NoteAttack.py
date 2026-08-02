import pygame
from screens.menu import Menu
from screens.gameplay import Gameplay
from screens.rules import Rules
from screens.settings import Settings
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.state = "menu"
        self.screens = {
            "menu": Menu(self.WIDTH, self.HEIGHT),
            "game": Gameplay(self.WIDTH, self.HEIGHT),
            "rules": Rules(self.WIDTH, self.HEIGHT),
            "settings": Settings(self.WIDTH, self.HEIGHT),
        }

        pygame.display.set_caption('Note Attack Revisited')

    def get_canvas_mouse_pos(self):
        mx, my = pygame.mouse.get_pos()
        sx = self.WIDTH / self.screen.get_width()
        sy = self.HEIGHT / self.screen.get_height()
        return (mx * sx, my * sy)

    def draw(self):
        mouse_pos = self.get_canvas_mouse_pos()
        self.screens[self.state].draw(self.game_canvas, mouse_pos)

        scaled = pygame.transform.scale(self.game_canvas, self.screen.get_size())
        self.screen.blit(scaled, (0, 0))
        pygame.display.update()

    def update(self):
        self.screens[self.state].update()
        self.draw()
        self.clock.tick(60)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = self.get_canvas_mouse_pos()
                    result = self.screens[self.state].handle_click(mouse_pos)
                    if result == "game":
                        self.screens["game"].end_game()  # Reset the gameplay  when starting a new game
                    if result:
                        self.state = result

            self.update()