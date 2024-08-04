COLOR_COUNT = 4
COLOR_HEAD = []
for i in range(COLOR_COUNT):
	COLOR_HEAD.append('')
	COLOR_HEAD[i] += "\033["
	COLOR_HEAD[i] += str(i+91)
	COLOR_HEAD[i] += "m\033[K"
COLOR_TAIL = "\033[m\033[K"
COLOR_NAMES = "RED GREEN BLUE ORANGE".split(' ')


for clr in COLOR_HEAD:
	print(COLOR_HEAD, "RANDOM COLOR TEXT!!", COLOR_TAIL)
