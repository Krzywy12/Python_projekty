#program dzieli dwie liczby podane przez uzytkownika

try:
    a = input("podaj liczbe: ")
    b = input("podaj druga liczbe: ")
    a = int(a)
    b = int(b)
    print(a/ b)
except (ZeroDivisionError, ValueError, NameError):
    print("Nieprawidlowe dane wejsciowe.")

