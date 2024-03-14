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


def random_position(xy_lower, xy_upper):
    """returns positive values"""
    pos = np.random.rand(2)
    pos *= np.array(xy_upper) - xy_lower
    pos += xy_lower
    print(pos)
    return pos


def hit_object():
    pass


def reflect_vector(d, n):
    """
    :param d: directional vector
    :param n: normal vector of reflection axis (must be normalised)
    :return: reflected vector
    """
    return d - 2 * (d @ n) * n



def distance_point_line_2(pt, l1, l2):
    """From https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/examples/minimal_examples/pygame_minimal_intersect_point_line.py"""
    nx, ny = l1[1] - l2[1], l2[0] - l1[0]
    nlen = np.hypot(nx, ny)
    nx /= nlen
    ny /= nlen
    vx, vy = pt[0] - l1[0],  pt[1] - l1[1]
    dist = abs(nx*vx + ny*vy)
    return dist

def distance_point_line(pt, l1, l2):
    """From https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/examples/minimal_examples/pygame_minimal_intersect_point_line.py"""
    NV = pygame.math.Vector2(l1[1] - l2[1], l2[0] - l1[0])
    LP = pygame.math.Vector2(l1)
    P = pygame.math.Vector2(pt)
    return abs(NV.normalize().dot(P -LP))
