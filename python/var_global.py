def valor_global():
    global var_global
    var_global = "Cambiar valor"


def mostrar_global():
    # print(var_global)
    var_global = "hola"
    print(var_global)


def crear_var_global():
    global new_var
    new_var = "new var"


var_global = "var global"
mostrar_global()
valor_global()
crear_var_global()
print(var_global)
print(new_var)
