loggeado = True


class Decorador(object):
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *args, **kwargs):
        print("Se crea el objeto operacion")
        self.funcion(*args, **kwargs)


def descripcion(funcion):
    def funcionDecorada(*args, **kwargs):
        print("Funcion ejecutada", funcion.__name__)
        funcion(*args, **kwargs)
    return funcionDecorada


def admin(funcion):
    def comprobar(*args, **kwargs):
        if loggeado:
            funcion(*args, **kwargs)
        else:
            print("No tiene permisos de ejecutar ",
                  funcion.__name__)
    return comprobar


@admin
@Decorador
@descripcion
def resta(n, m):
    print(n - m)


resta(5, 3)
