from tkinter import Frame, Button
from barra_menu.barraMenu_Actor import BarraMenuActor
from barra_menu.barraMenu_Pelicula import BarraMenuPelicula


class Botones():
    def __init__(self, root):
        self.root = root
        self.botones = Frame(self.root)
        self.barraMenuActores = BarraMenuActor(self.root, self.botones)
        self.barraMenuPelicula = BarraMenuPelicula(self.root, self.botones)

    def elegir(self):
        self.botones.pack()

        botonActor = Button(
            self.botones, text="Actor",
            command=self.barraMenuActores.opciones_de_menu_actor)
        botonActor.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        botonPelicula = Button(
            self.botones, text="Pelicula",
            command=self.barraMenuPelicula.opciones_de_menu_pelicula)
        botonPelicula.grid(row=1, column=1, sticky="e", padx=10, pady=10)
