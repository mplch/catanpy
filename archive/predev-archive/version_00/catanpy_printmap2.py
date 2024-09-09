import string

TILE_TYPES = "F P M C E D S".split(' ')

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

print(map_xmpl)

def isNumber(char):
    if char in list(range(10)):
        return True;
    return False;

def isTileType(char):
    ret = True if char in TILE_TYPES else False
    return ret

def printmap(mapstr):
    #bool state_number = False;
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
            state_number = False; # ?
            if mapstr[i+1] is NOT number...
        ## ! Tuhle cekovacku cisel asi taky nemusim delat..
        ## Pokud ovsem nechci podbarovat i cislo,
        ## pripadne celou dlazdici.. Ale to nechme na pozdeji
        ## zbytecna komplikace nyni..

        state_number = isNumber(symb)
        """


