import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))



# create a surface object, image is drawn on it.
imp = pygame.image.load("imaago.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (100, 0))
 
# paint screen one time
pygame.display.flip()



run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()