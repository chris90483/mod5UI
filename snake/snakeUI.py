import pygame
import snake.Game


class SnakeUI:
    gamefont = None
    screen = None
    score_txt = None
    score_surface = None
    frame_rate = 1

    # setup things, gets called when the UI is created automatically
    def __init__(self, screenarg, fontarg):
        # 'Arial', 20
        self.gamefont = fontarg
        self.screen = screenarg

        self.score_txt = "score: 0"

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

    def show_score(self, game):
        self.score_txt = "score: " + str(game.score)
        self.score_surface = self.gamefont.render(self.score_txt, False, (255, 255, 255))
        self.screen.blit(self.score_surface, (0, 0))

    def flip_display(self):
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill((0, 0, 0))