from tkinter import Menu
from db_service_actor import DB_serviceActor


class BarraMenuActor():
    def __init__(self, root, botones):
        self.root = root
        self.botones = botones
        self.barraMenuActores = Menu(self.root)
        self.bbddMenu = Menu(self.barraMenuActores, tearoff=0)
        self.borrarMenu = Menu(self.barraMenuActores, tearoff=0)
        self.crudMenu = Menu(self.barraMenuActores, tearoff=0)

    def opciones_de_menu_actor(self):
        self.botones.destroy()
        self.root.config(menu=self.barraMenuActores, width=600, height=600)
        self.camposActor = DB_serviceActor(self.root)
        self.bbddMenu.add_command(
            label="Actor", command=self.camposActor.conexionDB)
        self.bbddMenu.add_command(
            label="Salir de Actor",
            command=self.camposActor.salirAplicacion)
        self.borrarMenu.add_command(
            label="Borrar campos de Actor",
            command=self.camposActor.borrarCampos)
        self.crudMenu.add_command(
            label="Crear Actor", command=self.camposActor.crear)
        self.crudMenu.add_command(
            label="Leer Actor", command=self.camposActor.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=self.camposActor.actualizar)
        self.crudMenu.add_command(
            label="Borrar Actor", command=self.camposActor.eliminar)

        self.barraMenuActores.add_cascade(
            label="BBDD Actor", menu=self.bbddMenu)
        self.barraMenuActores.add_cascade(
            label="Borrar Actor", menu=self.borrarMenu)
        self.barraMenuActores.add_cascade(
            label="CRUD Actor", menu=self.crudMenu)
