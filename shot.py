import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS

    def draw(self, surface):
        pygame.draw.circle(surface, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt