rymy = {"1":"niebiem",
                   "2":"kwa kwa",
           "3":"spi",
                            "4":"ordery",
        "5":"ciec",
                  }

n = input("podaj liczbe: ")
if n in rymy:
    rym = rymy[n]
    print(rym)
else:
    print("Nie znaleziono.")

