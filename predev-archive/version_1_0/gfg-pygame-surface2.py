
# Importing the library
import pygame
   
# Initializing Pygame
pygame.init()
   
# Creating the surface
sample_surface = pygame.display.set_mode((400,300))
   
# Choosing yellow color to fill
color = (255,255,0)
 
# filling color to the surface
sample_surface.fill(color)
 
# updating the display
pygame.display.flip()
