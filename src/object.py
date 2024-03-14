import pygame
import numpy as np

from src.utils import rotate, reflect_vector


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
                 surf: pygame.surface.Surface = None,
                 color: (int, int, int) = (200, 100, 100)):
        self.radius = radius
        size = radius * 2
        surf = pygame.surface.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, color, (radius, radius), radius)
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

                bounds = self.radius + b.radius
                intersection = self.distance(b) - bounds
                if intersection < 0:
                    d = normalize(pos_diff)
                    self.pos += d * (intersection / 2)
                    b.pos -= d * (intersection / 2)

                #if (v_res * pos_diff).sum() >= 0:
                m1 = 2  # Todo: use masses
                m2 = 2
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
        if np.linalg.norm(self.vel) < 0.1:
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

    def reflect_on_line(self, lp0, lp1):
        l_dir = normalize(lp1 - lp0)                # direction vector of the line
        nv = np.array([-l_dir[1], l_dir[0]])   # normal vector to the line
        d = (lp0-self.pos) @ nv                            # distance to line
        pt_x = self.pos + nv * d                               # intersection point on endless line
        if not (abs(d) > self.radius or self.vel @ (pt_x-self.pos) <= 0 or  # test if the ball hits the line
           (pt_x-lp0) @ l_dir < 0 or (pt_x-lp1) @ l_dir > 0):
            self.vel = reflect_vector(self.vel, nv)                     # reflect the direction vector on the line (like a billiard ball)


    def collide_with_wall(self, line_list):
        for line in line_list:
            self.reflect_on_line(*np.array(line.p))


class Opponent(Obj):
    def __init__(self, pos, vertices):
        self.vertices = vertices
        size = abs(vertices[0][0] - vertices[1][0]) + 1
        surf = pygame.surface.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.polygon(surf, pygame.Color((50, 100, 50)), self.vertices)
        super().__init__(surf.get_rect(), surf)
        self.rect.center = pos
        self.visible = True

    def __del__(self):
        pass


    def update(self):
        pass


class Border:
    def __init__(self, p0, p1):
        self.p = [p0, p1]

    def draw(self, display: pygame.surface.Surface):
        pygame.draw.line(display, (200, 200, 200), self.p[0], self.p[1], 5)


