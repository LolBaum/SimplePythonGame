import pygame


def setup_pygame():
    pygame.init()
    pygame.font.init()


def basic_surf(size, color):
    if isinstance(size, int):
        size = (size, size)
    surf = pygame.surface.Surface(size)
    surf.fill(color)
    return surf


NUMBER_COLORS = ["blue",
                 "springgreen4",
                 "red",
                 "blue4",
                 "brown",
                 "cyan",
                 "black",
                 "grey"]


def number_field(n, font, size):
    surf = basic_surf(size, (180, 180, 180))
    color = NUMBER_COLORS[n-1] if len(NUMBER_COLORS) > n else NUMBER_COLORS[-1]
    surf.blit(font.render(" " + str(n), True, color), pygame.rect.Rect(0, 0, 0, 0))
    return surf
