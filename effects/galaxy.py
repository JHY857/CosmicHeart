import random
import pygame


class Galaxy:
    def __init__(self, count=300):
        self.stars = [
            (random.randint(0, 1200), random.randint(0, 800))
            for _ in range(count)
        ]

    def draw(self, screen):
        for x, y in self.stars:
            pygame.draw.circle(screen, (150, 180, 255), (x, y), 1)
