import pygame
import sys
from object import Ball, Opponent
from utils import normalize, vector_length, angle_between


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
    balls = [white_ball]
    other_ball = Ball((400, 400), 20)
    balls.append(other_ball)

    dragging = False
    drag_start_pos = (0, 0)
    dragging_pos = (0, 0)

    #obstacle
    opponent_vertices = [(0, 0), (100, 0), (0, 100)]
    opponent = Opponent((100, 100), opponent_vertices)

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
                    strength = vector_length(direction)/4
                    if strength >= 30:
                        strength = 30
                    white_ball.set_impulse(normalised_dir, strength)

        ###########################
        # Applying game mechanics #
        ###########################
        for b in balls:  # todo: move this to the ball class
            b.update()
            if b.rect.centerx <= b.radius:
                b.rect.centerx = b.radius
                b.flip_impulse(True, False)
            elif b.rect.centerx >= w - b.radius:
                b.rect.centerx = w - b.radius
                b.flip_impulse(True, False)

            if b.rect.centery <= b.radius:
                b.rect.centery = b.radius
                b.flip_impulse(False, True)
            elif b.rect.centery >= h - b.radius:
                b.rect.centery = h - b.radius
                b.flip_impulse(False, True)

        for i, b in enumerate(balls):
            b.collision(balls, i+1)

        #######################
        # Displaying graphics #
        #######################

        screen.fill(bg_color)

        for b in balls:
            b.draw(screen)

        opponent.draw(screen)

        if dragging:
            dragging_pos = pygame.mouse.get_pos()
            drag_start_pos = white_ball.rect.center
            pygame.draw.line(screen, (255, 255, 255), drag_start_pos, dragging_pos)

        pygame.display.flip()





