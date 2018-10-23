import snake.Game
import snake.snakeUI
import pygame
import time
#import communication


class Controller:

    gamefont = None
    game = None
    ui = None

    def __init__(self, screen, gamefont):
        self.gamefont = gamefont
        self.game = snake.Game.SnakeGame()
        self.ui = snake.snakeUI.SnakeUI(screen, gamefont)
        #communication.setup()

    def start(self):
        self.game.update_board()
        self.ui.draw_board(self.game.board)
        self.ui.flip_display()

        start_milis = time.time()
        while not self.game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.ui.clear_screen()
                        return
                    elif event.key == pygame.K_w:
                        self.game.heading = "y+"
                    elif event.key == pygame.K_a:
                        self.game.heading = "x+"
                    elif event.key == pygame.K_s:
                        self.game.heading = "y-"
                    elif event.key == pygame.K_d:
                        self.game.heading = "x-"
                    elif event.key == pygame.K_z:
                        self.game.heading = "z+"
                    elif event.key == pygame.K_c:
                        self.game.heading = "z-"

            # code after the if only gets executed once every frame
            exe_time = time.time() - start_milis
            if exe_time > (1 / self.ui.frame_rate):

                # local screen updates
                self.ui.clear_screen()
                self.game.update_board()
                self.ui.draw_board(self.game.board)
                self.ui.show_score(self.game)
                self.ui.flip_display()
                start_milis = time.time()

                # communication
                #to_send = self.game.get_board_as_sendable()
                #communication.matrixcomm(to_send)
        self.ui.show_final(self.game)
        #communication.cleanup()