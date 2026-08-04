import pygame
import random
from colours import ENEMY, ENEMY_OUTLINE, TEXT

class Enemy(pygame.sprite.Sprite):   
    def __init__(self, screen_width, screen_height, target_pos, letter, radius=25, speed=2):
        super().__init__()           

        self.radius = radius
        self.speed = speed
        self.letter = letter
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 60)

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, ENEMY, (radius, radius), radius)
        pygame.draw.circle(self.image, ENEMY_OUTLINE, (self.radius, self.radius), self.radius, 4)

        text_surface = self.font.render(self.letter, True, TEXT)
        text_rect = text_surface.get_rect(center=(radius, radius))
        self.image.blit(text_surface, text_rect)

        x, y = self.random_edge_position(screen_width, screen_height)
        self.rect = self.image.get_rect(center=(x, y))

        self.pos = pygame.Vector2(x, y)
        target = pygame.Vector2(target_pos)
        direction = target - self.pos
        if direction.length() != 0:
            direction = direction.normalize()
        self.direction = direction

    def random_edge_position(self, width, height):
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            return random.randint(0, width), - self.radius
        if side == "bottom":
            return random.randint(0, width), height + self.radius
        if side == "left":
            return - self.radius, random.randint(0, height)
        if side == "right":
            return width + self.radius, random.randint(0, height)

    def check_collision(self, player):
        distance = self.pos.distance_to(player.pos)
        return distance < (self.radius + player.radius - 5) # Adjusted collision threshold

    def update(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)