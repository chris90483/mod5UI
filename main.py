import pygame
import snake.snakeUI

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
gamefont = pygame.font.SysFont('Arial', 30)

def main():
    terminate = False

    select_txt = "Welcome! select game:"
    snake3d_txt = "1. Snake 3D"

    select_surface = gamefont.render(select_txt, False, (255, 255, 255))
    snake3d_surface = gamefont.render(snake3d_txt, False, (255, 255, 255))

    screen.blit(select_surface, (0,0))
    screen.blit(snake3d_surface, (0, 32))

    # main loop
    while not terminate:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate = True
                elif event.key == pygame.K_1:
                    start_snake_game()

        pygame.display.flip()

# functions
def start_snake_game():
    screen.fill((0, 0, 0))
    snake.snakeUI.main(screen, gamefont)
    main()

main()
