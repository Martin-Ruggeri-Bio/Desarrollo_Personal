class UnoError(Exception):
    def __init__(self, valor):
        self.valorError = valor

    def __str__(self):
        print("No se puede dividir por 1", self.valorError)


d = 5
n = 1
try:
    if n == 1:
        raise UnoError(d)
    print(d/n)
except UnoError:
    print("se intento dividir por uno")
except TypeError:
    print("Error en tipo de dato")
except NameError:
    print("variable no existe")
except ZeroDivisionError as ex:
    print(ex)
    print("No se puede dividir por 0")
else:
    print("No hubo error")
finally:
    print("me ejecuto pase lo que pase")
print("Adios")
