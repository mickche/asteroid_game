import random

from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        x, y = self.position
        first_velocity = self.velocity.rotate(random.uniform(20, 50))
        second_velocity = self.velocity.rotate(random.uniform(-20, -50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first, second = Asteroid(x, y, new_radius), Asteroid(x, y, new_radius)
        first.velocity = 1.2 * first_velocity
        second.velocity = 1.2 * second_velocity