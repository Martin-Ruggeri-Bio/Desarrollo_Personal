class Pelicula():
    def __init__(self, key="", title="", duracion=0, genero="", actores=None):
        self.key = key
        self.title = title
        self.duracion = duracion
        self.genero = genero
        self.actores = {}

    def __str__(self):
        linea = "%s %s %d %s" % (self.key, self.title, self.duracion,
                                 self.genero)
        for key in self.actores:
            linea = "%s \n          -> %s" % (linea, self.actores[key])
        return linea

    def ingresar(self, modificar=False):
        print("Ingresando Pelicula")
        if not modificar:
            self.key = input("Key: ")
        self.title = input("Ingrese Titulo: ")
        self.duracion = int(input("Ingrese Duracion como número: "))
        self.genero = input("Ingrese Genero: ")
        key_actor = input("Key Actor 1: ")
        personaje = input("Personaje 1: ")
        self.actores[key_actor] = personaje
        key_actor = input("Key Actor 2: ")
        personaje = input("Personaje 2: ")
        self.actores[key_actor] = personaje
