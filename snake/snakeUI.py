import math
import pygame
import time

import snake.Game


class SnakeUI:
    gamefont = None
    screen = None
    snake_game = None
    score_txt = None
    score_surface = None
    frame_rate = 1

    # setup things, gets called when the UI is created automatically
    def __init__(self, screenarg, fontarg):
        # 'Arial', 20
        self.gamefont = fontarg
        self.screen = screenarg

        self.snake_game = snake.Game.SnakeGame()
        self.score_txt = "score: " + str(self.snake_game.score)

        self.score_surface = self.gamefont.render(self.score_txt, False, (255, 255, 255))
        self.screen.blit(self.score_surface, (0, 0))

    def draw_board(self, board_surfaces):
        for plane in board_surfaces:
            for row in plane:
                for val in row:
                    if val[1]:
                        # snake body or apple
                        pygame.draw.rect(self.screen, (255, 255, 255), val[0])
                    else:
                        # normal
                        pygame.draw.rect(self.screen, (127, 127, 127), val[0])

    def show_score(self):
        self.score_txt = "score: " + str(self.snake_game.score)
        self.score_surface = self.gamefont.render(self.score_txt, False, (255, 255, 255))
        self.screen.blit(self.score_surface, (0, 0))

    def start(self):
        self.snake_game.update_board()
        self.draw_board(self.snake_game.board)
        pygame.display.flip()

        start_milis = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.screen.fill((0, 0, 0))
                        return
                    elif event.key == pygame.K_w:
                        self.snake_game.heading = "y-"
                    elif event.key == pygame.K_a:
                        self.snake_game.heading = "x-"
                    elif event.key == pygame.K_s:
                        self.snake_game.heading = "y+"
                    elif event.key == pygame.K_d:
                        self.snake_game.heading = "x+"
                    elif event.key == pygame.K_z:
                        self.snake_game.heading = "z+"
                    elif event.key == pygame.K_c:
                        self.snake_game.heading = "z-"

            # code after the if only gets executed once every frame
            exe_time = time.time() - start_milis
            if exe_time > (1 / self.frame_rate):
                self.screen.fill((0, 0, 0))
                self.snake_game.update_board()
                self.draw_board(self.snake_game.board)
                self.show_score()

                pygame.display.flip()
                start_milis = time.time()
