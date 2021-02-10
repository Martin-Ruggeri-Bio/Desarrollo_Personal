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
            label="Pelicula", command=self.camposPelicula.conexionDB)
        self.bbddMenu.add_command(
            label="Salir de Pelicula",
            command=self.camposPelicula.salirAplicacion)
        self.borrarMenu.add_command(
            label="Borrar campos de Pelicula",
            command=self.camposPelicula.borrarCampos)
        self.crudMenu.add_command(
            label="Crear Pelicula", command=self.camposPelicula.crear)
        self.crudMenu.add_command(
            label="Leer Pelicula", command=self.camposPelicula.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=self.camposPelicula.actualizar)
        self.crudMenu.add_command(
            label="Borrar Pelicula", command=self.camposPelicula.eliminar)

        self.barraMenuPelicula.add_cascade(
            label="BBDD Pelicula", menu=self.bbddMenu)
        self.barraMenuPelicula.add_cascade(
            label="Borrar Pelicula", menu=self.borrarMenu)
        self.barraMenuPelicula.add_cascade(
            label="CRUD Pelicula", menu=self.crudMenu)
