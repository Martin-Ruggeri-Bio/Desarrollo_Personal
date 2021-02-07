from tkinter import Tk, Frame, Button, messagebox, Menu
from conexion_bd import ConexionDB


class App_VideoClub():
    def __init__(self):
        self.root = Tk()
        self.actor = 1
        self.pelicula = 0
        self.barraMenu = Menu(self.root)
        self.eleccion = Frame(self.root)
        self.root.mainloop()

    def menu(self):
        dbMenu = Menu(self.barraMenu, tearoff=0)
        dbMenu.add_command(
            label="Conectar a Pelicula", command=ConexionDB.conectar_tablas(
                self.root, self.pelicula))
        dbMenu.add_command(
            label="Conectar a Actor", command=ConexionDB.conectar_tablas(
                self.root, self.actor))
        dbMenu.add_command(
            label="salir", command=self.salirAplicacion)

        ayudaMenu = Menu(self.barraMenu, tearoff=0)
        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de ...")

        self.barraMenu.add_cascade(label="DB", menu=dbMenu)
        self.barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

    def button(self):
        self.eleccion.pack()

        botonActor = Button(
            self.eleccion, text="Actor", command=ConexionDB.conectar_tablas(
                self.root, self.pelicula))
        botonActor.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        botonPelicula = Button(
            self.eleccion, text="Pelicula", command=ConexionDB.conectar_tablas(
                self.root, self.actor))
        botonPelicula.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    def salirAplicacion(self):
        valor = messagebox.askquestion("Salir", "¿Deseas salir?")
        if valor == "yes":
            self.root.destroy()
