def get_node_pix_coord(hex_coord, orientation):
    pass

"""
Jedna vec je pristup z tily,
jina vec je pristup z cele mapy.
Kreje se to.

Takze bych mozna udelat nejprve celkovy overlay,
pak bych udelal overlay jednotlivych hexu.
A pak bych nejakym zpusobem nachazel prunik.

Bez toho celkového pohledu se nehnu
a navic by to bylo peklo zkoordinovat.

Pripomina mi to, ze stale nemam reprezentaci ani mapy.

Dejme tomu, ze se budou postupne, asi po radach (sloupcich)
- snad to hexy prilis nerozbori svou "clenitosti" -
- no a pak budu mít funkci, ktera se mi "zepta", jake hexy jsou v okoli.

Potrebuji pix_coordy vsech nod ( cest )...


Jo, jenze jeste je ale vtipne, ze...necentricke souradnice.
Jako teoreticky, v pripade ctvercovych spritu,
nejde o nic jineho, nez o pricteni poloviny hrany v obou smerech,
respektive naopak v pripade pokladani.
Otazka zni, jestli se ma v pripade nody a cesty bavit o stredu...
...kdyz velikost jejich hrany je SUDE cislo.

Mozna to vidim tak, ze zas proste experimentalne vyladim offsety..

"""