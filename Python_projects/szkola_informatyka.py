#Program sprawdzajacy czy liczba jest liczba pierwsza
n = input("Podaj liczbe ,a ja powiem czy jest liczba pierwsza?: ") # n>2
n = int(n)
k = n-1

for i in range(2,n):
    if n%i == 0:
        print("Nie")
        break
    else:
        if k == i:
            print("Tak")
            break
        else:
            i += 1
