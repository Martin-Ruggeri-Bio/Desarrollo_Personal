class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre

    def getPersonaje(self):
        print("\n")
        return "Nombre: %s" % (
                self.nombre)

    def getDiccPersonaje(self):
        return self.__dict__
