import pygame
import numpy as np

from src.utils import rotate


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

    def draw(self, display: pygame.surface.Surface):
        display.blit(self.surf, self.rect)

    def update(self):
        pass


class Ball(Obj):
    def __init__(self, pos: (float, float),
                 radius: int,
                 surf: pygame.surface.Surface = None):
        self.radius = radius
        size = radius * 2
        surf = pygame.surface.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, (200, 100, 100), (radius, radius), radius)
        super().__init__(pygame.rect.Rect(pos, (size, size)), surf)
        self.pos = np.array(pos, dtype=float)
        self.vel = np.zeros(2, dtype=float)
        self.friction = 0.995
        self.is_moving = False

    def collision(self, balls: list, start_idx: int):
        """Based on a JS example from 101Computing
        https://www.101computing.net/elastic-collision-in-a-pool-game/
        """
        for b in balls[start_idx:]:
            if self.distance(b) < self.radius + b.radius:
                v_res = self.vel -b.vel
                pos_diff = b.pos - self.pos
                if (v_res * pos_diff).sum() >= 0:
                    m1 = 1  # Todo: use masses
                    m2 = 1
                    theta = - np.arctan2(pos_diff[0], pos_diff[1])
                    u1 = rotate(self.vel, theta)
                    u2 = rotate(b.vel, theta)
                    v1 = rotate([u1[0] * (m1 - m2)/(m1 + m2) + u2[0] * 2 * m2/(m1 + m2), u1[1]], -theta)
                    v2 = rotate([u2[0] * (m2 - m1)/(m1 + m2) + u1[0] * 2 * m1/(m1 + m2), u2[1]], -theta)

                    self.vel = np.array(v1)
                    b.vel = np.array(v2)

    def update(self):
        self.vel *= self.friction
        self.pos += self.vel
        self.rect.centerx += int(self.vel[0])
        self.rect.centery += int(self.vel[1])
        self.rect.center = (int(self.pos[0]), int(self.pos[1]))
        if np.linalg.norm(self.vel) < 0.5:
            self.vel = np.zeros(2, dtype=float)
            self.is_moving = False
        else:
            self.is_moving = True

    def set_impulse(self, direction: np.array, strength: float, dampening: float = 0.8):
        self.vel = direction * strength * dampening

    def flip_impulse(self, x: bool, y: bool):
        if x:
            self.vel[0] *= -1
        if y:
            self.vel[1] *= -1

    def distance(self, other):
        return np.sqrt(((self.pos - other.pos)**2).sum())



class Opponent(Obj):
    def __init__(self, pos, vertices):
        self.vertices = vertices
        surf = pygame.surface.Surface((200,200), pygame.SRCALPHA)
        pygame.draw.polygon(surf, pygame.Color((0, 128, 0)), self.vertices)
        super().__init__(pygame.Rect(pos, (0, 0)),
                         surf)

    def update(self):
        pass


