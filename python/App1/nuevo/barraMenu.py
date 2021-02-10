from tkinter import Menu
from db_service import DB_service


class BarraMenu():
    def __init__(self, root):
        self.root = root
        self.barraMenu = Menu(self.root)
        self.root.config(menu=self.barraMenu, width=300, height=300)
        self.campos = DB_service(self.root)
        self.bbddMenu = Menu(self.barraMenu, tearoff=0)
        self.borrarMenu = Menu(self.barraMenu, tearoff=0)
        self.crudMenu = Menu(self.barraMenu, tearoff=0)

    def opciones_de_menu(self):
        self.bbddMenu.add_command(
            label="Conectar", command=self.campos.conexionDB)
        self.bbddMenu.add_command(
            label="salir", command=self.campos.salirAplicacion)

        self.borrarMenu.add_command(
            label="Borrar campos", command=self.campos.borrarCampos)

        self.crudMenu.add_command(label="Crear", command=self.campos.crear)
        self.crudMenu.add_command(label="Leer", command=self.campos.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=self.campos.actualizar)

        self.crudMenu.add_command(label="Borrar", command=self.campos.eliminar)
        self.barraMenu.add_cascade(label="BBDD", menu=self.bbddMenu)
        self.barraMenu.add_cascade(label="Borrar", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="CRUD", menu=self.crudMenu)
