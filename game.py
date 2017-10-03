import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((HEIGHT, WIDTH),
                                 pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Snake")

block_size = 10
FPS = 30
speed = 10
block_size = 10
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def msg_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [(WIDTH / 2 - len(msg)), HEIGHT / 3])


def gameLoop():
    gameExit = False
    gameOver = False

    x = WIDTH / 2
    y = HEIGHT / 2
    dx = 0
    dy = 0

    randx = random.randrange(0, WIDTH - block_size)
    randy = random.randrange(0, HEIGHT - block_size)

    while not gameExit:
        while gameOver == True:
            screen.fill(white)
            msg_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -speed
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = speed
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -speed
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = speed
                    dx = 0
                    # if event.type == pygame.KEYUP:
                    #	dx,dy=0,0

        if x >= HEIGHT or x < 0 or y >= WIDTH or y < 0:
            gameOver = True

        x += dx
        y += dy

        screen.fill(black)
        pygame.draw.rect(screen, red, [randx, randy, block_size, block_size])
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
