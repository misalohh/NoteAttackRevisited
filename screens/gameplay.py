import pygame
from colours import BACKGROUND, TEXT
from sprites.laser import Laser
from sprites.player import Player
from sprites.enemies import Enemy
from UI.button import Button

class Gameplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.centre = (width // 2, height // 2)
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 170)

        self.back_button = Button(35, 35, 120, 60, "Back")
        self.player = Player(width // 2, height // 2) 
        self.lasers = []

        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
        self.spawn_interval = 150
        self.difficulty = "medium"

        self.game_over = False

    def end_game(self):
        self.enemies.empty()
        self.lasers.empty()
        self.spawn_timer = 0
        self.game_over = True

    def start_game(self):
        self.enemies.empty()
        self.spawn_timer = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            return
        
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            enemy = Enemy(self.width, self.height, target_pos=self.centre)
            self.enemies.add(enemy)

        self.enemies.update()

        for enemy in self.enemies:
            if enemy.check_collision(self.player):
                self.end_game()

        for laser in self.lasers:
            laser.update()
            for enemy in self.enemies:
                if enemy.check_collision(laser):
                    self.enemies.remove(enemy)
                    self.lasers.remove(laser)
                    break
                
        self.lasers = [laser for laser in self.lasers if not laser.finished]

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        self.back_button.draw(surface, mouse_pos)
        self.player.draw(surface)
        for laser in self.lasers:
            laser.draw(surface)

        for enemy in self.enemies:
            enemy.draw(surface)

        if self.game_over:
            text_surface = self.font.render("Game Over", True, TEXT)
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
            surface.blit(text_surface, text_rect)

    def handle_click(self, mouse_pos):
            if self.back_button.is_clicked(mouse_pos):
                return "menu"

    def handle_key(self, key):
        if key == pygame.K_SPACE:
            self.lasers.append(Laser(self.centre[0], self.centre[1]))