import pygame
import random
from deepin_utils import font

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


body = pygame.image.load('img/body.png')
tail = pygame.image.load('img/tail.png')
head = pygame.image.load('img/head.png')
img = pygame.image.load('img/head.png')
apple = pygame.image.load('img/apple.png')

block_size = 20
apple_size = 30
FPS = 15
speed = 20
direction = "dx"

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)



def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)

    elif size == "medium":
        textSurface = medfont.render(text, True, color)

    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def msg_to_screen(msg, color, x_space ,y_space, size="small"):
    textSurf , textRect = text_objects(msg,color, size)
    textRect.center = ((WIDTH/2)+x_space,(HEIGHT/3)+y_space)
    screen.blit(textSurf,textRect)

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        screen.fill(black)
        msg_to_screen("Welcome to SnaKe",
                      green,
                      y_space=-100,
                      x_space = 50,
                      size = "large")


        # msg_to_screen("The objective of the game is to eat red apples",
        #                   white,
        #               y_space=-30)
        #
        # msg_to_screen("The more apples you eat, the longer you get",
        #                   white,
        #               y_space=10)
        #
        # msg_to_screen("If you run into yourself, or the edges, you die!",
        #                   white,
        #               y_space=50)

        msg_to_screen("Press C to play or Q to quit.",
                          white,
                      x_space=50,
                      y_space=180,
                      size="medium")

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):

    if direction == "dx":
        head =  img
        body_r = body

    if direction == "sx":
        head =  pygame.transform.rotate(img ,180)
        body_r = pygame.transform.rotate(body, 180)

    if direction == "up":
        head = pygame.transform.rotate(img, 90)
        body_r = pygame.transform.rotate(body, 90)

    if direction == "down":
        head = pygame.transform.rotate(img, 270)
        body_r = pygame.transform.rotate(body, 270)

    screen.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for i in snakelist[:-1]:
        #pygame.draw.rect(screen, green, [i[0], i[1], block_size, block_size])
        screen.blit(body_r, (i[0], i[1]))



def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    x = WIDTH / 2
    y = HEIGHT / 2
    dx = 0
    dy = 0

    snakeList = []
    snakeLength = 1
    randx = round(random.randrange(1, (WIDTH - apple_size*2)+1)) #/ 10.0) * 10.0
    randy = round(random.randrange(1, (HEIGHT - apple_size*2)+1)) # / 10.0) * 10.0
    printo = True

    while not gameExit:
        while gameOver == True:
            screen.fill(black)
            msg_to_screen("Game over",
                          red,
                          x_space=50,
                          y_space=-50,
                          size="large")
            msg = "Press C to play again or Q to quit"
            msg_to_screen(msg,
                          white,
                          x_space=len(msg)*2,
                          y_space=50,
                          size="medium")
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
                    direction = "sx"
                    dx = -speed
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "dx"
                    dx = speed
                    dy = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    dy = -speed
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    dy = speed
                    dx = 0
                    # if event.type == pygame.KEYUP:
                    #	dx,dy=0,0

        if x >= HEIGHT or x < 0 or y >= WIDTH or y < 0:
            gameOver = True

        x += dx
        y += dy

        screen.fill(black)
        #pygame.draw.rect(screen, red, [randx, randy, apple_size, apple_size])
        if printo:
            print str(randx)+" " +str(randy)
            printo = False
            
        screen.blit(apple, (randx,randy))

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
                randx = round(random.randrange(0, (WIDTH - apple_size*2)+1)) #/ 10.0) * 10.0
                randy = round(random.randrange(0, (HEIGHT - apple_size*3)+1)) #/ 10.0) * 10.0
                snakeLength += 1
                printo = True

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
