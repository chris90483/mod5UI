import pygame


class RainUI:

    screen = None
    gamefont = None
    framerate = 1

    def __init__(self, screen, gamefont):
        self.screen = screen
        self.gamefont = gamefont

    def draw(self, cube):
        self.clear_screen()
        for plane in cube:
            for row in plane:
                for val in row:
                    if val[1]:
                        # raindrop
                        pygame.draw.rect(self.screen, (255, 255, 255), val[0])
                    else:
                        # air
                        pygame.draw.rect(self.screen, (0, 0, 0), val[0])
        quit_surface = self.gamefont.render("Press q to quit | framerate: " + str(self.framerate)[:3] + " | use + and - to change", False, (255, 255, 255))
        self.screen.blit(quit_surface, (0, 0))
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill((0, 0, 0))
