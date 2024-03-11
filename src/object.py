import pygame
import numpy as np
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm

class Obj:
    def __init__(self, rect: pygame.rect.Rect,
                 surf: pygame.surface.Surface):
        self.surf = surf
        self.rect = rect

    def on_click(self):
        self._set_hidden(False)
        print(f"freed {self.value}")

    def draw(self, display: pygame.surface.Surface):
        display.blit(self.surf, self.rect)

    def update(self):
        pass


class Ball(Obj):
    def __init__(self, pos: (float, float),
                 radius: int,
                 surf: pygame.surface.Surface = None):
        self.radius = radius
        size = radius*2
        surf = pygame.surface.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, (200, 100, 100), (radius, radius), radius)
        super().__init__(pygame.rect.Rect(pos, (size, size)), surf)
        self.pos = np.array(pos, dtype=float)
        self.vel = np.zeros(2, dtype=float)
        self.friction = 0.995


    def update(self):
        self.vel *= self.friction
        self.pos += self.vel
        self.rect.centerx += int(self.vel[0])
        self.rect.centery += int(self.vel[1])
        self.rect.center = (int(self.pos[0]), int(self.pos[1]))
        if np.linalg.norm(self.vel) < 0.5:
            self.vel = np.zeros(2, dtype=float)
        print(self.rect.centerx,  int(self.vel[1]))

    def set_impulse(self, direction: np.array, strength: float, dampening: float = 0.8):
        self.vel = direction * strength * dampening

    def flip_impulse(self, x: bool, y: bool):
        if x:
            self.vel[0] *= -1
        if y:
            self.vel[1] *= -1




