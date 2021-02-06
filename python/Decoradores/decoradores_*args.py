def funcion_decoradora(funcion_parametro):
    # puede recibir un numero indeterminado de parametros a las 2 fc
    def funcion_interior(*args):
        print("vamos a realizar un calculo")
        funcion_parametro(*args)
        print("hemos teerminado el calculo")
    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)


@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)


resta(10, 2)
suma(10, 2, 3)
