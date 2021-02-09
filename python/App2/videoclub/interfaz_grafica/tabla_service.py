from tkinter import Menu, Frame
from db_Actor_service import ActorServiceDB
from frame_actor import Actor
from db_pelicula_service import PeliculaServiceDB
from frame_pelicula import Pelicula


class TablaService():
    def __init__(self, root):
        self.miframe = Frame(root)
        self.miframe.pack()
        self.barraMenu = Menu(self.miframe)
        self.salir = Menu(self.barraMenu, tearoff=0)
        self.borrarMenu = Menu(self.barraMenu, tearoff=0)
        self.crudMenu = Menu(self.barraMenu, tearoff=0)

    def frame(self, frame_elegido):
        if frame_elegido:
            self.tabla = ActorServiceDB()
            self.actorFrame = Actor(self.miframe)
            self.actorFrame.cuadros()
            self.actorFrame.label()
        else:
            self.tabla = PeliculaServiceDB()
            self.peliculaFrmae = Pelicula(self.miframe)
            self.peliculaFrmae.cuadros()
            self.peliculaFrmae.label()

    def command_menu(self):
        self.barraMenu.add_cascade(label="salir", menu=self.salir)
        self.barraMenu.add_cascade(label="Borrar", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="CRUD", menu=self.crudMenu)

    def command_salir(self):
        self.salir.add_command(
            label="salir", command=self.tabla.cerrarConexionDB(self.miframe))

    def command_borrar(self):
        self.borrarMenu.add_command(
            label="Borrar campos", command=self.tabla.borrarCampos)

    def command_crud(self):
        self.crudMenu.add_command(
            label="Crear", command=self.tabla.crear)
        self.crudMenu.add_command(
            label="Leer", command=self.tabla.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=self.tabla.actualizar)
        self.crudMenu.add_command(
            label="Borrar", command=self.tabla.eliminar)
