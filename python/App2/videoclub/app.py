from pelicula_service import PeliculaService
from pelicula_repository import PeliculaRepository
from actor_service import ActorService
from actor_repository import ActorRepository


class App():
    def __init__(self):
        self.peliculas_db = PeliculaRepository({})
        self.actores_db = ActorRepository({})

    def menu_pelicula(self):
        print("\n\n1. Listar peliculas")
        print("2. Agregar pelicula")
        print("3. Modificar pelicula")
        print("4. Eliminar pelicula")
        return int(input("Elija una opción: "))

    def menu_actor(self):
        print("\n\n1. Listar actores/actrices")
        print("2. Agregar actor/actriz")
        print("3. Modificar actor/actriz")
        print("4. Eliminar actor/actriz")
        return int(input("Elija una opción: "))

    def menu(self):
        print("\n\n1. Menú Películas")
        print("2. Menú Actores")
        return int(input("Elija una opción: "))


if __name__ == '__main__':
    app = App()
    while True:
        opcion = app.menu()
        if opcion == 1:
            while True:
                opcion_pelicula = app.menu_pelicula()
                if opcion_pelicula == 1:
                    service = PeliculaService(app.peliculas_db)
                    service.listar()
                    service = None
                if opcion_pelicula == 2:
                    service = PeliculaService(app.peliculas_db)
                    service.agregar_pelicula()
                    service = None
                if opcion_pelicula == 3:
                    service = PeliculaService(app.peliculas_db)
                    service.modificar()
                    service = None
                if opcion_pelicula == 4:
                    service = PeliculaService(app.peliculas_db)
                    service.eliminar()
                    service = None
                if opcion_pelicula < 1 or opcion_pelicula > 4:
                    break
        if opcion == 2:
            while True:
                opcion_actor = app.menu_actor()
                if opcion_actor == 1:
                    service = ActorService(app.actores_db)
                    service.listar()
                    service = None
                if opcion_actor == 2:
                    service = ActorService(app.actores_db)
                    service.agregar_actor()
                    service = None
                if opcion_actor == 3:
                    service = ActorService(app.actores_db)
                    service.modificar()
                    service = None
                if opcion_actor == 4:
                    service = ActorService(app.actores_db)
                    service.eliminar()
                    service = None
                if opcion_actor < 1 or opcion_actor > 4:
                    break
        if opcion < 1 or opcion > 2:
            break
