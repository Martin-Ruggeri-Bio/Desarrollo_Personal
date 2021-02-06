# import scripts
import doctest


class Areas:
    """ comentario de
        muchas lineas de la clase"""
    def areaCuadrado(lado):
        """ comentario de
        muchas lineas del cuadrado"""
        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """ comentario de
        muchas lineas del triangulo
        >>> Areas.areaTriangulo(3, 2)
        'El area del triangulo es: 3.0'"""
        return "El area del triangulo es: " + str((base*altura)/2)


print(Areas.areaCuadrado(3))
print(Areas.areaTriangulo(3, 2))
# print(areaCuadrado.__doc__)
# help(areaCuadrado)
# help(Areas.areaTriangulo)
# help(Areas)
# help(scripts)
doctest.testmod()
