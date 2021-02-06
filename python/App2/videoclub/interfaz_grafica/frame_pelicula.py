from tkinter import Entry, StringVar
from label_pelicula import LabelPelicula


class Pelicula():
    def __init__(self, framePelicula):
        self.framePelicula = framePelicula
        self.keyID = StringVar()
        self.titulo = StringVar()
        self.genero = StringVar()
        self.duracion = StringVar()
        self.actores = StringVar()

    def cuadros(self):
        cuadroID = Entry(self.framePelicula, textvariable=self.keyID)
        cuadroID.grid(row=0, column=1, padx=10, pady=10)

        cuadroNombre = Entry(self.framePelicula, textvariable=self.titulo)
        cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

        cuadroApellido = Entry(self.framePelicula, textvariable=self.genero)
        cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

        cuadroDireccion = Entry(self.framePelicula, textvariable=self.duracion)
        cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

        cuadroDireccion = Entry(self.framePelicula, textvariable=self.actores)
        cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

    def label(self):
        peliculaLabel = LabelPelicula(self.framePelicula)
        peliculaLabel.peliculaGrid()
