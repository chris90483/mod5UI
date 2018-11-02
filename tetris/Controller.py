import snake.Game
import snake.SnakeUI
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
        self.ui = snake.SnakeUI.SnakeUI(screen, gamefont)
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
                        self.game.move_current("back")

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
                self.game.get_board_as_sendable()
                # communication
                #to_send = self.game.get_board_as_sendable()
                #communication.matrixcomm(to_send)
        self.ui.show_final(self.game)
        #communication.cleanup()