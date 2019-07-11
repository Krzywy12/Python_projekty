#zapisac w pliku csv liste

import csv

lista = [["Top gun", "Ocean's Eleven","Raport mniejszosci"],
        ["Titanic", "Ostatni Jedi", "Incepcja"],
        ["Pulp Fiction","Czlowiek w ogniu","Seksmisja"]]

with open("filmy.csv","w") as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(lista[0])
    write.writerow(lista[1])
    write.writerow(lista[2])
