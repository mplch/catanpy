import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))



imp = pygame.image.load("oceano128.png").convert()
screen.blit(imp, (100, 0))
# pygame.display.flip() 

screen.blit(pygame.image.load("verti128.png").convert(), (0, 100))


pygame.display.flip()



run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()