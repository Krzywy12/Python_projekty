qs = ["Jak masz na imie?: ",
      "Jaki jest twoj ulubiony kolor?: ",
      "Jakie masz zadanie?:"]
n = 0
while True:
    print("Wpisz q,aby zakonczyc")
    a = input(qs[n])
    if a == 'q':
        break
    n = (n+1) % 3

