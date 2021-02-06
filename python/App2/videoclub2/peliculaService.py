from pelicula import Pelicula


class PeliculaService():
    def __init__(self, repoP, repoA):
        self.repo = repoP
        self.repoA = repoA

    def listar(self):
        peliculas = self.repo.repoPeliculas
        for k in peliculas:
            print(peliculas[k].getPelicula())

    def agregar(self, k=0, modif=False):
        if modif is False:
            k = input("\nIngrese el codigo de Pelicula: ")
        titulo = input("Ingrese el titulo: ")
        duracion = int(input("Ingrese duracion en minutos: "))
        genero = input("Ingrese el genero: ")
        actor = {}
        pelicula = Pelicula(titulo, duracion, genero, actor)
        self.repo.repoPeliculas[k] = pelicula
        self.listar()

    def modificar(self):
        k = input("\nIngrese codigo de Pelicula: ")
        del self.repo.repoPeliculas[k]
        self.agregar(True, k)

    def eliminar(self):
        k = input("\nIngrese el codigo de Pelicula: ")
        print(self.repo.repoPeliculas[k])
        yn = input("\n¿Seguro que desea eliminar este registro? Y/N\n")
        if yn.upper() == "Y":
            del self.repo.repoPeliculas[k]
            print("Registro eliminado!")

    def agregarActorPelicula(self):
        kP = input("\nIngrese codigo de Pelicula: ")
        pelicula = self.repo.repoPeliculas[kP]
        print(pelicula.getPelicula(), "\n")
        kA = input("Ingrese codigo de Actor: ")
        actor = self.repoA.repoActors[kA]
        print(actor.getActor(), "\n")
        pelicula.actores[kA] = actor.nombre
        print(pelicula.getPelicula(), "\n")


if __name__ == "__main__":
    service = PeliculaService()
    service.agregar()
    service.agregarActorPelicula()
