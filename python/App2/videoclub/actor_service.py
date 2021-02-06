from actor import Actor


class ActorService():
    def __init__(self, repository):
        self.repository = repository

    def listar(self):
        print("\n     Listando")
        for key in self.repository.actores:
            print("-> %s" % (self.repository.actores[key]))

    def agregar_actor(self):
        print("\n     Agregando")
        actor = Actor()
        actor.ingresar()
        self.repository.actores[actor.key] = actor

    def eliminar(self):
        print("\n     Eliminando")
        key = input("Ingrese código a Eliminar: ")
        del self.repository.actores[key]

    def modificar(self):
        print("\n     Modificando")
        key = input("Ingrese código a Modificar: ")
        actor = self.repository.actores[key]
        print("actor %s " % actor)
        actor.ingresar(True)
        self.repository.actores[key] = actor
