import pygame
import sys
from object import Ball


if __name__ == "__main__":
    print("running game")
    pygame.init()
    pygame.font.init()
    w, h = 940, 940
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    font = pygame.font.Font(size=40)

    b = Ball((200, 200), 20)

    print("Starting main loop")
    while True:
        pygame.display.flip()
        clock.tick(30)

        b.draw(screen)

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

