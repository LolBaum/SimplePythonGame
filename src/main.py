import pygame
import sys
from object import Ball, Opponent
from utils import normalize, vector_length


if __name__ == "__main__":
    print("running game")
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Billard Blizzard")
    w, h = 940, 640
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    font = pygame.font.Font(size=40)

    white_ball = Ball((200, 200), 20)

    dragging = False
    drag_start_pos = (0, 0)
    dragging_pos = (0, 0)

    #obstacle
    opponent_vertices = [(10, 100), (0, -300), (100, 10)]
    opponent = Opponent(opponent_vertices)

    bg_color = pygame.Color('black')

    print("Starting main loop")
    while True:
        clock.tick(60)
        ################
        # Handling I/O #
        ################

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
            if dragging:
                if not pygame.mouse.get_pressed(num_buttons=3)[0]:  # left mouse button
                    dragging = False
                    direction = (drag_start_pos[0] - dragging_pos[0], drag_start_pos[1] - dragging_pos[1])
                    normalised_dir = normalize(direction)
                    print("dir = ", normalised_dir)
                    strength = vector_length(direction)
                    if strength >= 30:
                        strength = 30
                    white_ball.set_impulse(normalised_dir, strength)

        ###########################
        # Applying game mechanics #
        ###########################
        white_ball.update()
        if white_ball.rect.centerx <= white_ball.radius:
            white_ball.flip_impulse(True, False)
        elif white_ball.rect.centerx >= w - white_ball.radius:
            white_ball.flip_impulse(True, False)

        if white_ball.rect.centery <= white_ball.radius:
            white_ball.flip_impulse(False, True)
        elif white_ball.rect.centery >= h - white_ball.radius:
            white_ball.flip_impulse(False, True)

        #######################
        # Displaying graphics #
        #######################

        screen.fill(bg_color)

        white_ball.draw(screen)
        opponent.draw(screen)

        if dragging:
            print("dragging")
            dragging_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255, 255, 255), drag_start_pos, dragging_pos)

        pygame.display.flip()





