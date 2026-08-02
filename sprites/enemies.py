import pygame
import random
import math

import pygame
import random

class Enemy(pygame.sprite.Sprite):   
    def __init__(self, screen_width, screen_height, target_pos, radius=20, color=(200, 60, 60), speed=2):
        super().__init__()           

        self.radius = radius
        self.color = color
        self.speed = speed

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

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
        return distance < (self.radius + player.radius - 10)

    def update(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)