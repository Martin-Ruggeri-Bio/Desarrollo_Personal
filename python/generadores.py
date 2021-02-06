def generador(*args):
    """recibe n argumentos y devuelve cada uno * 10"""
    for valor in args:
        yield valor * 10, True


documentacion = generador.__doc__
nombre = generador.__name__
print(nombre, ":")
print(documentacion, "\n")

for valor, validacion in generador(1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(valor, validacion)


def factorial(n):
    i = 1
    while n > 1:
        i = n * i
        yield i
        n -= 1


print("otra funcion")
for e in factorial(5):
    print(e)
