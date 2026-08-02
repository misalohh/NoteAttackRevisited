import pygame
from colours import PLAYER, PLAYER_OUTLINE

class Player:
    def __init__(self, x, y):

        self.radius = 30
        self.color = PLAYER
        self.pos = pygame.Vector2(x, y)

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, PLAYER , (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, PLAYER_OUTLINE, (self.radius, self.radius), self.radius, 4)

        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)