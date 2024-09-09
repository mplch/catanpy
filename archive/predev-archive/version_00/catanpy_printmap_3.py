import string

TILE_TYPES = "F P M C E D S".split(' ')
TILE_BACKCOL = "D_GREEN L_GREEN GRAY ORANGE YELLOW WHITE BLUE".split(' ')
TILE_BACKCOL = "CYAN GREEN BLACK RED YELLOW WHITE BLUE".split(' ')
TILE_TYPE_BG_CLRS = dict(zip(TILE_TYPES, TILE_BACKCOL))

# use colorist package / library...
# or write primitive one of my own??
## Maybe not needed in this phase, i just need proof of concept.

ANSI_CLR_NAMES = "BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE".split(' ')

START_BG_DARK = 40
START_BG_BRIGHT = 100
s = START_BG_DARK

ANSI_CLRS = dict()

for i, clr in enumerate(ANSI_CLR_NAMES):
    c = s + i
    c = 100 if (c==40) else c ## bright black for visibility
    # ANSI_CLRS[clr] = "\033[{c}m\033[K"
    ANSI_CLRS[clr] = ""
    ANSI_CLRS[clr] += "\033["
    ANSI_CLRS[clr] += str(c)
    ANSI_CLRS[clr] += "m\033[K"

# print(ANSI_CLRS)



"""
D_GREEN = "\033[{c}m\033[K"
L_GREEN
GRAY
ORANGE
YELLOW
WHITE
BLUE
"""

# RED = "\033[91m\033[K"
# GRE = "\033[32m\033[K"
# YEL = "\033[33m\033[K"
# BLU = "\033[34m\033[K"
END = "\033[m\033[K"

map_xmpl = """
      
      0 2  .  4 6    8 0    2 4

00      >-----<        >----*  
       /       \      /      \ 
02    <   6 P   >----<   2F   *
       \       /      \      / 
04      > --- <   4F   >----*  
       /       \      /      \ 
02    *   3 P   *----*   9C   o
       \       /      \      / 
04      * --- *   8M   R-r--o  
       b       \      /      r 
02    BV  11C   o -- o   5F   o
       \       y      \      / 
04      *--y--YM       *r---*  

"""

# print(map_xmpl)

def isNumber(char):
    if char in list(range(10)):
        return True
    return False

def isTileType(char):
    ret = True if char in TILE_TYPES else False
    return ret

# COLOR_BACK = {
#     "F P M C E D S"

    ## delam miliardy kopii a zaloh..
    ## Cely a JEDINY duvod je cas, coz je nesmysl,
    ## to chce resit lepe..
    ## Plus to stale neni na gitu..

def colorize_back(char):
    ret = ""
    ret += ANSI_CLRS[TILE_TYPE_BG_CLRS[char]]
    ret += char
    ret += END
    # return char ## kamoo :D
    return ret


def printmap(mapstr):
    #bool state_number = False
    state_number = False;
    for i, symb in enumerate(mapstr):
        # // Mozna bych namisto for loopu chtel pouzivat replace
        # Jak realne funguje replace pod kapotou? Vektorizace?
        # Nastudovat kdyztak pozdeji. -> Oznaceni? (symbol) ?
        # switch v pythonu evidentne neni
        """
        if isNumber(symb):
            if (mapstr[i+1] == '1'):
                ## number = 10, 11, 12
                pass
            mapstr[i+2]
            ## !!! Tohle lepsi resit stavovou masinou!
        """

        """
        if state_number:
            state_number = False # ?
            if mapstr[i+1] is NOT number...
        ## ! Tuhle cekovacku cisel asi taky nemusim delat..
        ## Pokud ovsem nechci podbarovat i cislo,
        ## pripadne celou dlazdici.. Ale to nechme na pozdeji
        ## zbytecna komplikace nyni..

        state_number = isNumber(symb)
        """
        
        if isTileType(symb):
            symb = colorize_back(symb)
        
        print(symb, end='')
    print() #('\n')

printmap(map_xmpl)