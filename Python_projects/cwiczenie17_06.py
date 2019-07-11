import re

text = """Zyrafy od samego momentu odkrycia
 stanowia __RZECZOWNIK_LPOJ__ swiata zwierzat.
 Sa one najwyzszymi ze wszystkich zyjacych
 na swiecie __RZECZOWNIK_LMNOGA__, jednak
 naukowcy nie sa w sanie wyjasnic, w jaki
 sposob ich __CZESC_CIALA__ stala sie tak
 dluga.Zyrafy zawdziedzaja swoja niesamowita
 wysokosc, ktora moze dochodzic do
 __LICZBA__ __RZECZOWNIK_LMNOGA__, swoim
 nogom i __CZESC_CIALA__.
    """

def mad_libs(mls):
    """
    :param mls: lancuch znakow,
    zawierajacy czesci otoczone podwojnymi
    znakami podkreslenia, ktore uzytkownik
    powinien zastapic samodzielnie wybranymi
    slowami. W sugestiach nie mozna
    umieszczac znakow podkreslenia; np:
    nie __to_sugestia__, tylko
    __sugestia__.

    """

    hints = re.findall("__.*?__", mls)

    if hints is not None:
        for word in hints:
            q = "Wpisz {}:"\
                    .format(word)
            new = input(q)
            mls = mls.replace(word,new,1)
            print("\n")
            mls = mls.replace("\n","")
            print(mls)
    else:
        print("Nieprawidlowy parametr mls")

mad_libs(text)
