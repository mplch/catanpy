#!/usr/bin/env python3

# does not work - add to PATH in linux
# works -> './f'
# pygame transparent screen when run from explorer

#202408032257-Polesovice

import pygame
from sys import exit as sys_exit

SCA = 5

def putTile(file, coords):
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale_by(img, (SCA, SCA))
    screen.blit(img, coords)


oc = "basetile.png"

d = 160
s = 5  # scale: 5*32=160
"""
* (!!!) changing value messes up grid
* mozna bych nejprve nahazel policka mapy na canvas
* a pak skaloval cely canvas -->
* --> coz ovsem ale nevyresi pozdejsi pokladani budov
* je potreba spravne zadefinovat transformacni souradnicove funkce
"""


#--------------------------------------------------------------

pygame.init()

#screen = pygame.display.set_mode((1920, 1080))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
W, H = screen.get_size()
print(f"Screen size: {W} x {H}")

"""
* HANDLE FULLSCREEN LOGIC,
* calculate 'SCA' scalar accordingly to user's display
"""


def draw_map_ocean(w, h):
    x_off, y_off = 450, 50
    for c in range(w):
        if c % 2 == 0:
            for i in range(h):
                putTile(oc, (x_off + c*(d-8*s), y_off + i*(d-4*s)))
        else:
            for i in range(h):
                putTile(oc, (x_off + c*(d-8*s), y_off + i*(d-4*s) + d//2 - 2*s))
    """
    * nenapada me, jak nejak hezky udelat stridani...
    * teoreticky reasignment, ale na to stejne potrebuji vetve
    * takto je to mozna nejprehlednejsi
    * funguje to? funguje!
    """
        
    
draw_map_ocean(7, 6)


# bottom_bar
img = pygame.image.load("bar.png").convert_alpha()
w, h = img.get_size()
screen.blit(img, ((1920-w)//2, 1080-h))


pygame.display.flip()



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys_exit()




