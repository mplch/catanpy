import maps # ??

# KOLIZE - Mesto M a Mountains M !!


#----------------------------------------------------------------------
 
TILE_TYPES = "F P M C E D S".split(' ')
# TILE_BACKCOL = "D_GREEN L_GREEN GRAY ORANGE YELLOW WHITE BLUE".split(' ')
TILE_BACKCOL = "CYAN GREEN BLACK RED YELLOW WHITE BLUE".split(' ')
TILE_TYPE_BG_CLRS = dict(zip(TILE_TYPES, TILE_BACKCOL))

ANSI_CLR_NAMES = "BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE".split(' ')

START_BG_DARK = 40
START_BG_BRIGHT = 100
s = START_BG_DARK

ANSI_CLRS = dict()

for i, clr in enumerate(ANSI_CLR_NAMES):
    c = s + i
    c = 100 if (c==40) else c ## bright black for visibility
    ANSI_CLRS[clr] = f"\033[{c}m\033[K"

END = "\033[m\033[K"


#----------------------------------------------------------------------

# def isNumber(char):
#     if char in list(range(10)):
#         return True
#     return False

def isTileType(char):
    ret = True if char in TILE_TYPES else False
    return ret

def colorize_back(char):
    ret = ""
    ret += ANSI_CLRS[TILE_TYPE_BG_CLRS[char]]
    ret += char
    ret += END
    return ret


def printmap(mapstr):
    # state_number = False
    for i, symb in enumerate(mapstr):

        if isTileType(symb):
            symb = colorize_back(symb)
        
        print(symb, end='')
    print() #('\n')

#----------------------------------------------------------------------

printmap(map_xmpl)