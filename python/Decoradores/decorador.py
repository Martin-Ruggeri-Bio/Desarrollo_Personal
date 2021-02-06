def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("vamos a realizar un calculo")
        funcion_parametro()
        print("hemos teerminado el calculo")
    return funcion_interior


@funcion_decoradora
def suma():
    print(15+20)


@funcion_decoradora
def resta():
    print(20-15)


resta()
suma()
