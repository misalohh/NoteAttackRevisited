import pygame
from colours import PLAYER_OUTLINE

class Laser:
    def __init__(self, x, y, start_radius=5, max_radius=700, growth_speed=4, outline_width=4):
        self.color = PLAYER_OUTLINE
        self.pos = pygame.Vector2(x, y)

        self.radius = start_radius
        self.max_radius = max_radius
        self.growth_speed = growth_speed
        self.outline_width = outline_width

        self.image = self.laser_image()
        self.rect = self.image.get_rect(center=self.pos)

        self.finished = False

    def laser_image(self):
        size = int(self.radius * 2)
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.color, (size // 2, size // 2), int(self.radius), self.outline_width)
        return surface

    def update(self):
        self.radius += self.growth_speed
        if self.radius >= self.max_radius:
            self.finished = True
            return

        self.image = self.laser_image()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)