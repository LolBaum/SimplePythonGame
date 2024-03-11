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


def normalize(vec: np.array or list[float, float] or tuple(float, float)):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm


def vector_length(vec):
    return np.linalg.norm(vec)
