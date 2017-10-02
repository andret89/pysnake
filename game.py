import pygame, os, sys

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((HEIGHT,WIDTH),
	pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Esempio 01")




block_size = 10
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,25)

def msg_to_screen(msg,color):
	screen_text = font.render(msg,True,color)
	screen.blit(screen_text,[WIDTH/2,HEIGHT/2])


def gameLoop():
	gameExit = False

	x,y=WIDTH/2,HEIGHT/2
	dx,dy=0,0
	speed = 10
	FPS = 30

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					dx = -speed
					dy = 0
				elif event.key == pygame.K_RIGHT:
					dx =speed
					dy = 0
				elif event.key == pygame.K_UP:
					dy = -speed
					dx = 0
				elif event.key == pygame.K_DOWN:
					dy =speed
					dx = 0
			#if event.type == pygame.KEYUP:
			#	dx,dy=0,0

		if dx >= HEIGHT or dx < 0 or dy >= WIDTH or dy < 0:
			gameExit = True


		x += dx
		y += dy
			#else:
			#	print(event)
		screen.fill(black)
		pygame.draw.rect(screen, green,[x,y,10,10])
	#	pygame.draw.rect(screen, red,[400,300,10,10])
	#	screen.fill(red,rect=[10,10,10,10])

		pygame.display.update()
		clock.tick(FPS)

msg_to_screen("You Lose",red)
pygame.display.update()

pygame.quit()
quit()