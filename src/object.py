import pygame


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


class Ball(Obj):
    def __init__(self, pos: (int, int),
                 radius: int,
                 surf: pygame.surface.Surface = None):
        self.radius = radius
        size = radius*2
        surf = pygame.surface.Surface((size, size))
        pygame.draw.circle(surf, (200, 100, 100), (radius, radius), radius)
        super().__init__(pygame.rect.Rect(pos, (size, size)), surf)


