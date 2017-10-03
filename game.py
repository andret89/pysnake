import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((HEIGHT, WIDTH),
                                 pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Snake")

block_size = 10
apple_size = 15
FPS = 30
speed = 10

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def msg_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [(WIDTH / 2 - len(msg)), HEIGHT / 3])


def snake(block_size, snakelist):
    for i in snakelist:
        pygame.draw.rect(screen, green, [i[0], i[1], block_size, block_size])


def gameLoop():
    gameExit = False
    gameOver = False

    x = WIDTH / 2
    y = HEIGHT / 2
    dx = 0
    dy = 0

    snakeList = []
    snakeLength = 1
    randx = round(random.randrange(0, WIDTH - block_size)) #/ 10.0) * 10.0
    randy = round(random.randrange(0, HEIGHT - block_size)) # / 10.0) * 10.0

    while not gameExit:
        while gameOver == True:
            screen.fill(black)
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
        pygame.draw.rect(screen, red, [randx, randy, apple_size, apple_size])

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for elm in snakeList[:-1]:
            if elm == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()


        if x > randx and x < randx + apple_size or x + block_size > randx and x + block_size < randx + apple_size:
            if y > randy and y < randy + apple_size or y + block_size > randy and y + block_size < randy + apple_size:
                randx = round(random.randrange(0, WIDTH - apple_size)) #/ 10.0) * 10.0
                randy = round(random.randrange(0, HEIGHT - apple_size)) #/ 10.0) * 10.0
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
