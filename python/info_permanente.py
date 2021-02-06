import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    def __init__(self):
        self.personas = []
        lista_personas = open("ficheroExterno", "ab+")
        lista_personas.seek(0)

        try:
            self.personas = pickle.load(lista_personas)
            print("se cargaron {} personas del fichero externo"
                  .format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            lista_personas.close()
            del(lista_personas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonaEnFichero()

    def guardarPersonaEnFichero(self):
        lista_personas = open("ficheroExterno", "wb+")
        pickle.dump(self.personas, lista_personas)
        lista_personas.close()
        del(lista_personas)

    def mostrarInfoFichero(self):
        fichero = open("ficheroExterno", "rb+")
        lista_personas = pickle.load(fichero)
        for persona in lista_personas:
            print(persona)
        print("\n")


miLista = ListaPersonas()
persona = Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFichero()
