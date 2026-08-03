import math
import pygame

from config import settings
from core.particle import Particle


class Heart:
    def __init__(self):
        self.particles = []
        self.create()

    def create(self):
        for i in range(settings.PARTICLE_COUNT):
            t = i / settings.PARTICLE_COUNT * math.pi * 2
            x = 16 * math.sin(t) ** 3
            y = (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            self.particles.append(
                Particle(
                    settings.WIDTH//2 + x * settings.HEART_SCALE,
                    settings.HEIGHT//2 - y * settings.HEART_SCALE
                )
            )

    def update(self):
        pass

    def draw(self, screen):
        for p in self.particles:
            pygame.draw.circle(screen, (255, 40, 140), (int(p.x), int(p.y)), 2)
