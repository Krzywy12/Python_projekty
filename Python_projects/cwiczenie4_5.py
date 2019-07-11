#	funkcja wyswietlajaca lancuch znakow
try:
    x = input("podaj liczbe:")
    x = float(x)
    print(x)
except (ValueError,NameError):
    print("Nieprawidlowe dane")
