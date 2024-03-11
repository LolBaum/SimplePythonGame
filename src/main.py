import pygame
import sys


class Obj:
    def __init__(self, rect: pygame.rect.Rect,
                 surf: pygame.surface.Surface):
        self.surf = surf
        self.rect = rect

    def on_click(self):
        self._set_hidden(False)
        print(f"freed {self.value}")

    def draw(self, display: pygame.surface.Surface):
        pass


if __name__ == "__main__":
    print("running game")
    pygame.init()
    pygame.font.init()
    w, h = 940, 940
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    font = pygame.font.Font(size=40)

    print("Starting main loop")
    while True:
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Shutting down the game')
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    x, y = pygame.mouse.get_pos()

