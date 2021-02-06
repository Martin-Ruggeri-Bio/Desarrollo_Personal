from peliculaRepository import PeliculaRepository
from peliculaService import PeliculaService
from actorsService import ActorsService
from actorsRepository import ActorsRepository
'''Hasta ahora los actores solo soportan
un personaje por actor, sera necesario implementar un
repositorio de personajes con carateristicas similares
a las de actorsRepository y peliculaRepository, ademas de tener que
establecerlo como atributo de la clase App'''


class App():
    def __init__(self):
        self.repositorioPeliculasApp = PeliculaRepository()
        self.repositorioActorsApp = ActorsRepository()

    def menuActorPeliculas(self):
        print("1. Menu actores")
        print("2. Menu Peliculas")
        return int(input("\nIngrese la opcion a realizar: "))

    def menuPeliculas(self):
        print("1. Listar Peliculas")
        print("2. Agregar Pelicula")
        print("3. Modificar Peliculas")
        print("4. Eliminar Pelicula")
        print("5. Agregar un Actor a un Pelicula")
        return int(input("\nIngrese la opcion a realizar: "))

    def menuActores(self):
        print("1. Listar Actores/Actriz")
        print("2. Agregar Actor/Actriz")
        print("3. Modificar Actor/Actriz")
        print("4. Eliminar Actor/Actriz")
        return int(input("\nIngrese la opcion a realizar: "))


if __name__ == "__main__":
    app = App()
    servicePelicula = PeliculaService(app.repositorioPeliculasApp,
                                      app.repositorioActorsApp)
    serviceActors = ActorsService(app.repositorioActorsApp)
    while True:
        print("\n")
        opt = app.menuActorPeliculas()
        if opt == 1:
            while True:
                print("\n")
                opt = app.menuActores()
                if opt == 1:
                    serviceActors.listar()
                if opt == 2:
                    serviceActors.agregar()
                if opt == 3:
                    serviceActors.modificar()
                if opt == 4:
                    serviceActors.eliminar()
                if opt < 1 or opt > 4:
                    break
        if opt == 2:
            while True:
                print("\n")
                opt = app.menuPeliculas()
                if opt == 1:
                    servicePelicula.listar()
                if opt == 2:
                    servicePelicula.agregar()
                if opt == 3:
                    servicePelicula.modificar()
                if opt == 4:
                    servicePelicula.eliminar()
                if opt == 5:
                    servicePelicula.agregarActorPelicula()
                if opt < 1 or opt > 5:
                    break
        if opt < 1 or opt > 4:
            pass
