import pygame
import snake.Controller
import raindrops.Controller
import tetris.Controller
import communication 

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
gamefont = pygame.font.SysFont('Arial', 20)
communication.setup()


def main():
    terminate = False
    draw_main_menu()
    communication.changeProgram(0)

    # main loop
    while not terminate:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate = True
                elif event.key == pygame.K_1:
                    start_snake_game()
                    draw_main_menu()
                elif event.key == pygame.K_2:
                    start_raindrops()
                    draw_main_menu()
                elif event.key == pygame.K_3:
                    start_tetris_game()
                    draw_main_menu()

        pygame.display.flip()
    pygame.quit()


# functions
def start_snake_game():
    screen.fill((0, 0, 0))
    controller = snake.Controller.Controller(screen, gamefont)
    communication.changeProgram(1)
    controller.start()

def start_tetris_game():
    screen.fill((0, 0, 0))
    controller = tetris.Controller.Controller(screen, gamefont)
    communication.changeProgram(3)
    controller.start()

def start_raindrops():
    screen.fill((0, 0, 0))
    pygame.display.flip()
    controller = raindrops.Controller.Controller(screen, gamefont)
    communication.changeProgram(2)
    controller.start()


def draw_main_menu():
    select_txt = "Welcome! Select application: [1-n] Quit: q"
    snake3d_txt = "1. Snake 3D"
    raindrops_txt = "2. Raindrops"
    tetris3d_txt = "3. Tetris 3D"

    select_surface = gamefont.render(select_txt, False, (255, 255, 255))
    snake3d_surface = gamefont.render(snake3d_txt, False, (255, 255, 255))
    raindrops_surface = gamefont.render(raindrops_txt, False, (255, 255, 255))
    tetris3d_surface = gamefont.render(tetris3d_txt, False, (255, 255, 255))

    screen.blit(select_surface, (0, 0))
    screen.blit(snake3d_surface, (0, 22))
    screen.blit(raindrops_surface, (0, 44))
    screen.blit(tetris3d_surface, (0, 66))


main()
