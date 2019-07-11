import re

zen = """Lepiej teraz niz nigdy.
Choc zazwyczaj
nigdy
jest lepsze od *juz* teraz.
Jesli trudno ci wyjasnic implementacje,
to jej uzycie bedzie zlym pomyslem.
Jesli jednak latwo ci ja wyjasnic,
to moze jes warta zachodu?
"""
m = re.findall("nigdy$",zen,re.MULTILINE)

print(m)
