x = input("Podaj liczbe calkowita: ")
x = int(x)

def f(x):
    """
    zwraca x // 2
    :param x: int.
    :return: int x // 2
    """

    return x // 2

result = f(x)

def g(result):
    """
    zwraca result * 4
    :result: int
    :return: int result * 4
    """
    return result * 4

ostateczny_result = g(result)
print(ostateczny_result)
