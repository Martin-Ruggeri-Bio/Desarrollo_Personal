def funcion_decoradora(funcion_parametro):
    # puede recibir parametros con kay_worth (clave_valor)
    def funcion_interior(*args, **kwargs):
        print("vamos a realizar un calculo")
        funcion_parametro(*args, **kwargs)
        print("hemos teerminado el calculo")
    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)


@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)


@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


resta(10, 2)
suma(10, 2, 3)
potencia(base=5, exponente=3)
potencia(exponente=3, base=5)
