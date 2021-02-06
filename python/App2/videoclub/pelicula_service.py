from pelicula import Pelicula


class PeliculaService():
    def __init__(self, repository):
        self.repository = repository

    def listar(self):
        print("\n     Listando")
        for key in self.repository.peliculas:
            print("-> %s" % (self.repository.peliculas[key]))

    def agregar_pelicula(self):
        print("\n     Agregando")
        pelicula = Pelicula()
        pelicula.ingresar()
        self.repository.peliculas[pelicula.key] = pelicula

    def eliminar(self):
        print("\n     Eliminando")
        key = input("Ingrese código a Eliminar: ")
        del self.repository.peliculas[key]

    def modificar(self):
        print("\n     Modificando")
        key = input("Ingrese código a Modificar: ")
        pelicula = self.repository.peliculas[key]
        print("Pelicula %s " % pelicula)
        pelicula.ingresar(True)
        self.repository.peliculas[key] = pelicula
