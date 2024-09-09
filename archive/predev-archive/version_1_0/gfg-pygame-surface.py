
# Importing the library
import pygame
import time
   
# Initializing Pygame
pygame.init()
   
# Creating the surface
sample_surface = pygame.display.set_mode((400,300))
   
# Choosing red color for the rectangle
color = (255,255,0)
   
# Drawing Rectangle
pygame.draw.rect(sample_surface, color, 
                 pygame.Rect(30, 30, 60, 60))
 
# The pygame.display.flip() method is used 
# to update content on the display screen
pygame.display.flip()
