#!/usr/bin/env python3

# does not work - add to PATH in linux
# works -> './f'
# pygame transparent screen when run from explorer

#202408032257-Polesovice


# PYCHARM


import pygame
from sys import exit as sys_exit

SCA = 5

def putTile(file, coords):
    img = pygame.image.load(file).convert_alpha()
    # load all images just once, then just copy them (directly place)
    #    img = pygame.transform.scale_by(img, (SCA, SCA))
    surf_board.blit(img, coords)


oc = "basetile.png"
hx = "hextempl.png"

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

surf_board = pygame.Surface((W, H))

"""
* HANDLE FULLSCREEN LOGIC,
* calculate 'SCA' scalar accordingly to user's display
"""

tileSize = 32
tilesRange = 7
mindim = min(W, H)
SCALE = mindim/tilesRange//tileSize # rounddown
# capitals?

s = SCALE
print("scale:", s)
# test! vary! check tiling!


def draw_map_ocean(w, h):
    x_off, y_off = 450, 50
    hor_con, ver_con = 8, 4
    for c in range(w):
        if c % 2 == 0:
            for r in range(h):
                x = x_off + c*(d-hor_con*s)
                y = y_off + r*(d-ver_con*s)
                putTile(hx, (x,y))
        else:
            for r in range(h):
                x = x_off + c*(d-hor_con*s)
                y = y_off + r*(d-ver_con*s) + d//2 - 2*s
                putTile(hx, (x, y))
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
surf_board.blit(img, ((1920-w)//2, 1080-h))

screen.blit(surf_board, (0,0))



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




