from actors import Actor
from personaje import Personaje


class ActorsService():
    def __init__(self, repoA):
        self.repoA = repoA

    def listar(self):
        actors = self.repoA.repoActors
        for k in actors:
            print(actors[k].getActor())

    def agregar(self, k=0, modif=False):
        if modif is False:
            k = input("\nIngrese el codigo de Actor: ")
        nombre = input("Ingrese el nombre: ")
        personajes = {}
        actor = Actor(nombre, personajes)
        self.repoA.repoActors[k] = actor
        self.listar()

    def modificar(self):
        k = input("\nIngrese codigo de Actor: ")
        del self.repoA.repoActors[k]
        self.agregar(True, k)

    def eliminar(self):
        k = input("\nIngrese el codigo de Actor: ")
        print(self.repoA.repoActors[k])
        yn = input("\n¿Seguro que desea eliminar este registro? Y/N\n")
        if yn.upper() == "Y":
            del self.repoA.repoActors[k]
            print("Registro eliminado!")

    def agregarPersonajeActor(self):
        kA = input("\nIngrese codigo de Actor: ")
        actor = self.repoA.repoActors[kA]
        print(actor.getActor(), "\n")
        nomPersonaje = input("Ingrese nombre del personaje: ")
        personaje = Personaje(nomPersonaje)
        actor.personajes['personajes'] = personaje
