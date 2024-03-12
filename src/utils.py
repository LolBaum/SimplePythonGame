import pygame
import numpy as np


def setup_pygame():
    pygame.init()
    pygame.font.init()


def basic_surf(size, color):
    if isinstance(size, int):
        size = (size, size)
    surf = pygame.surface.Surface(size)
    surf.fill(color)
    return surf


def normalize(vec: np.array or list[float, float] or tuple[float, float]):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2"""
    v1_u = normalize(v1)
    v2_u = normalize(v2)
    return np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))


def vector_length(vec):
    return np.linalg.norm(vec)


def rotate(vel, theta):
    return [vel[0] * np.cos(theta) - vel[1] * np.sin(theta), vel[0] * np.sin(theta) + vel[1] * np.cos(theta)]


def hit_object():
    pass
