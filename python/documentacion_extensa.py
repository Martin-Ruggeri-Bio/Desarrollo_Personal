import math
import doctest


def raizCuadrada(listaNumeros):
    """
    La funcion devuelve una lista con
    la raiz cuadrada de los elementos numericos
    pasados por parametros en otra lista
    >>> lista = []
    >>> for i in [9, 16, 25, 36]
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    '[3.0, 4.0, 5.0, 6.0]'
    """

    return [math.sqrt(n) for n in listaNumeros]


# print(raizCuadrada([9, 16, 25, 36]))
doctest.testmod()
