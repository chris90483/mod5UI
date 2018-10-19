import pygame
import snake.snakeUI

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
gamefont = pygame.font.SysFont('Arial', 20)


def main():
    terminate = False
    draw_main_menu()

    # main loop
    while not terminate:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate = True
                elif event.key == pygame.K_1:
                    start_snake_game()
                    draw_main_menu()

        pygame.display.flip()


# functions
def start_snake_game():
    screen.fill((0, 0, 0))
    ui = snake.snakeUI.SnakeUI(screen, gamefont)
    ui.start()


def draw_main_menu():
    select_txt = "Welcome! select game:"
    snake3d_txt = "1. Snake 3D"

    select_surface = gamefont.render(select_txt, False, (255, 255, 255))
    snake3d_surface = gamefont.render(snake3d_txt, False, (255, 255, 255))

    screen.blit(select_surface, (0, 0))
    screen.blit(snake3d_surface, (0, 22))


main()
