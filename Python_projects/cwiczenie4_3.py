#funkcja majaca 3 parametry wymagane i 3 parametry opcjonalne
def f(x , y, z, k=2, l= 3):
    """
    zwraca x + y + z + k +l
    :param x: int,float
    :param y: int,float
    :param z: int,float
    :param k: int,float
    :param l: int,float
    :return: int,float suma x, y, z, k, l
    """
    return x + y + z + k + l

result = f(2, 3 ,4.2, 6)
print(result)
