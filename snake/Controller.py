import snake.Game
import snake.SnakeUI
import pygame
import time
import communication


class Controller:

    gamefont = None
    game = None
    ui = None
    cube_cont = True 
    
    def __init__(self, screen, gamefont):
        self.gamefont = gamefont
        self.game = snake.Game.SnakeGame()
        self.ui = snake.SnakeUI.SnakeUI(screen, gamefont)
        communication.setup()

    def start(self):
        self.game.update_board()
        self.ui.draw_board(self.game.board)
        self.ui.flip_display()

       
        start_milis = time.time()
        while not self.game.game_over:
            # Where [0] is head, [1] is neck
            snake_neck = self.game.get_neck()
            possible_moves = [ snake_neck[1] != [snake_neck[0][0], snake_neck[0][1]+1, snake_neck[0][2]], snake_neck[1] != [snake_neck[0][0], snake_neck[0][1], snake_neck[0][2]+1], snake_neck[1] != [snake_neck[0][0], snake_neck[0][1]-1, snake_neck[0][2]], snake_neck[1] != [snake_neck[0][0], snake_neck[0][1], snake_neck[0][2]-1], snake_neck[1] != [snake_neck[0][0]+1, snake_neck[0][1], snake_neck[0][2]], snake_neck[1] != [snake_neck[0][0]-1, snake_neck[0][1], snake_neck[0][2]]]

            if self.cube_cont:
                for i in range(0,6):
                    #for when we have communication imported
                    if communication.queryController(i):
                        if i == 0 and possible_moves[0]:
                            self.game.heading = "y+"
                        elif i == 1 and possible_moves[1]:
                            self.game.heading = "x+"
                        elif i == 2 and possible_moves[2]:
                            self.game.heading = "y-"
                        elif i == 3 and possible_moves[3]:
                            self.game.heading = "x-"
                        elif i == 4 and possible_moves[4]:
                            self.game.heading = "z+"
                        elif i == 5 and possible_moves[5]:
                            self.game.heading = "z-"
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.ui.clear_screen()
                        return
                    elif not self.cube_cont:
                        if event.key == pygame.K_w and possible_moves[0]:
                                self.game.heading = "y+"
                        elif event.key == pygame.K_a and possible_moves[1]:
                                self.game.heading = "x+"
                        elif event.key == pygame.K_s and possible_moves[2]:
                                self.game.heading = "y-"
                        elif event.key == pygame.K_d and possible_moves[3]:
                                self.game.heading = "x-"
                        elif event.key == pygame.K_z and possible_moves[4]:
                                self.game.heading = "z+"
                        elif event.key == pygame.K_c and possible_moves[5]:
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
                self.game.get_board_as_sendable()
                # communication
                to_send = self.game.get_board_as_sendable()
                communication.matrixcomm(to_send)
        self.ui.show_final(self.game)
        communication.cleanup()
