import pygame
from UI.button import Button
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 100)
        
        self.clock = pygame.time.Clock()

        self.state = "menu"

        self.start_button = Button(self.WIDTH // 2 - 175, 170, 350, 80, "Start")
        self.rules_button = Button(self.WIDTH // 2 - 175, 270, 350, 80, "Rules")
        self.settings_button = Button(self.WIDTH // 2 - 175, 370, 350, 80, "Settings")
        

        pygame.display.set_caption('Note Attack Revisited')

    def get_canvas_mouse_pos(self):
        mx, my = pygame.mouse.get_pos()
        sx = self.WIDTH / self.screen.get_width()
        sy = self.HEIGHT / self.screen.get_height()
        return (mx * sx, my * sy)

    def draw_menu(self):
        self.game_canvas.fill((132, 169, 192))
        text_surface = self.font.render("Note Attack Revisited", True, (221, 216, 184))
        text_rect = text_surface.get_rect(midtop=(self.WIDTH // 2, 50))
        self.game_canvas.blit(text_surface, text_rect)
        self.start_button.draw(self.game_canvas)
        self.rules_button.draw(self.game_canvas)
        self.settings_button.draw(self.game_canvas)

    def draw_game(self):
        self.game_canvas.fill((132, 169, 192))

    def draw_settings(self):
        self.game_canvas.fill((132, 169, 192))
        text_surface = self.font.render("Settings", True, (221, 216, 184))
        text_rect = text_surface.get_rect(midtop=(self.WIDTH // 2, 50))
        self.game_canvas.blit(text_surface, text_rect)

    def draw_rules(self):
        self.game_canvas.fill((132, 169, 192))
        text_surface = self.font.render("Rules", True, (221, 216, 184))
        text_rect = text_surface.get_rect(midtop=(self.WIDTH // 2, 50))
        self.game_canvas.blit(text_surface, text_rect)

    def draw(self):
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "game":
            self.draw_game()
        elif self.state == "rules":
            self.draw_rules()
        elif self.state == "settings":
            self.draw_settings()

        scaled = pygame.transform.scale(self.game_canvas, self.screen.get_size())
        self.screen.blit(scaled, (0, 0))
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = self.get_canvas_mouse_pos()

                    if self.state == "menu":
                        if self.start_button.is_clicked(mouse_pos):
                            self.state = "game"
                        if self.rules_button.is_clicked(mouse_pos):
                            self.state = "rules"
                        if self.settings_button.is_clicked(mouse_pos):
                            self.state = "settings"

            self.update()