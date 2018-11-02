from raindrops.RainUI import RainUI
from raindrops.Model import Model
import pygame
import time


class Controller:
    rainUI = None
    model = None
    screen = None
    gamefont = None

    def __init__(self, screen, gamefont):
        self.screen = screen
        self.gamefont = gamefont
        self.rainUI = RainUI(screen, gamefont)
        self.model = Model()

    def start(self):
        self.model.step()
        self.rainUI.draw(self.model.cube)

        start = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.rainUI.clear_screen()
                        return
                    elif event.key == pygame.K_KP_PLUS:
                        self.rainUI.framerate += 0.2
                    elif event.key == pygame.K_KP_MINUS:
                        if not self.rainUI.framerate - 0.2 < 0.1:
                            self.rainUI.framerate -= 0.2
            exe_time = time.time() - start
            if exe_time > (1 / self.rainUI.framerate):
                print(self.rainUI.framerate)
                self.model.step()
                self.rainUI.draw(self.model.cube)
                start = time.time()

