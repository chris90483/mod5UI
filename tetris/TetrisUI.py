import pygame
import math
import snake.Game


class TetrisUI:
    gamefont = None
    screen = None
    score_txt = None
    score_surface = None
    frame_rate = 0.5

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
        self.score_txt = "score: " + str(game.score) + " Press q to quit"
        self.score_surface = self.gamefont.render(self.score_txt, False, (255, 255, 255))
        self.screen.blit(self.score_surface, (0, 0))

    def show_final(self, game):
        self.clear_screen()
        width, height = pygame.display.get_surface().get_size()
        width, height = math.floor(0.5 * width) - 100, math.floor(0.5 * height)
        self.score_txt = "Game over! Final score: " + str(game.score)
        self.score_surface = self.gamefont.render(self.score_txt, False, (255, 255, 255))
        self.screen.blit(self.score_surface, (width, height))
        self.flip_display()
        keydown = False
        while not keydown:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keydown = True
        self.clear_screen()
        self.flip_display()

    def flip_display(self):
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill((0, 0, 0))
