class Pelicula():
    def __init__(self, titulo, duracion, genero, actores):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.actores = actores

    def getPelicula(self):
        return "\nTitulo: %s, Duracion: %d, Genero: %s, Actores: %s" % (
                self.titulo, self.duracion, self.genero, self.actores)

    def getDiccPelicula(self):
        return self.__dict__


if __name__ == "__main__":
    peli = Pelicula("test", 20, "nada", "")
    print(peli.getPelicula())
