import pygame
import snake.Game

# setup thingsy things
def main(screenarg, fontarg):
    gamefont = fontarg
    screen = screenarg

    snake_game = snake.Game.SnakeGame()
    snake_game.setup_board()
    score_txt = "score: " + str(snake_game.score)

    score_surface = gamefont.render(score_txt, False, (255, 255, 255))
    screen.blit(score_surface, (0,0))


    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    screen.fill((0, 0, 0))
                    return

        pygame.display.flip()
