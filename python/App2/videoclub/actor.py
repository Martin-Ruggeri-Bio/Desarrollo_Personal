class Actor():
    def __init__(self, key="", nombre=""):
        self.key = key
        self.nombre = nombre

    def __str__(self):
        return "%s %s" % (self.key, self.nombre)

    def ingresar(self, modificar=False):
        print("Ingresando Actor/Actriz")
        if not modificar:
            self.key = input("Key: ")
        self.nombre = input("Ingrese Nombre: ")
