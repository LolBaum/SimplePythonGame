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
    def __init__(self, pos: (int, int),
                 radius: int,
                 surf: pygame.surface.Surface = None):
        self.radius = radius
        size = radius*2
        surf = pygame.surface.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, (200, 100, 100), (radius, radius), radius)
        super().__init__(pygame.rect.Rect(pos, (size, size)), surf)
        self.vel = np.zeros(2)

    def update(self):
        pass



