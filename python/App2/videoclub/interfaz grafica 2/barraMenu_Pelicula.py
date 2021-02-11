from tkinter import Menu
from db_service_pelicula import DB_servicePelicula


class BarraMenuPelicula():
    def __init__(self, root, botones):
        self.root = root
        self.botones = botones
        self.barraMenuPelicula = Menu(self.root)
        self.bbddMenu = Menu(self.barraMenuPelicula, tearoff=0)
        self.borrarMenu = Menu(self.barraMenuPelicula, tearoff=0)
        self.crudMenu = Menu(self.barraMenuPelicula, tearoff=0)

    def opciones_de_menu_pelicula(self):
        self.botones.destroy()
        self.root.config(menu=self.barraMenuPelicula, width=700, height=700)
        self.camposPelicula = DB_servicePelicula(self.root)
        self.bbddMenu.add_command(
            label="Conectar", command=self.camposPelicula.conexionDB)
        self.bbddMenu.add_command(
            label="Salir",
            command=self.camposPelicula.salirAplicacion)
        self.borrarMenu.add_command(
            label="Borrar campos",
            command=self.camposPelicula.borrarCampos)
        self.crudMenu.add_command(
            label="Crear", command=self.camposPelicula.crear)
        self.crudMenu.add_command(
            label="Leer", command=self.camposPelicula.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=self.camposPelicula.actualizar)
        self.crudMenu.add_command(
            label="Eliminar", command=self.camposPelicula.eliminar)

        self.barraMenuPelicula.add_cascade(
            label="BBDD", menu=self.bbddMenu)
        self.barraMenuPelicula.add_cascade(
            label="Borrar", menu=self.borrarMenu)
        self.barraMenuPelicula.add_cascade(
            label="CRUD", menu=self.crudMenu)
