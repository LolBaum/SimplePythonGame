import numpy as np
import pygame
import sys
from object import Ball, Opponent
from utils import normalize, vector_length, random_position

if __name__ == "__main__":
    print("running game")
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Billard Blizzard")
    w, h = 940, 640
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    font = pygame.font.Font(size=40)

    white_ball = Ball((200, 200), 20, color=(220, 220, 220))
    blue_ball = Ball((400, 200), 20, color=(100, 100, 220))
    balls = [white_ball, blue_ball]
    for i in range(10):
        balls.append(Ball(random_position([30, 30], [w-30, h-30]), 20))

    dragging = False
    dragging_blue = False
    drag_start_pos = (0, 0)
    dragging_pos = (0, 0)

    #obstacle
    opponent_vertices = [(0, 0), (50, 0), (25, 50)]
    opponent = Opponent((300,300), opponent_vertices)

    opponents = [opponent]

    bg_color = pygame.Color('black')

    print("Starting main loop")
    while True:
        clock.tick(120)
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
                    elif blue_ball.rect.collidepoint(x, y):
                        dragging_blue = True
                        print("blue_ball")

            if dragging:
                if not pygame.mouse.get_pressed(num_buttons=3)[0]:  # left mouse button
                    dragging = False
                    direction = (drag_start_pos[0] - dragging_pos[0], drag_start_pos[1] - dragging_pos[1])
                    normalised_dir = normalize(direction)
                    print("dir = ", normalised_dir)
                    strength = vector_length(direction)/4
                    if strength >= 15:
                        strength = 15
                    white_ball.set_impulse(normalised_dir, strength)
        if dragging_blue:
            old_pos = blue_ball.pos
            blue_ball.pos = np.array(pygame.mouse.get_pos(), dtype=float)
            blue_ball.vel = (blue_ball.pos - old_pos)/3
            if not pygame.mouse.get_pressed(num_buttons=3)[0]:  # left mouse button
                dragging_blue = False

        ###########################
        # Applying game mechanics #
        ###########################
        for b in balls:  # todo: move this to the ball class
            b.update()
            if b.rect.centerx <= b.radius:
                b.pos[0] = b.radius
                b.flip_impulse(True, False)
            elif b.rect.centerx >= w - b.radius:
                b.pos[0] = w - b.radius
                b.flip_impulse(True, False)

            if b.rect.centery <= b.radius:
                b.pos[1] = b.radius
                b.flip_impulse(False, True)
            elif b.rect.centery >= h - b.radius:
                b.pos[1] = h - b.radius
                b.flip_impulse(False, True)

            for o in opponents:
                if o.rect.collidepoint(b.pos):
                    opponents.remove(o)
                    print("Collide")

        for i, b in enumerate(balls):
            b.collision(balls, i+1)

        #######################
        # Displaying graphics #
        #######################

        screen.fill(bg_color)

        for b in balls:
            b.draw(screen)

        for o in opponents:
            o.draw(screen)

        if dragging:
            dragging_pos = pygame.mouse.get_pos()
            drag_start_pos = white_ball.rect.center
            pygame.draw.line(screen, (255, 255, 255), drag_start_pos, dragging_pos)

        pygame.display.flip()





