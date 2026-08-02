import pygame
from colours import BACKGROUND
from sprites.player import Player
from sprites.enemies import Enemy
from UI.button import Button

class Gameplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.centre = (width // 2, height // 2)
        self.back_button = Button(35, 35, 120, 60, "Back")

        self.player = Player(width // 2, height // 2) 

        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
        self.spawn_interval = 100

    def end_game(self):
        self.enemies.empty()


    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            enemy = Enemy(self.width, self.height, target_pos=self.centre)
            self.enemies.add(enemy)

        self.enemies.update()

        for enemy in self.enemies:
            if enemy.check_collision(self.player):
                self.end_game()
                return "menu"

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        self.back_button.draw(surface, mouse_pos)
        self.player.draw(surface)

        for enemy in self.enemies:
            enemy.draw(surface)

    def handle_click(self, mouse_pos):
            if self.back_button.is_clicked(mouse_pos):
                return "menu"