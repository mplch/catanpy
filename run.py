#!/usr/bin/env python3

# does not work - add to PATH in linux
# works -> './f'
# pygame transparent screen when run from explorer

#202408032257-Polesovice

import pygame

SCA = 5

def putTile(file, coords):
	img = pygame.image.load(file).convert_alpha()
#	pygame.transform.scale(img, (128, 128))
	img = pygame.transform.scale_by(img, (SCA, SCA))
	screen.blit(img, coords)

oc = "basetile.png"

d = 160
s = 5  # scale: 5*32=160

#--------------------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

# for c in range(5):
for i in range(5):
    putTile(oc, (0, i*(d-4*5)))

for i in range(5):
    putTile(oc, (d - 8*s, i*(d-4*s) + d//2 - 2*s))

for i in range(5):
    putTile(oc, (2*(d-8*s), i*(d-4*s)))

for i in range(5):
    putTile(oc, (3*(d-8*s), i*(d-4*s) + d//2 - 2*s))

for i in range(5):
    putTile(oc, (4*(d-8*s), i*(d-4*s)))


pygame.display.flip()



run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


pygame.quit()





