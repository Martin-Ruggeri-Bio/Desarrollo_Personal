from tkinter import Menu
from db_service.db_service_actor import DB_serviceActor


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
            label="Conectar_DB", command=self.camposActor.crearDB)
        self.bbddMenu.add_command(
            label="Salir",
            command=self.camposActor.salirAplicacion)
        self.borrarMenu.add_command(
            label="Borrar campos",
            command=self.camposActor.borrarCampos)
        self.crudMenu.add_command(
            label="Crear", command=self.camposActor.crear)
        self.crudMenu.add_command(
            label="Leer", command=self.camposActor.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=self.camposActor.actualizar)
        self.crudMenu.add_command(
            label="Borrar", command=self.camposActor.eliminar)

        self.barraMenuActores.add_cascade(
            label="BBDD", menu=self.bbddMenu)
        self.barraMenuActores.add_cascade(
            label="Borrar", menu=self.borrarMenu)
        self.barraMenuActores.add_cascade(
            label="CRUD", menu=self.crudMenu)
