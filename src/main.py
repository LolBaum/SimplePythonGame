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

    white_ball = Ball((200, 200), 20)
    dragging = False
    drag_start_pos = (0, 0)
    dragging_pos = (0, 0)

    bg_color = pygame.Color('black')

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
                    print("dragging = ", dragging)
                    x, y = pygame.mouse.get_pos()
                    if white_ball.rect.collidepoint(x, y):
                        dragging = True
                        drag_start_pos = white_ball.rect.center #(x, y)
                        print("white_ball")
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    dragging = False
                    print("dragging = ", dragging)
            if dragging:
                if not pygame.mouse.get_pressed(num_buttons=3)[0]:  # left mouse button
                    dragging = False

        screen.fill(bg_color)


        white_ball.draw(screen)


        if dragging:
            print("dragging")
            dragging_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255, 255, 255), drag_start_pos, dragging_pos)





